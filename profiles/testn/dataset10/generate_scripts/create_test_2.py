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
ob.location = (0.053463723932228646, 0, -3.197515026296984)
# rotation
bpy.ops.transform.rotate(value=1.5579303731732959, orient_axis='X')
bpy.ops.transform.rotate(value=2.2970077494566628, orient_axis='Y')
bpy.ops.transform.rotate(value=0.6267085379518743, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.5830518719229318, 0.2919096013592939, 0.794977753962915))
ob.select_set(False)

# 194
ob = bpy.context.scene.objects[194]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.7701840183850397, 0, -2.666965973210536)
# rotation
bpy.ops.transform.rotate(value=0.262254436422259, orient_axis='X')
bpy.ops.transform.rotate(value=1.3220800888600694, orient_axis='Y')
bpy.ops.transform.rotate(value=2.8647581483896127, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.0936031070732661, 1.5203229566195489, 0.7411886202493729))
ob.select_set(False)

# 405
ob = bpy.context.scene.objects[405]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.7491647686013705, 0, -1.2924161391355007)
# rotation
bpy.ops.transform.rotate(value=1.2684911553231124, orient_axis='X')
bpy.ops.transform.rotate(value=0.4574014610269692, orient_axis='Y')
bpy.ops.transform.rotate(value=1.8248176960643332, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.2963424127741672, 1.9581002401455487, 1.9199218603899109))
ob.select_set(False)

# 202
ob = bpy.context.scene.objects[202]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.4028941416884324, 0, 1.896153597562435)
# rotation
bpy.ops.transform.rotate(value=0.7739533533617846, orient_axis='X')
bpy.ops.transform.rotate(value=0.40983352188810457, orient_axis='Y')
bpy.ops.transform.rotate(value=0.8778907412224252, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8685239254079458, 1.654341130684628, 0.9624932681466167))
ob.select_set(False)

# 593
ob = bpy.context.scene.objects[593]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.2250021183136335, 0, -2.3315804893935486)
# rotation
bpy.ops.transform.rotate(value=2.813133457522032, orient_axis='X')
bpy.ops.transform.rotate(value=2.5790626487203103, orient_axis='Y')
bpy.ops.transform.rotate(value=0.7539235144080445, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.421964535592569, 1.8526257170140281, 1.0298759080154982))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 3.7729634263075162
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_2.JPEG"
bpy.ops.render.render(write_still=True)


