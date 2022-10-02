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


# 537
ob = bpy.context.scene.objects[537]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.26784576216442346, 0, -3.566929102260163)
# rotation
bpy.ops.transform.rotate(value=1.5606317740306834, orient_axis='X')
bpy.ops.transform.rotate(value=2.2782256626538415, orient_axis='Y')
bpy.ops.transform.rotate(value=0.5152878079063848, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.5490080555121344, 0.5009595447866035, 1.8939666023825792))
ob.select_set(False)

# 1
ob = bpy.context.scene.objects[1]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.1857178263830614, 0, -0.04478841707019399)
# rotation
bpy.ops.transform.rotate(value=2.0604640322407652, orient_axis='X')
bpy.ops.transform.rotate(value=0.5874775841422768, orient_axis='Y')
bpy.ops.transform.rotate(value=3.0609460888949314, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6254282083948888, 1.4067232542282895, 1.4419359454678213))
ob.select_set(False)

# 223
ob = bpy.context.scene.objects[223]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.1318720790096322, 0, 0.18430360792503997)
# rotation
bpy.ops.transform.rotate(value=2.1232248799519127, orient_axis='X')
bpy.ops.transform.rotate(value=0.19980868650640296, orient_axis='Y')
bpy.ops.transform.rotate(value=2.6023907143684686, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.9675139608073853, 1.7531971619621258, 1.1025625003425876))
ob.select_set(False)

# 490
ob = bpy.context.scene.objects[490]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.615450113452309, 0, -0.4437189726087185)
# rotation
bpy.ops.transform.rotate(value=2.215816720071191, orient_axis='X')
bpy.ops.transform.rotate(value=2.2090667575527307, orient_axis='Y')
bpy.ops.transform.rotate(value=0.02293169142619606, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9144732058608493, 0.29645267960709587, 0.925832560913773))
ob.select_set(False)

# 45
ob = bpy.context.scene.objects[45]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.1199405501426076, 0, 0.5115319163340875)
# rotation
bpy.ops.transform.rotate(value=0.8397873684853019, orient_axis='X')
bpy.ops.transform.rotate(value=0.6374811925867101, orient_axis='Y')
bpy.ops.transform.rotate(value=2.8288581758211784, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.8560095141590232, 1.0128930630648645, 1.6646304414979856))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 10.65142555578754
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_97.JPEG"
bpy.ops.render.render(write_still=True)


