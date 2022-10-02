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


# 230
ob = bpy.context.scene.objects[230]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.5584570066147077, 0, -0.9782092178625659)
# rotation
bpy.ops.transform.rotate(value=2.2109968804246694, orient_axis='X')
bpy.ops.transform.rotate(value=0.028335389824139297, orient_axis='Y')
bpy.ops.transform.rotate(value=0.9836590788273994, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.4966453030540303, 0.24609605328776651, 0.23365798897217172))
ob.select_set(False)

# 398
ob = bpy.context.scene.objects[398]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.1070779312621353, 0, -2.4651839839514245)
# rotation
bpy.ops.transform.rotate(value=1.9820435999565742, orient_axis='X')
bpy.ops.transform.rotate(value=1.4015173415730158, orient_axis='Y')
bpy.ops.transform.rotate(value=0.12984497188935126, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.918524284996066, 1.2141097784712767, 0.3368723231542541))
ob.select_set(False)

# 26
ob = bpy.context.scene.objects[26]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.6460753724778234, 0, 0.5702348611277568)
# rotation
bpy.ops.transform.rotate(value=2.056025279264704, orient_axis='X')
bpy.ops.transform.rotate(value=1.7979069282468916, orient_axis='Y')
bpy.ops.transform.rotate(value=2.8567364268689763, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.868682011186434, 1.033421504571479, 1.7533014092242853))
ob.select_set(False)

# 422
ob = bpy.context.scene.objects[422]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.1063323114962849, 0, 3.39262042481295)
# rotation
bpy.ops.transform.rotate(value=0.5253982313576339, orient_axis='X')
bpy.ops.transform.rotate(value=2.8020013140556683, orient_axis='Y')
bpy.ops.transform.rotate(value=2.4748964694020987, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.7548931983020946, 1.195938934221977, 1.937170512809458))
ob.select_set(False)

# 234
ob = bpy.context.scene.objects[234]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.398508100833073, 0, 3.6910669425187486)
# rotation
bpy.ops.transform.rotate(value=0.06309167917066838, orient_axis='X')
bpy.ops.transform.rotate(value=2.0054080187291605, orient_axis='Y')
bpy.ops.transform.rotate(value=2.4213384477322637, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.0943099326909855, 0.6356652491614714, 0.5648572547961961))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 19.528258731066032
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_53.JPEG"
bpy.ops.render.render(write_still=True)


