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


# 426
ob = bpy.context.scene.objects[426]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.0353503765578473, 0, -3.7238573083797046)
# rotation
bpy.ops.transform.rotate(value=2.6995996448393784, orient_axis='X')
bpy.ops.transform.rotate(value=0.020221789213994215, orient_axis='Y')
bpy.ops.transform.rotate(value=2.891402224054968, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.7935907234453212, 0.39183099069979344, 1.665974240398624))
ob.select_set(False)

# 261
ob = bpy.context.scene.objects[261]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.110444648045005, 0, 3.0295630280880905)
# rotation
bpy.ops.transform.rotate(value=1.3076040378580256, orient_axis='X')
bpy.ops.transform.rotate(value=0.5449508364488219, orient_axis='Y')
bpy.ops.transform.rotate(value=0.8667739929134054, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.27902162733059255, 1.1192674384649934, 0.9365385570044249))
ob.select_set(False)

# 18
ob = bpy.context.scene.objects[18]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.756878097885213, 0, 2.1141032966726048)
# rotation
bpy.ops.transform.rotate(value=3.04903504534856, orient_axis='X')
bpy.ops.transform.rotate(value=2.1947784889185686, orient_axis='Y')
bpy.ops.transform.rotate(value=1.2527805943162564, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.5151800419346135, 1.7080752555161862, 1.51217854200628))
ob.select_set(False)

# 78
ob = bpy.context.scene.objects[78]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.7468715204407794, 0, 2.7558201382481142)
# rotation
bpy.ops.transform.rotate(value=2.011743352854925, orient_axis='X')
bpy.ops.transform.rotate(value=0.9209284562786332, orient_axis='Y')
bpy.ops.transform.rotate(value=2.916893992010699, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.520405366629996, 1.2791432477704412, 0.48894162384881645))
ob.select_set(False)

# 17
ob = bpy.context.scene.objects[17]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.07049605039700868, 0, 2.7265089573308794)
# rotation
bpy.ops.transform.rotate(value=2.2131446531375834, orient_axis='X')
bpy.ops.transform.rotate(value=1.9068807599506288, orient_axis='Y')
bpy.ops.transform.rotate(value=0.808402725906467, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.0213928324938444, 1.1198963862341378, 1.9355351009639812))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 18.803683436765656
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_65.JPEG"
bpy.ops.render.render(write_still=True)


