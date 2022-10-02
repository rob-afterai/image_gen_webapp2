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


# 430
ob = bpy.context.scene.objects[430]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.4842265886244945, 0, 0.4675617222723423)
# rotation
bpy.ops.transform.rotate(value=1.6468455474195693, orient_axis='X')
bpy.ops.transform.rotate(value=0.9338269146436188, orient_axis='Y')
bpy.ops.transform.rotate(value=2.8377928460030524, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.2559223852725261, 1.1873437480903328, 1.6366509661270545))
ob.select_set(False)

# 614
ob = bpy.context.scene.objects[614]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.5208040260347175, 0, 3.1523389550247947)
# rotation
bpy.ops.transform.rotate(value=0.741672761259292, orient_axis='X')
bpy.ops.transform.rotate(value=3.139260255102601, orient_axis='Y')
bpy.ops.transform.rotate(value=2.111689376763932, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.10518556861364492, 0.7225444452410872, 0.3395199559215627))
ob.select_set(False)

# 91
ob = bpy.context.scene.objects[91]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.044057976423055, 0, 1.9602443759910937)
# rotation
bpy.ops.transform.rotate(value=1.0804085583329166, orient_axis='X')
bpy.ops.transform.rotate(value=0.5185342667089419, orient_axis='Y')
bpy.ops.transform.rotate(value=0.4566219708491061, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.5516903179131005, 1.0070217969216293, 0.09270274532941891))
ob.select_set(False)

# 199
ob = bpy.context.scene.objects[199]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.016500931418779, 0, -3.555801093004481)
# rotation
bpy.ops.transform.rotate(value=0.3919409192428926, orient_axis='X')
bpy.ops.transform.rotate(value=2.4632574918664396, orient_axis='Y')
bpy.ops.transform.rotate(value=0.23338325721867553, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1631852293564737, 0.3338798217519945, 1.731350328891846))
ob.select_set(False)

# 373
ob = bpy.context.scene.objects[373]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.278023903736656, 0, -1.0430071585860894)
# rotation
bpy.ops.transform.rotate(value=2.107905147577267, orient_axis='X')
bpy.ops.transform.rotate(value=0.3311146866117168, orient_axis='Y')
bpy.ops.transform.rotate(value=2.0258169677224442, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.4461370411127208, 1.9048166408031828, 0.6764195579890924))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 15.38714512048979
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_54.JPEG"
bpy.ops.render.render(write_still=True)


