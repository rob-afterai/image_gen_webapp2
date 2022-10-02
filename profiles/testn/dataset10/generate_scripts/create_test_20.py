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


# 48
ob = bpy.context.scene.objects[48]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.5537897359595165, 0, 0.43781028241743325)
# rotation
bpy.ops.transform.rotate(value=0.3427945444412653, orient_axis='X')
bpy.ops.transform.rotate(value=1.5036806289498883, orient_axis='Y')
bpy.ops.transform.rotate(value=1.5514400263688692, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8472166576378966, 0.735118891855542, 0.7287623353717907))
ob.select_set(False)

# 291
ob = bpy.context.scene.objects[291]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.047322517542447, 0, 1.931744157069903)
# rotation
bpy.ops.transform.rotate(value=0.2859394859744575, orient_axis='X')
bpy.ops.transform.rotate(value=0.09836466585556408, orient_axis='Y')
bpy.ops.transform.rotate(value=2.8092880701646896, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.2018493583877876, 1.7912850977888628, 0.320362755767998))
ob.select_set(False)

# 109
ob = bpy.context.scene.objects[109]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.3523008266387775, 0, -0.27083863457453283)
# rotation
bpy.ops.transform.rotate(value=1.142593049027887, orient_axis='X')
bpy.ops.transform.rotate(value=0.6801176473037505, orient_axis='Y')
bpy.ops.transform.rotate(value=1.7907098407802589, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8397712426447237, 0.6727199047855279, 1.2897320205260463))
ob.select_set(False)

# 151
ob = bpy.context.scene.objects[151]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.0657220051898477, 0, 0.47973573262075764)
# rotation
bpy.ops.transform.rotate(value=1.1206916805755214, orient_axis='X')
bpy.ops.transform.rotate(value=0.6243216447431241, orient_axis='Y')
bpy.ops.transform.rotate(value=0.6475949586904399, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.21141840052281125, 0.3147450289940612, 1.4635931350642815))
ob.select_set(False)

# 554
ob = bpy.context.scene.objects[554]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.6041162574178509, 0, -1.8413685485266784)
# rotation
bpy.ops.transform.rotate(value=1.9374978504841276, orient_axis='X')
bpy.ops.transform.rotate(value=1.2802951218044551, orient_axis='Y')
bpy.ops.transform.rotate(value=1.7444807020783695, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.0161262241800302, 1.2370343773660344, 0.41470993922997157))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 8.178344138989369
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_20.JPEG"
bpy.ops.render.render(write_still=True)


