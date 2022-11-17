import re
from django.shortcuts import render
from django.http import HttpResponse
import os
from pathlib import Path
from django.shortcuts import render, redirect
import requests
from django.core.files.storage import FileSystemStorage
from .models import Obj
from django.http import StreamingHttpResponse
import shutil
from wsgiref.util import FileWrapper
import mimetypes
# from paypal.standard.models import ST_PP_COMPLETED
# from paypal.standard.ipn.signals import valid_ipn_received
# from paypal.standard.forms import PayPalPaymentsForm
# from paypal.standard.models import ST_PP_COMPLETED
# from paypal.standard.ipn.signals import valid_ipn_received
from azure.storage.blob import ContainerClient  # BlobClient
import json
from django.core.files.storage import default_storage
from django.apps import apps
Obj = apps.get_model(app_label='users', model_name='Obj')


BASE_DIR = Path(__file__).resolve().parent.parent


def home(request):
    # return HttpResponse('<h1>Datagen Home</h1>')
    return render(request, 'datagen/home.html')


def datagen(request):
    image_paths = []
    abs_dir = os.path.join(BASE_DIR, 'datagen', 'static', 'datagen', "image_thumbnails")
    rel_dir = '/' + '/'.join(['static', 'datagen', 'image_thumbnails'])
    dir_files = os.listdir(abs_dir)
    for file in dir_files:
        image_paths.append([f"{rel_dir}/{file}", file])
    
    image_profiles_path = "C:/Users/RMSmi/Documents/GitHub/image_gen_webapp2/datagen/static/datagen/objs"
    rel_dir = "/static/datagen/objs"
    dir_files = os.listdir(image_profiles_path)
    object_paths = []
    for file in dir_files:
        object_paths.append([f"{rel_dir}/{file}", file])

    context = {
        'object_paths': object_paths,
        'image_paths': image_paths,
        'num_images': len(image_paths)
    }
    return render(request, 'datagen/datagen.html', context)


def library(request):
    context = dict()
    con_str='DefaultEndpointsProtocol=https;AccountName=afteraisub1storage;AccountKey=pmabm0K12K0TGF2DiHvLd8Z0hg+/EA3UEs/eAd2KXE1Txj9s/VDxNowVQdixuv1RK83qeY97UlXH+AStJtJ6Iw==;EndpointSuffix=core.windows.net'

    if request.method == 'POST':
        print('post method')
        if 'obj_file' in request.FILES:
            # check file is valid - size limit & extension
            uploaded_file = request.FILES['obj_file']
            print('uploaded_file: ' + str(uploaded_file))
            if not uploaded_file._name[-4:] == ".obj":
                print("file is not a .obj")
                
            elif uploaded_file.size > 1_000_000:
                print('uploaded file size is ' + str(uploaded_file.size) + \
                '  is greater allowed size 10^6. Try removing verticed from the .obj')
            
            elif len(Obj.objects.all().filter(name=uploaded_file._name)) > 0:
                print('File already exists, please choose another name')
            
            else:
                # upload to azure
                print('uploading new obj')
                print(type(uploaded_file))
                container_name = request.user.username
                container_client = ContainerClient.from_connection_string(con_str, container_name)
                dst = "objs/" + uploaded_file._name
                print("dst: " + dst)
                blob_client = container_client.get_blob_client(dst)
                blob_client.upload_blob(uploaded_file)
                
                # store in database
                new_obj = Obj(user=request.user, name=uploaded_file._name)
                new_obj.save()
                print('obj saved to database')
    
    # # get objs in library (todo - real objs not just imgs)
    # if request.user.is_authenticated:
    #     user_imgs_dir = "profiles/"  + request.user.username + "/objs"
    #     dir_files = os.listdir(user_imgs_dir)
    #     for file in dir_files:
    #         path = "/media/" + request.user.username + "/objs/" + file
    #         user_imgs.append([path, file])

    # get the names too
    container_name = "0-library"
    # container_client = ContainerClient.from_connection_string(con_str, container_name)
    # only display the first 10?

    # for file in dir_files:
    #     image_paths.append([f"{rel_dir}/{file}", file])
    #     names.append(file)

    # context['user_logged_in'] = user.
    context['user_objs'] = Obj.objects.filter(user_id=request.user.id)    # user=request.user
    context['lib_objs'] = Obj.objects.filter(user_id=1)
    # context['image_paths'] = image_paths
    # context['image_names'] = names
    # context['no_images'] = len(names)
    # print(str(len(image_paths)) + " images")
    return render(request, 'datagen/library.html', context)


def add_obj_to_dataset(request, pk):
    print('add_obj_to_dataset')
    # user.active_dataset.objects.add(selected_obj)
    # user.active_dataset.objs[name]
    user = request.user
    return redirect('datagen')


