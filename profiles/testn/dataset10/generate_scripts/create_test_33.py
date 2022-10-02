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


# 437
ob = bpy.context.scene.objects[437]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.30418308617077994, 0, -0.8036784811819788)
# rotation
bpy.ops.transform.rotate(value=2.9733261676661975, orient_axis='X')
bpy.ops.transform.rotate(value=1.4741256391878899, orient_axis='Y')
bpy.ops.transform.rotate(value=2.93799720727373, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.9821519717879876, 0.4654395512247682, 0.28187532169425755))
ob.select_set(False)

# 527
ob = bpy.context.scene.objects[527]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.8833004134210456, 0, -1.3592532559024244)
# rotation
bpy.ops.transform.rotate(value=1.8120366756623723, orient_axis='X')
bpy.ops.transform.rotate(value=0.14829402427713725, orient_axis='Y')
bpy.ops.transform.rotate(value=1.525936397201177, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.3315229484364086, 1.4701566774995956, 1.0199758535261887))
ob.select_set(False)

# 107
ob = bpy.context.scene.objects[107]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.059775712563236, 0, 3.303427852728108)
# rotation
bpy.ops.transform.rotate(value=1.9710154630857228, orient_axis='X')
bpy.ops.transform.rotate(value=1.1062317389408625, orient_axis='Y')
bpy.ops.transform.rotate(value=1.4223706270790153, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.6833239207300261, 0.6684287540103442, 0.8337156249114288))
ob.select_set(False)

# 393
ob = bpy.context.scene.objects[393]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.6068890413229675, 0, -1.8080122745995446)
# rotation
bpy.ops.transform.rotate(value=3.059780356226977, orient_axis='X')
bpy.ops.transform.rotate(value=3.0963171855462344, orient_axis='Y')
bpy.ops.transform.rotate(value=0.017033730775060804, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.9829498042822387, 0.32238041022409814, 0.5963806575770643))
ob.select_set(False)

# 39
ob = bpy.context.scene.objects[39]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.6683108210047837, 0, 0.3421089119710654)
# rotation
bpy.ops.transform.rotate(value=2.122510655658521, orient_axis='X')
bpy.ops.transform.rotate(value=0.7825792618630464, orient_axis='Y')
bpy.ops.transform.rotate(value=3.0843824244557028, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.02653504440876464, 1.8932845811925623, 1.601597080176516))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 16.40223983175752
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_33.JPEG"
bpy.ops.render.render(write_still=True)


