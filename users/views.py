from django.shortcuts import render, redirect
from wsgiref.util import FileWrapper
import mimetypes
from .forms import UserRegisterForm
from django.http import StreamingHttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from pathlib import Path
import os
from .models import Dataset
# from .source import simulation
# import json
# from django.http import JsonResponse
# from importlib import import_module
import sys
import shutil
from PIL import Image


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            dir = os.path.dirname(os.path.abspath(__file__))
            parts = dir.split('\\')
            username = form.cleaned_data.get('username')
            # linux (docker)
            profile_dir = "/".join(parts[:-1] + ["profiles", username])
            # windows
            # profile_dir = "\\".join(parts[:-1] + ["profiles", username])
            print("profile_dir: " + profile_dir)
            os.mkdir(profile_dir)
            print('Created profile at ' + str(profile_dir))
            form.save()
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    datasets = user.dataset_set.all()
    # if not isinstance(datasets, list):
    #     datasets = False
    # else:
    # print(str(datasets) + 'datasets@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    context = {
        'datasets': datasets  # Dataset.objects.all()  # User.dataset_set.objects.all()
    }
    return render(request, 'users/profile.html' , context)


def dataset(request, pk):
    # file = os.path.abspath(__file__)
    # dir = os.path.dirname(file)
    # parts = dir.split('\\')
    # abs_path = "\\".join(parts[:-2] + ['image_gen_website'])
    # print("abs_path: " + str(abs_path))
    # sys.path.insert(0, abs_path)

    username = request.user.username
    # print("user " + username)
    context = dict()
    print("request.user.profile.dataset_count = " + str(request.user.profile.dataset_count))
    # dataset = request.user.dataset_set.all()[0]
    dataset = Dataset.objects.get(pk=pk)
    rel_dir = '/' + '/'.join(['media', username, dataset.title, "image_thumbnails"])
    # request.user.dataset_count = 5
    print('dataset ' + str(dataset.path_to_images))
    # need list of path to each image, not dir
    dir_files = os.listdir(dataset.path_to_images + "/images")     # \\\\images
    image_paths = []
    count = 0
    names = []
    for file in dir_files:
        if file[-5:] == ".JPEG":
            image_paths.append([f"{rel_dir}/{file}", file])
            names.append(file)
            count += 1
    dataset.number_of_images = count/2
    dataset.save()
    context['dataset'] = dataset
    context['image_paths'] = image_paths
    context['image_names'] = names
    print(str(len(image_paths)) + " images")
    # print(image_paths[0])
    return render(request, 'users/dataset.html', context)
    # todo: just move the users folder into the project??


def dataset_create(request):
    context = dict()
    # context['url'] = ""
    print('dataset_create')

    # on create
    # if request.method == 'POST':
    # take json file & save
    # uploaded_file = request.FILES['document']
    # print(uploaded_file.name)
    # fs = FileSystemStorage()
    # settings_name = fs.save(uploaded_file.name, uploaded_file)
    # print(settings_name)

    # import datagen function
    dir = os.path.dirname(os.path.abspath(__file__))
    print("dir: " + dir)
    parts = dir.split('/')  # \\

    # get username & name new dataset
    if not request.user.is_authenticated:
        return render(request, 'users/dataset_create.html', context)
    username = request.user.username
    print(username)
    print('profile ' + str(request.user.profile))
    request.user.profile.dataset_count += 1
    request.user.profile.save()
    count = request.user.profile.dataset_count
    dataset_name = "dataset" + str(count)
    # print("request.user.profile.dataset_count = " + str(request.user.profile.dataset_count))

    dataset = Dataset(user=request.user)
    dataset.title = dataset_name
    # user_dataset_path = "\\".join(parts[:-1] + ["profiles", username, dataset_name])
    user_dataset_path = "/".join(parts[:-1] + ["profiles", username, dataset_name])
    dataset.path_to_images = user_dataset_path
    dataset.save()
    print("creating new dataset at: " + user_dataset_path)
    if not os.path.isdir(user_dataset_path):
        os.mkdir(user_dataset_path)
        os.mkdir(user_dataset_path + "/images")
        os.mkdir(user_dataset_path + "/image_thumbnails")
        os.mkdir(user_dataset_path + "/label_files")
        os.mkdir(user_dataset_path + "/generate_scripts")

    # fill context
    context['content'] = dir
    print('dataset ' + str(dataset.path_to_images))
    # context['dataset_name'] = dataset_name

    #     with open(abs_dir, 'r') as f:
    #         json_content = json.load(f)
    #     datagen_module.generate_images()
    #     # print(MEDIA_URL)
    #     context['url'] = abs_dir  # fs.url(name)
    #     context['content'] = json_content
    print("request.user.profile.dataset_count = " + str(request.user.profile.dataset_count))
    return redirect('dataset', dataset.pk)


