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


# 220
ob = bpy.context.scene.objects[220]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.0934962263184875, 0, 1.7453072782746721)
# rotation
bpy.ops.transform.rotate(value=1.9829544075318057, orient_axis='X')
bpy.ops.transform.rotate(value=2.0089553655656505, orient_axis='Y')
bpy.ops.transform.rotate(value=1.2817277421613347, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.432641693965069, 0.891493927492621, 0.7056555428633582))
ob.select_set(False)

# 454
ob = bpy.context.scene.objects[454]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.3687653981909707, 0, -1.6704521315854715)
# rotation
bpy.ops.transform.rotate(value=1.8850629419467613, orient_axis='X')
bpy.ops.transform.rotate(value=1.438033617739365, orient_axis='Y')
bpy.ops.transform.rotate(value=0.09995089095427569, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.2991132388875062, 1.5795699632627798, 0.07153633387882019))
ob.select_set(False)

# 543
ob = bpy.context.scene.objects[543]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.533439239020562, 0, -3.442065435812404)
# rotation
bpy.ops.transform.rotate(value=2.264628453864052, orient_axis='X')
bpy.ops.transform.rotate(value=2.635746429345331, orient_axis='Y')
bpy.ops.transform.rotate(value=1.676878896050733, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.409511217303138, 1.5794743865605554, 1.3465182654945314))
ob.select_set(False)

# 297
ob = bpy.context.scene.objects[297]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.6124480133300843, 0, 3.183046002921775)
# rotation
bpy.ops.transform.rotate(value=2.5149345951985307, orient_axis='X')
bpy.ops.transform.rotate(value=2.026282598980689, orient_axis='Y')
bpy.ops.transform.rotate(value=0.6857284336314714, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.2515382895680052, 0.4885622109899568, 0.2734586602077955))
ob.select_set(False)

# 267
ob = bpy.context.scene.objects[267]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.397854890970149, 0, 2.3204803071252638)
# rotation
bpy.ops.transform.rotate(value=1.5641055519043439, orient_axis='X')
bpy.ops.transform.rotate(value=0.7728488723365072, orient_axis='Y')
bpy.ops.transform.rotate(value=1.4906853626005054, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1294839124228695, 0.556112327001016, 0.47164272990844114))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 19.428574075890364
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_91.JPEG"
bpy.ops.render.render(write_still=True)


