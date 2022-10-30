from django.urls import path
from . import views as datagen_views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', datagen_views.home, name='home'),
    path('datagen/', datagen_views.datagen, name='datagen'),
    path('library/', datagen_views.library, name='library'),
    path('contact/', datagen_views.contact, name='contact'),
    path('datagen/download/', datagen_views.download_dataset, name='download'),
    path('library/add_obj_to_dataset/', datagen_views.add_obj_to_dataset, name='add_obj_to_dataset'),
    # path('library/upload_obj/', datagen_views.upload_obj, name='upload_obj'),
    # path('register/', user_views.register, name='register'),
    # path('', include('datagen.urls')),
]