def remove_obj_from_dataset(request):
    print('remove_obj_from_dataset')
    return redirect('datagen')


def download_dataset(request):
    print('Beginning download')
    file_name = "scene_000000.JPEG"
    blob_sas_url = 'https://afteraisub1storage.blob.core.windows.net/imgs?sp=racwdl&st=2022-10-24T20:37:57Z&se=2022-10-25T04:37:57Z&spr=https&sv=2021-06-08&sr=c&sig=Sw5x2hhDdu%2FcD3Yyh1X4b71hOO1k73SYtD3XCT38Jmo%3D'
    r = requests.get(blob_sas_url, stream=True)
    response = StreamingHttpResponse(streaming_content=r)
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response


def contact(request):
    search_term = ''

    if 'search' in request.GET:
        search_term = request.GET['search']
        print('searching for "' + search_term + "\"")
        user_imgs_dir = "profiles/"  + request.user.username + "/objs"
        dir_files = os.listdir(user_imgs_dir)
        # articles = Article.objects.all().filter(feeder__icontains=search_term) 
        # now

    # articles = Article.objects.all()
    context = dict()
    # context = {'articles' : articles, 'search_term': search_term }
    return render(request, 'datagen/contact.html', context)


def view_that_asks_for_money(request):

    # What you want the button to do.
    paypal_dict = {
        "business": "receiver_email@example.com",
        "amount": "10000000.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri(reverse('your-return-view')),
        "cancel_return": request.build_absolute_uri(reverse('your-cancel-view')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "payment.html", context)


def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # WARNING !
        # Check that the receiver email is the same we previously
        # set on the `business` field. (The user could tamper with
        # that fields on the payment form before it goes to PayPal)
        if ipn_obj.receiver_email != "receiver_email@example.com":
            # Not a valid payment
            return

        # ALSO: for the same reason, you need to check the amount
        # received, `custom` etc. are all what you expect or what
        # is allowed.

        # Undertake some action depending upon `ipn_obj`.
        if ipn_obj.custom == "premium_plan":
            price = ...
        else:
            price = ...

        if ipn_obj.mc_gross == price and ipn_obj.mc_currency == 'USD':
            ...
    else:
        #...
        pass


# download code to delete
# chunk_size = 8192
# dataset = Dataset.objects.get(pk=pk)
# src_folder = dataset.path_to_images + "/images"
# dst_folder = dataset.path_to_images + "_zip"
# print("src_folder: " + src_folder)
# print("dst_folder: " + dst_folder)
# zip_folder = dataset.path_to_images + "\\" + dataset.title
# print("zip_folder: " + zip_folder)
# shutil.make_archive(zip_folder, 'zip', src_folder)
# zip_folder_zip = zip_folder + ".zip"
# dl_zip = 'https://drive.google.com/uc?id=1LLO7T7H7Sy7O0I6UhNhxfLbARCiC7VD6'
# output = "C:\Users\User\Downloads"
# print('Beginning download')
# gdown.download(dl_zip, quiet=False)
# response['Content-Length'] = os.path.getsize(zip_folder_zip)
# response['Content-Disposition'] = f"Attachment; filename={zip_folder_zip}"  # dataset.title
# return response
# return redirect('datagen/datagen.html')
# key = 'pmabm0K12K0TGF2DiHvLd8Z0hg+/EA3UEs/eAd2KXE1Txj9s/VDxNowVQdixuv1RK83qeY97UlXH+AStJtJ6Iw=='
# container_name = 'imgs'
# con_str='DefaultEndpointsProtocol=https;AccountName=afteraisub1storage;AccountKey=pmabm0K12K0TGF2DiHvLd8Z0hg+/EA3UEs/eAd2KXE1Txj9s/VDxNowVQdixuv1RK83qeY97UlXH+AStJtJ6Iw==;EndpointSuffix=core.windows.net'
# container_client = ContainerClient.from_connection_string(con_str, container_name)
# file_name = "scene_000000.JPEG"
# blob_client = container_client.get_blob_client(file_name)
# with open(file=download_file_path, mode="wb") as download_file:
#     # download_file.write(container_client.download_blob(blob.name).readall())
#     download_stream = blob_client.download_blob()
#     download_stream.readinto(download_file)
# zip_folder_zip = download_file_path
# response = StreamingHttpResponse(FileWrapper(open(zip_folder_zip, 'rb'), chunk_size),
#     content_type=mimetypes.guess_type(zip_folder)[0])
# blob_sas_token = 'sp=racwdl&st=2022-10-24T20:37:57Z&se=2022-10-25T04:37:57Z&spr=https&sv=2021-06-08&sr=c&sig=Sw5x2hhDdu%2FcD3Yyh1X4b71hOO1k73SYtD3XCT38Jmo%3D'
