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


# 287
ob = bpy.context.scene.objects[287]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.8776363857768548, 0, -2.732101941975969)
# rotation
bpy.ops.transform.rotate(value=1.7454620495764392, orient_axis='X')
bpy.ops.transform.rotate(value=1.5532028792434736, orient_axis='Y')
bpy.ops.transform.rotate(value=2.2881618341295638, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.417298402017132, 1.336995025644264, 0.5238338632515263))
ob.select_set(False)

# 24
ob = bpy.context.scene.objects[24]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.3453801707184061, 0, 1.318723819648386)
# rotation
bpy.ops.transform.rotate(value=0.7833951290945395, orient_axis='X')
bpy.ops.transform.rotate(value=0.8347610974858771, orient_axis='Y')
bpy.ops.transform.rotate(value=2.147561656538557, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.2215195250732629, 1.4481952321915077, 1.3864122902888392))
ob.select_set(False)

# 305
ob = bpy.context.scene.objects[305]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.4618311665095245, 0, -0.6542991948920176)
# rotation
bpy.ops.transform.rotate(value=1.102094868058537, orient_axis='X')
bpy.ops.transform.rotate(value=1.367497988185664, orient_axis='Y')
bpy.ops.transform.rotate(value=1.9072000920744232, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.9005146645657054, 1.1559235882415015, 0.28741870280312476))
ob.select_set(False)

# 110
ob = bpy.context.scene.objects[110]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.027390308674041, 0, 0.34484709806359426)
# rotation
bpy.ops.transform.rotate(value=0.5804918069709961, orient_axis='X')
bpy.ops.transform.rotate(value=2.0886061187178084, orient_axis='Y')
bpy.ops.transform.rotate(value=1.5920088008941928, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.45509855910553143, 1.261086370109737, 0.3717444708244051))
ob.select_set(False)

# 354
ob = bpy.context.scene.objects[354]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.727664257848378, 0, 0.7800565037734364)
# rotation
bpy.ops.transform.rotate(value=1.6593609795138584, orient_axis='X')
bpy.ops.transform.rotate(value=1.9766817380639063, orient_axis='Y')
bpy.ops.transform.rotate(value=1.9739922249089243, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.2820829910783027, 0.09026858539835736, 1.9202836695102259))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 18.811895815401453
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_75.JPEG"
bpy.ops.render.render(write_still=True)


