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


# 423
ob = bpy.context.scene.objects[423]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.2845968595388157, 0, -2.9948553355125336)
# rotation
bpy.ops.transform.rotate(value=1.2409867858354704, orient_axis='X')
bpy.ops.transform.rotate(value=1.6345129586158738, orient_axis='Y')
bpy.ops.transform.rotate(value=0.28854027851676384, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.5708749115635974, 0.09398548045584931, 1.7653984848768474))
ob.select_set(False)

# 492
ob = bpy.context.scene.objects[492]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.8907938699533728, 0, 1.9901390665982914)
# rotation
bpy.ops.transform.rotate(value=1.2293939314534226, orient_axis='X')
bpy.ops.transform.rotate(value=0.2426765965581257, orient_axis='Y')
bpy.ops.transform.rotate(value=0.7585124447593009, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6666615731762857, 0.5816939532228391, 1.8377516817530641))
ob.select_set(False)

# 505
ob = bpy.context.scene.objects[505]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.994028305268964, 0, 0.6404514688452032)
# rotation
bpy.ops.transform.rotate(value=2.3168532290679247, orient_axis='X')
bpy.ops.transform.rotate(value=2.5938871731126154, orient_axis='Y')
bpy.ops.transform.rotate(value=2.4948043884726525, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8250833939179203, 0.7775737023802491, 0.12975543245629773))
ob.select_set(False)

# 302
ob = bpy.context.scene.objects[302]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.868291141194165, 0, 0.7575886937868681)
# rotation
bpy.ops.transform.rotate(value=1.854557578748349, orient_axis='X')
bpy.ops.transform.rotate(value=1.9002822275948932, orient_axis='Y')
bpy.ops.transform.rotate(value=2.4409550651040837, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6600259709934484, 0.964302224631006, 0.5439344540058646))
ob.select_set(False)

# 293
ob = bpy.context.scene.objects[293]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.5521848298076923, 0, 1.0586694298485249)
# rotation
bpy.ops.transform.rotate(value=0.759211940233293, orient_axis='X')
bpy.ops.transform.rotate(value=2.660701482485413, orient_axis='Y')
bpy.ops.transform.rotate(value=0.4852581733531757, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.091130067562375, 1.8337860368845205, 1.5610775763513614))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 11.422472450045847
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_46.JPEG"
bpy.ops.render.render(write_still=True)


