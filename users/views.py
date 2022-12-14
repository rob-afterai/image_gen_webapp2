from django.shortcuts import render, redirect
from wsgiref.util import FileWrapper
import mimetypes
from .forms import UserRegisterForm, DatasetForm
from django.http import StreamingHttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from pathlib import Path
import os
from .models import Dataset, Obj
import sys
import shutil
import json
# from PIL import Image
from azure.storage.blob import BlobServiceClient, ContainerClient


connect_str = "DefaultEndpointsProtocol=https;AccountName=afteraisub1storage;AccountKey=pmabm0K12K0TGF2DiHvLd8Z0hg+/EA3UEs/eAd2KXE1Txj9s/VDxNowVQdixuv1RK83qeY97UlXH+AStJtJ6Iw==;EndpointSuffix=core.windows.net"


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username').lower()
            # todo: if number of symbol in username, fail.
            messages.success(request, f'Account created for {username}!')
            blob_service_client = BlobServiceClient.from_connection_string(connect_str)
            container_client = blob_service_client.create_container(username)
            print('Created user ' + str(username))
            print('Created container ' + str(container_client))
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    datasets = user.dataset_set.all()
    context = {
        'datasets': datasets
    }
    return render(request, 'users/profile.html' , context)


def dataset_create(request):
    print('dataset_create')
    if not request.user.is_authenticated:
        print('user not authenticated')
        return redirect('home')
    
    # update profile
    print('profile ' + str(request.user.profile))
    request.user.profile.dataset_count += 1
    request.user.profile.save()

    # create dataset
    dataset = Dataset(user=request.user)
    dataset.name = "dataset" + str(request.user.profile.dataset_count)
    dataset.save()
    print('dataset created')
    return redirect('dataset' , dataset.pk)


def dataset(request, pk):
    # settings
    dataset = Dataset.objects.get(pk=pk)
    form = DatasetForm()

    if request.method == "POST":
        # search for objs
        print('post')
        if 'searched' in request.POST:
            print('searched')
            searched = request.POST['searched']
            obj = Obj.objects.filter(name__contains=searched).first()
            if obj:
                print("found " + obj.name)
                # add obj to dataset obj list as a json string
                objs_json = json.loads(dataset.objs_list_json_str)
                objs_json.append(obj.name)
                dataset.objs_list_json_str = json.dumps(objs_json)
                dataset.save()
                # for obj_name in objs_json:
                # o = Obj.objects.filter(name=obj.name).first()
                # context['lib_objs'].append(o)
        # form
        else:
            form = DatasetForm(request.POST)
            if form.is_valid():
                dataset.no_images = form.cleaned_data.get('no_images')
                dataset.image_height = form.cleaned_data.get('image_height')
                dataset.image_width = form.cleaned_data.get('image_width')
                dataset.image_extension = form.cleaned_data.get('image_extension')
                dataset.color_mode = form.cleaned_data.get('color_mode')
                dataset.segmented_labelling = form.cleaned_data.get('segmented_labelling')
                dataset.json_label = form.cleaned_data.get('json_label')
                dataset.save()
                print('dataset saved')
            else:
                print('form invalid')
        return redirect('dataset', pk)

    context = dict()
    context['lib_objs'] = []
    for ob_name in json.loads(dataset.objs_list_json_str):
        o = Obj.objects.get(name=ob_name)
        context['lib_objs'].append(o)
    context['dataset'] = dataset
        
    # # update form with dataset
    # print("no imgs " + str(dataset.no_images))
    # setattr(form, 'no_images', dataset.no_images)
    # setattr(form, 'image_height', dataset.image_height)
    # setattr(form, 'image_width', dataset.image_width)
    # setattr(form, 'image_extension', dataset.image_extension)
    # setattr(form, 'color_mode', dataset.color_mode)
    # setattr(form, 'segmented_labelling', dataset.segmented_labelling)
    # setattr(form, 'json_label', dataset.json_label)
    context["form"] = form

    # get generated images
    dir_files = []
    image_paths = []
    count = 0
    names = []
    # for file in dir_files:
    #     if file[-5:] == ".JPEG":
    #         image_paths.append([f"{rel_dir}/{file}", file])
    #         names.append(file)
    #         count += 1
    context['image_paths'] = image_paths
    context['image_names'] = names
    return render(request, 'users/dataset.html', context)


