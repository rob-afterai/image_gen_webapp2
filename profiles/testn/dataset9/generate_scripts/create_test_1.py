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


# 32
ob = bpy.context.scene.objects[32]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.070813790038057, 0, 1.254841186120954)
# rotation
bpy.ops.transform.rotate(value=0.12105277551937335, orient_axis='X')
bpy.ops.transform.rotate(value=1.2828026608591103, orient_axis='Y')
bpy.ops.transform.rotate(value=0.8536888011660452, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.7765361529049761, 0.7036925116557653, 1.0963156568326593))
ob.select_set(False)

# 135
ob = bpy.context.scene.objects[135]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.898044212915235, 0, -0.02217088117257937)
# rotation
bpy.ops.transform.rotate(value=0.7646457749073182, orient_axis='X')
bpy.ops.transform.rotate(value=3.0720342552849296, orient_axis='Y')
bpy.ops.transform.rotate(value=1.93782423674365, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8272859451097823, 0.18067970853869908, 1.931838376049888))
ob.select_set(False)

# 573
ob = bpy.context.scene.objects[573]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.116908577756808, 0, 0.7268144844056099)
# rotation
bpy.ops.transform.rotate(value=0.703942391020605, orient_axis='X')
bpy.ops.transform.rotate(value=0.9665132098640611, orient_axis='Y')
bpy.ops.transform.rotate(value=1.552690548975425, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8559831317553486, 0.8902784503136456, 0.9523165244586913))
ob.select_set(False)

# 627
ob = bpy.context.scene.objects[627]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.767304006221889, 0, -3.8627196564683466)
# rotation
bpy.ops.transform.rotate(value=0.23485239658156773, orient_axis='X')
bpy.ops.transform.rotate(value=2.32884045782976, orient_axis='Y')
bpy.ops.transform.rotate(value=2.14851659057391, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.819538475847744, 0.6475066916415313, 0.14685330960466314))
ob.select_set(False)

# 608
ob = bpy.context.scene.objects[608]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.981660737843109, 0, 3.2375560067267886)
# rotation
bpy.ops.transform.rotate(value=1.4156537212153284, orient_axis='X')
bpy.ops.transform.rotate(value=1.1635478530424042, orient_axis='Y')
bpy.ops.transform.rotate(value=2.5092222590265227, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.6289562908956208, 0.29067232366656137, 0.5429822265198911))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 10.838131889488832
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_1.JPEG"
bpy.ops.render.render(write_still=True)


