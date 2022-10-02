import bpy
import random
import math

# test
bpy.context.scene.eevee.taa_render_samples = 32
# bpy.context.scene.render.use_compositing = True
bpy.context.scene.render.film_transparent = True

bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080
for ob in bpy.context.scene.objects:
    ob.hide_render = True
    ob.hide_set(True)
    ob.location = (0, 0, 0)

cam = bpy.context.scene.objects['Camera']
cam.hide_render = True
cam.select_set(True)
cam.location = (0, -50, 0)
cam.data.ortho_scale = 10
cam.select_set(False)
cam.rotation_euler = (math.pi/2, 0, 0)


# 185
ob = bpy.context.scene.objects[185]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.3024103092765316, 0, -4.486859724972809)
# rotation
bpy.ops.transform.rotate(value=1.7763519088958015, orient_axis='X')
bpy.ops.transform.rotate(value=1.3775944267536804, orient_axis='Y')
bpy.ops.transform.rotate(value=0.5901667846679804, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.7478759805962527, 1.401455056177806, 1.084366375828602))
ob.select_set(False)

# 144
ob = bpy.context.scene.objects[144]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.5003134891139172, 0, -4.3541071734452705)
# rotation
bpy.ops.transform.rotate(value=1.0128642469114084, orient_axis='X')
bpy.ops.transform.rotate(value=0.1670320132219349, orient_axis='Y')
bpy.ops.transform.rotate(value=0.49581729458806445, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.17940809549873116, 1.0208208395704865, 1.2302379391087634))
ob.select_set(False)

# 67
ob = bpy.context.scene.objects[67]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.0926288958412647, 0, 0.9101073017007701)
# rotation
bpy.ops.transform.rotate(value=1.5220116199182074, orient_axis='X')
bpy.ops.transform.rotate(value=2.0856229792413528, orient_axis='Y')
bpy.ops.transform.rotate(value=1.0298016174256102, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.3350074172544082, 1.805760823424241, 1.096823094166032))
ob.select_set(False)

# 260
ob = bpy.context.scene.objects[260]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.9431815645620265, 0, -0.15467201937455322)
# rotation
bpy.ops.transform.rotate(value=0.12442009623587101, orient_axis='X')
bpy.ops.transform.rotate(value=1.49944200605083, orient_axis='Y')
bpy.ops.transform.rotate(value=1.5380222986876018, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.8364273558227784, 1.3407689727651562, 1.8190326658007554))
ob.select_set(False)

# 6
ob = bpy.context.scene.objects[6]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.375036483977814, 0, -2.8396126158423387)
# rotation
bpy.ops.transform.rotate(value=0.542214260117046, orient_axis='X')
bpy.ops.transform.rotate(value=1.7003857916709846, orient_axis='Y')
bpy.ops.transform.rotate(value=1.195935863026756, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.3102789964127597, 0.05635174118012043, 0.9800320383113312))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 4.45652675824324
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_71.JPEG"
bpy.ops.render.render(write_still=True)