def dataset_generate_images(request, pk):
    context = dict()

    # get username & name new dataset
    if not request.user.is_authenticated:
        return render(request, 'users/dataset_create.html', context)
    username = request.user.username
    
    # dataset = request.user.dataset_set.all()[0]
    dataset = Dataset.objects.get(pk=pk)
    

    # call generate images
    paths = dict()
    # paths['json_settings'] = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\common\\base_settings.json"
    # base_dir = dataset.path_to_images.replace('\\', '\\\\') + "\\\\"
    # paths['images'] = base_dir + "images"
    # paths['generate_scripts'] = base_dir + "generate_scripts"
    # paths['label_files'] = base_dir + "label_files"
    # paths['image_thumbnails'] = base_dir + "image_thumbnails"
    # paths['blender_exe'] = "C:\\Program Files\\Blender Foundation\\Blender 2.83\\blender.exe"
    # paths['blender_base'] = "C:\\\\Users\\\\RMSmi\\\\PycharmProjects\\\\islenn\\\\Simulator\\\\fut__kit900_283.blend"
    dataset_dir = dataset.path_to_images
    print("dataset_dir: " + dataset_dir)
    web_dir = dataset_dir + "/../../.."
    paths['json_settings'] = web_dir + "/users/common/base_settings.json"
    # dataset_dir =  + "/"  # .replace('\\', '\\\\') + "\\\\"
    paths['images'] = dataset_dir + "/images"
    paths['generate_scripts'] = dataset_dir + "/generate_scripts"
    paths['label_files'] = dataset_dir + "/label_files"
    paths['image_thumbnails'] = dataset_dir + "/image_thumbnails"
    paths['blender_exe'] = web_dir + "/users/Blender 2.83/blender.exe"
    paths['blender_base'] = web_dir + "/users/common/fut__kit900_283.blend"
    print(os.listdir(dataset_dir + "/../../.."))
    print(paths)
    # success = simulation.generate_images(paths)

    # save thumbnails
    images = paths['images'] + "/"  # paths['images'].replace('\\\\', '\\') + "\\"
    image_thumbnails = paths['image_thumbnails'] + "/"  # paths['image_thumbnails'].replace('\\\\', '\\') + "\\"
    for image_name in os.listdir(paths['images']):
        infile = images + image_name
        im = Image.open(infile)
        resizedImage = im.resize((int(100), int(100)), Image.ANTIALIAS)
        outfile = image_thumbnails + image_name
        resizedImage.save(outfile, "JPEG")

    # fill context
    context['content'] = dir
    # context['dataset_name'] = dataset_name
    return redirect('dataset', pk)


def delete_dataset(request, pk):
    print('deleting')
    if request.method=='POST':
        dataset = Dataset.objects.get(pk=pk)
        print("dataset: " + str(dataset))
        shutil.rmtree(dataset.path_to_images)
        dataset.delete()
        # dataset.save()
        print("no_datasets: " + str(len(request.user.dataset_set.all()) + 1))
    return redirect('profile')


def download_dataset(request, pk):
    chunk_size = 8192
    dataset = Dataset.objects.get(pk=pk)
    src_folder = dataset.path_to_images + "/images"
    dst_folder = dataset.path_to_images + "_zip"
    print("src_folder: " + src_folder)
    print("dst_folder: " + dst_folder)
    zip_folder = dataset.path_to_images + "\\" + dataset.title
    print("zip_folder: " + zip_folder)
    shutil.make_archive(zip_folder, 'zip', src_folder)
    zip_folder_zip = zip_folder + ".zip"
    response = StreamingHttpResponse(FileWrapper(open(zip_folder_zip, 'rb'), chunk_size),
        content_type=mimetypes.guess_type(zip_folder)[0])
    response['Content-Length'] = os.path.getsize(zip_folder_zip)
    response['Content-Disposition'] = f"Attachment; filename={zip_folder_zip}"  # dataset.title
    return response


def save_settings_file(request, pk):
    dataset = Dataset.objects.get(pk=pk)
    # copy from base to dataset & update with form
    dataset.path_to_images
    # form = DatasetForm
    return redirect('dataset', pk)
