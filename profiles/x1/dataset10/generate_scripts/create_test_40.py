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


# 408
ob = bpy.context.scene.objects[408]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.9623418940512085, 0, 2.770687598131394)
# rotation
bpy.ops.transform.rotate(value=1.6217542805978926, orient_axis='X')
bpy.ops.transform.rotate(value=0.07585081885659048, orient_axis='Y')
bpy.ops.transform.rotate(value=0.42448063149444504, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.0322579077781018, 1.8081655050803092, 0.35947149831466274))
ob.select_set(False)

# 615
ob = bpy.context.scene.objects[615]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.236576825470451, 0, -1.8644277630897887)
# rotation
bpy.ops.transform.rotate(value=2.9685247733253632, orient_axis='X')
bpy.ops.transform.rotate(value=0.47424833058342947, orient_axis='Y')
bpy.ops.transform.rotate(value=1.0605849974879171, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.40391428973122157, 0.7068108862903368, 1.125482370930074))
ob.select_set(False)

# 139
ob = bpy.context.scene.objects[139]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.075244198937922, 0, 1.7244217426467339)
# rotation
bpy.ops.transform.rotate(value=0.1581698304293392, orient_axis='X')
bpy.ops.transform.rotate(value=2.8516755114960843, orient_axis='Y')
bpy.ops.transform.rotate(value=0.5107151561067572, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.8945985651387085, 1.7678767843965557, 0.49434761661889826))
ob.select_set(False)

# 10
ob = bpy.context.scene.objects[10]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.5567125881564836, 0, -1.6444475167488442)
# rotation
bpy.ops.transform.rotate(value=1.1085473603638156, orient_axis='X')
bpy.ops.transform.rotate(value=0.32011846637474994, orient_axis='Y')
bpy.ops.transform.rotate(value=1.9388920372104634, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.10019352963487149, 1.83424837970008, 0.39833706549868375))
ob.select_set(False)

# 133
ob = bpy.context.scene.objects[133]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.38529210956122206, 0, 2.320198110477583)
# rotation
bpy.ops.transform.rotate(value=2.528948184700156, orient_axis='X')
bpy.ops.transform.rotate(value=2.7681547541890215, orient_axis='Y')
bpy.ops.transform.rotate(value=2.8793402576066915, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.4818291136547417, 0.14082891778713136, 1.5860760884091862))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 6.650398150381247
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_40.JPEG"
bpy.ops.render.render(write_still=True)


