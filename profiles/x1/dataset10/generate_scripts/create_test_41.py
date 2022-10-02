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


# 539
ob = bpy.context.scene.objects[539]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.641247349633179, 0, 3.9846225045553965)
# rotation
bpy.ops.transform.rotate(value=2.8981621888226803, orient_axis='X')
bpy.ops.transform.rotate(value=1.4195084176193014, orient_axis='Y')
bpy.ops.transform.rotate(value=2.1804097520440475, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.8248851732255253, 0.8912382791712454, 0.030004691731548627))
ob.select_set(False)

# 481
ob = bpy.context.scene.objects[481]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.8233764735438545, 0, -0.18019971577757854)
# rotation
bpy.ops.transform.rotate(value=0.0008603846093281154, orient_axis='X')
bpy.ops.transform.rotate(value=1.112239569507285, orient_axis='Y')
bpy.ops.transform.rotate(value=2.7056313390079954, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.4877374771179386, 1.0085685268917892, 1.9373681206833184))
ob.select_set(False)

# 498
ob = bpy.context.scene.objects[498]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.887087662319888, 0, 2.7475120677507716)
# rotation
bpy.ops.transform.rotate(value=1.397476942114198, orient_axis='X')
bpy.ops.transform.rotate(value=2.3925216260950233, orient_axis='Y')
bpy.ops.transform.rotate(value=2.7542821470521797, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.4033459555135368, 1.2941727656374096, 1.4970642834820642))
ob.select_set(False)

# 297
ob = bpy.context.scene.objects[297]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.3408202160555991, 0, 0.49255783667821795)
# rotation
bpy.ops.transform.rotate(value=2.656227308545671, orient_axis='X')
bpy.ops.transform.rotate(value=1.8236196456856464, orient_axis='Y')
bpy.ops.transform.rotate(value=2.7026235643916743, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.5758753994561914, 0.5721281737743298, 1.0751973581610652))
ob.select_set(False)

# 210
ob = bpy.context.scene.objects[210]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.7678042595501582, 0, 2.9557825879707034)
# rotation
bpy.ops.transform.rotate(value=0.8148455579988063, orient_axis='X')
bpy.ops.transform.rotate(value=0.08653538757463138, orient_axis='Y')
bpy.ops.transform.rotate(value=2.188992080985528, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.5258590553764675, 0.1834330238423305, 0.5901558434004792))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 6.192520044641309
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_41.JPEG"
bpy.ops.render.render(write_still=True)


