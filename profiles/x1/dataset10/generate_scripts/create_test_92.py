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


# 410
ob = bpy.context.scene.objects[410]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.3870796184022698, 0, 2.658630379241907)
# rotation
bpy.ops.transform.rotate(value=2.6717969826291244, orient_axis='X')
bpy.ops.transform.rotate(value=2.950149950571219, orient_axis='Y')
bpy.ops.transform.rotate(value=1.6822228416253593, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.7759170376229085, 0.49499423981594504, 0.004488472087488704))
ob.select_set(False)

# 167
ob = bpy.context.scene.objects[167]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.030815443249339047, 0, -0.2816326424062634)
# rotation
bpy.ops.transform.rotate(value=2.0344763877507157, orient_axis='X')
bpy.ops.transform.rotate(value=2.930191613809541, orient_axis='Y')
bpy.ops.transform.rotate(value=2.2173425868029177, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.4287741846022002, 0.8228084123243036, 1.9692630373241882))
ob.select_set(False)

# 316
ob = bpy.context.scene.objects[316]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.05104072157018358, 0, 1.546779602705107)
# rotation
bpy.ops.transform.rotate(value=0.01729326444982659, orient_axis='X')
bpy.ops.transform.rotate(value=2.4098667093452852, orient_axis='Y')
bpy.ops.transform.rotate(value=0.3101903561031381, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8908525956163689, 0.1659041999844586, 1.5339492028888022))
ob.select_set(False)

# 216
ob = bpy.context.scene.objects[216]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.52143333706397, 0, -0.31789535856030504)
# rotation
bpy.ops.transform.rotate(value=0.7979068708292086, orient_axis='X')
bpy.ops.transform.rotate(value=1.5261413088012534, orient_axis='Y')
bpy.ops.transform.rotate(value=2.809387577121918, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.03479576533678297, 0.05943870974114396, 1.7886803669502933))
ob.select_set(False)

# 419
ob = bpy.context.scene.objects[419]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.15242294236353882, 0, 2.344664396866862)
# rotation
bpy.ops.transform.rotate(value=2.9339996401109647, orient_axis='X')
bpy.ops.transform.rotate(value=1.279223477193883, orient_axis='Y')
bpy.ops.transform.rotate(value=1.2517686367449032, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.23608782146823737, 0.010319467260876403, 1.026876485236399))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 19.84785578210925
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_92.JPEG"
bpy.ops.render.render(write_still=True)


