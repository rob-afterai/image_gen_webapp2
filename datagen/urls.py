from django.urls import path
from . import views as datagen_views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', datagen_views.home, name='home'),
    path('datagen/', datagen_views.datagen, name='datagen'),
    # path('register/', user_views.register, name='register'),
    # path('', include('datagen.urls')),
]
