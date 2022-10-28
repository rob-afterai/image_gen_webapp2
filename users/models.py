# from socket import fromshare
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from django import forms


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dir = ""  # models.CharField(max_length=100, default=".")
    dataset_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} Profile"
    
    # def save(self, *args, **kwargs):
    #     super().save(args, kwargs)


class Dataset(models.Model):
    title = models.CharField(max_length=100)
    last_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    path_to_images = models.CharField(max_length=200, default="default")
    settings_file = models.CharField(max_length=200, default="default")
    number_of_images = models.IntegerField(default=0)
    # object_names = models.


# content = models.TextField()
# image = models.ImageField(default='default.jpg', upload_to='profile_pics')
# author = models.ForeignKey(User, on_delete=models.CASCADE)


# class DatasetForm(forms.ModelForm):
#     class Meta:
#         model = Dataset
#         fields = ('title', 'settings_file')

# dataset_detail.html
# dataset_form.html
# ???


# create dataset
# save dataset

# /datagen is currently my create dataset page

# i guess we turn datagen / setup and view images tabs in to seperate pages
# generate data -> dataset_detail
# setup tab only becomes configurable 
# generate data page becomes setup tab only & links to static instance of dataset_detail page
