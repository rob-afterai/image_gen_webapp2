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


# 28
ob = bpy.context.scene.objects[28]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.03376490078574, 0, -0.32265949365437585)
# rotation
bpy.ops.transform.rotate(value=0.879677826701115, orient_axis='X')
bpy.ops.transform.rotate(value=2.860909096052237, orient_axis='Y')
bpy.ops.transform.rotate(value=0.4751678007289326, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.5332408854977579, 0.995880978646023, 0.14976892649278573))
ob.select_set(False)

# 131
ob = bpy.context.scene.objects[131]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.4571535623854475, 0, 0.38192841648450404)
# rotation
bpy.ops.transform.rotate(value=2.9694967982976337, orient_axis='X')
bpy.ops.transform.rotate(value=1.6968629142853136, orient_axis='Y')
bpy.ops.transform.rotate(value=1.2794061052794619, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9899215407156672, 1.0889747806996348, 0.06601484187285744))
ob.select_set(False)

# 293
ob = bpy.context.scene.objects[293]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.9084817902295441, 0, -1.9014074581847002)
# rotation
bpy.ops.transform.rotate(value=2.8110159413334377, orient_axis='X')
bpy.ops.transform.rotate(value=2.951874235115367, orient_axis='Y')
bpy.ops.transform.rotate(value=1.2654066358649088, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.13393662727656186, 1.3324130720651979, 1.0209240445917898))
ob.select_set(False)

# 492
ob = bpy.context.scene.objects[492]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.742125769574218, 0, 1.9380512088669342)
# rotation
bpy.ops.transform.rotate(value=2.7758465513977346, orient_axis='X')
bpy.ops.transform.rotate(value=1.374415918487797, orient_axis='Y')
bpy.ops.transform.rotate(value=1.7925044712684186, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.27547374993110973, 0.27817014766057047, 1.1259613718849988))
ob.select_set(False)

# 89
ob = bpy.context.scene.objects[89]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.9245787653403577, 0, 4.245582880934677)
# rotation
bpy.ops.transform.rotate(value=0.5924861253280471, orient_axis='X')
bpy.ops.transform.rotate(value=1.9093402268087794, orient_axis='Y')
bpy.ops.transform.rotate(value=1.7974899909787867, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.5144200963058645, 0.37686838808451917, 0.8878246222976838))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 4.480470934276541
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_28.JPEG"
bpy.ops.render.render(write_still=True)


