from django.urls import path
from . import views as datagen_views


urlpatterns = [
    path('', datagen_views.home, name='home'),
    path('contact/', datagen_views.contact, name='contact'),

    path('datagen/', datagen_views.datagen, name='datagen'),
    path('datagen/download/', datagen_views.download_dataset, name='download'),
    # path('datagen/generate_images', datagen_views.generate_images, name='generate_images'),
    # path('datagen/remove_obj_from_dataset/', datagen_views.remove_obj_from_dataset, name='remove_obj_from_dataset'),

    path('library/', datagen_views.library, name='library'),
    # path('library/add_obj_to_dataset/', datagen_views.add_obj_to_dataset, name='add_obj_to_dataset'),
]