# def save(request, pk):
#     dataset = Dataset.objects.get(pk=pk)
#     form = DatasetForm(request.POST)
#     if form.is_valid():
#         dataset.no_images = form['no_images']
#         dataset.image_height = form['image_height']
#         dataset.image_width = form['image_width']
#         dataset.image_extension = form.cleaned_data['image_extension']
#         dataset.color_mode = form.cleaned_data['color_mode']
#         dataset.segmented_labelling = form.cleaned_data['segmented_labelling']
#         dataset.json_label = form.cleaned_data['json_label']
#         dataset.save()
#         print('save')
#     return redirect('dataset', pk)


def remove_obj(request, pk, obj_pk):
    dataset = Dataset.objects.get(pk=pk)
    obj = Obj.objects.get(pk=obj_pk)
    objs_json = json.loads(dataset.objs_list_json_str)
    print('removing obj ' + str(obj.name))
    new_list = []
    for o in objs_json:
        if o != obj.name:
            new_list.append(o)
    dataset.objs_list_json_str = json.dumps(new_list)
    dataset.save()
    return redirect('dataset', pk)


def test(request):
    if request.method == "POST":
        print('post')
        form = DatasetForm(request.POST)
        # if form.is_valid():
        no_images = form.cleaned_data['no_images']
        ds = Dataset()
        ds.no_images = no_images
        # ds.save()
    else:
        form = DatasetForm()
    return render(request, "users/test.html", {"form":form})


def generate_images(request, pk):
    # 1. get database and container
    jobs_container = ContainerClient.from_connection_string(connect_str, "jobs")
    dataset = Dataset.objects.get(pk=pk)
    blob_name = request.user.username + "/" + dataset.name + ".json"

    # 2. write params to dict
    settings_dict = dict()
    settings_dict['username'] = request.user.username
    settings_dict['dataset_name'] = dataset.name
    settings_dict["no_images"] = dataset.no_images
    settings_dict["image_height"] = dataset.image_height
    settings_dict["image_width"] = dataset.image_width
    settings_dict["image_extension"] = dataset.image_extension
    settings_dict["color_mode"] = dataset.color_mode
    settings_dict['segmented_labelling'] = dataset.segmented_labelling
    settings_dict['json_label'] = dataset.json_label

    objs_json = json.loads(dataset.objs_list_json_str)
    settings_dict['objects'] = []
    for obj_name in objs_json:
        settings_dict['objects'].append(obj_name)

    # 3. upload to job container
    json_str = json.dumps(settings_dict, indent=4)
    blob_client = jobs_container.get_blob_client(blob_name)
    blob_client.upload_blob(json_str)

    print("Sending instructions to server for " + dataset.name)
    # return success message
    return redirect('dataset', pk)


def download_dataset(request, pk):
    chunk_size = 8192
    dataset = Dataset.objects.get(pk=pk)
    src_folder = dataset.path_to_images + "/images"
    dst_folder = dataset.path_to_images + "_zip"
    print("src_folder: " + src_folder)
    print("dst_folder: " + dst_folder)
    # zip_folder = dataset.path_to_images + "\\" + dataset.title
    print("zip_folder: " + zip_folder)
    shutil.make_archive(zip_folder, 'zip', src_folder)
    zip_folder_zip = zip_folder + ".zip"
    response = StreamingHttpResponse(FileWrapper(open(zip_folder_zip, 'rb'), chunk_size),
        content_type=mimetypes.guess_type(zip_folder)[0])
    response['Content-Length'] = os.path.getsize(zip_folder_zip)
    response['Content-Disposition'] = f"Attachment; filename={zip_folder_zip}"  # dataset.title
    return response


def delete_dataset(request, pk):
    print('deleting')
    if request.method=='POST':
        dataset = Dataset.objects.get(pk=pk)
        print("dataset: " + str(dataset))
        # todo: delete folder in azure
        dataset.delete()
        print("no_datasets: " + str(len(request.user.dataset_set.all()) + 1))
    return redirect('profile')
