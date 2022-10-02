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


# 18
ob = bpy.context.scene.objects[18]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.568353596783165, 0, 0.6422274304922855)
# rotation
bpy.ops.transform.rotate(value=2.994056033094456, orient_axis='X')
bpy.ops.transform.rotate(value=2.660728526116997, orient_axis='Y')
bpy.ops.transform.rotate(value=2.867021801308041, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.03855042941204001, 0.7088954881475813, 1.793422108515152))
ob.select_set(False)

# 471
ob = bpy.context.scene.objects[471]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.3049090309040228, 0, 1.6908712593030666)
# rotation
bpy.ops.transform.rotate(value=1.8626287161568442, orient_axis='X')
bpy.ops.transform.rotate(value=0.20570527424299992, orient_axis='Y')
bpy.ops.transform.rotate(value=2.9375918658270628, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.8668328391497775, 0.2535028123404819, 0.25254498202490105))
ob.select_set(False)

# 344
ob = bpy.context.scene.objects[344]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.027844322230802, 0, -4.0911835027536645)
# rotation
bpy.ops.transform.rotate(value=1.5862667027743342, orient_axis='X')
bpy.ops.transform.rotate(value=0.3300522012965127, orient_axis='Y')
bpy.ops.transform.rotate(value=2.8050714054187313, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.3542134034216555, 1.1849275877259278, 1.886721933038046))
ob.select_set(False)

# 396
ob = bpy.context.scene.objects[396]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.669993953571855, 0, 2.809748005483364)
# rotation
bpy.ops.transform.rotate(value=0.35774362205650095, orient_axis='X')
bpy.ops.transform.rotate(value=0.9534001038960946, orient_axis='Y')
bpy.ops.transform.rotate(value=0.8768575353812093, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.206846157026535, 0.21912077641113714, 1.9348967724552593))
ob.select_set(False)

# 420
ob = bpy.context.scene.objects[420]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.590972292312226, 0, 2.376350017697395)
# rotation
bpy.ops.transform.rotate(value=1.8280473789151863, orient_axis='X')
bpy.ops.transform.rotate(value=0.7905010816418032, orient_axis='Y')
bpy.ops.transform.rotate(value=0.7775183047077009, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.23476141021769603, 1.6424192869028276, 1.0456331495880362))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 16.711916095198763
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_66.JPEG"
bpy.ops.render.render(write_still=True)


