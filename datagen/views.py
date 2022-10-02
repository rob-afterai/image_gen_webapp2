from django.shortcuts import render
from django.http import HttpResponse
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def home(request):
    # return HttpResponse('<h1>Datagen Home</h1>')
    return render(request, 'datagen/home.html')


def datagen(request):
    # return HttpResponse('<h1>Datagen About</h1>')
    image_paths = []
    abs_dir = os.path.join(BASE_DIR, 'datagen', 'static', 'datagen', "image_thumbnails")
    rel_dir = '/' + '/'.join(['static', 'datagen', 'image_thumbnails'])

    # items = thumbnail_dir.split('\\')
    # dir_forward_slash = '/'.join(items)
    dir_files = os.listdir(abs_dir)
    for file in dir_files:
        image_paths.append(f"{rel_dir}/{file}")

    context = {
        'image_paths': image_paths,
        'num_images': len(image_paths)
    }
    return render(request, 'datagen/datagen.html', context)
