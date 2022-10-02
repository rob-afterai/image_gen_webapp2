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


# 604
ob = bpy.context.scene.objects[604]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.23318862389768924, 0, 2.2068679410787464)
# rotation
bpy.ops.transform.rotate(value=3.1161855677831203, orient_axis='X')
bpy.ops.transform.rotate(value=1.3642234942328477, orient_axis='Y')
bpy.ops.transform.rotate(value=0.2866504778564653, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.258283167492947, 0.2567194885350794, 1.1273513210706956))
ob.select_set(False)

# 222
ob = bpy.context.scene.objects[222]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.8555649353683226, 0, -2.2541609134109892)
# rotation
bpy.ops.transform.rotate(value=0.9235389340676935, orient_axis='X')
bpy.ops.transform.rotate(value=2.4707852569637216, orient_axis='Y')
bpy.ops.transform.rotate(value=1.3488953114800812, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.10288316458677138, 1.1206847172456664, 0.03869075764677454))
ob.select_set(False)

# 101
ob = bpy.context.scene.objects[101]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.7551717729098906, 0, -2.3769159679616507)
# rotation
bpy.ops.transform.rotate(value=2.640469910950329, orient_axis='X')
bpy.ops.transform.rotate(value=2.3990263734925463, orient_axis='Y')
bpy.ops.transform.rotate(value=2.2647635448605685, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6008725420026071, 1.5560616117722346, 0.3666267920193691))
ob.select_set(False)

# 209
ob = bpy.context.scene.objects[209]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.184717748773896, 0, -1.066509558683797)
# rotation
bpy.ops.transform.rotate(value=2.435320136682764, orient_axis='X')
bpy.ops.transform.rotate(value=2.4781384147828724, orient_axis='Y')
bpy.ops.transform.rotate(value=1.2422853778499874, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.22719969193943346, 0.6942836119047016, 0.18778584738463922))
ob.select_set(False)

# 508
ob = bpy.context.scene.objects[508]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.401236688287259, 0, 4.429212295782946)
# rotation
bpy.ops.transform.rotate(value=1.1108661531083124, orient_axis='X')
bpy.ops.transform.rotate(value=1.7925354675373821, orient_axis='Y')
bpy.ops.transform.rotate(value=0.6014251391502808, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.8595250014755578, 0.35263211779808357, 1.8969880576596985))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 19.793852782066228
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_52.JPEG"
bpy.ops.render.render(write_still=True)


