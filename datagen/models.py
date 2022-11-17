from django.db import models


class Obj(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')


# class Settings(models.Model):
#     # seed = models.
# 	# no_images
# 	# image_size
# 	# image_extension
# 	# objects_per_image
# 	# selected_objects
#     pass
