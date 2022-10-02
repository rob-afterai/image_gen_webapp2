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


# 308
ob = bpy.context.scene.objects[308]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.899981995773312, 0, -1.20233044807626)
# rotation
bpy.ops.transform.rotate(value=2.3758146811700436, orient_axis='X')
bpy.ops.transform.rotate(value=0.9699292284528772, orient_axis='Y')
bpy.ops.transform.rotate(value=1.7295803325603678, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.5746595632575326, 0.8220392566903274, 0.5607518590848455))
ob.select_set(False)

# 120
ob = bpy.context.scene.objects[120]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.7855883100243872, 0, -3.632929970001717)
# rotation
bpy.ops.transform.rotate(value=0.12687011600321443, orient_axis='X')
bpy.ops.transform.rotate(value=1.071568436964998, orient_axis='Y')
bpy.ops.transform.rotate(value=0.7444510024442613, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6062756268306113, 1.8124246874387402, 1.4964050717564725))
ob.select_set(False)

# 477
ob = bpy.context.scene.objects[477]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.263378602590894, 0, -3.8585034723729583)
# rotation
bpy.ops.transform.rotate(value=3.0121426281201096, orient_axis='X')
bpy.ops.transform.rotate(value=0.936432554349097, orient_axis='Y')
bpy.ops.transform.rotate(value=2.2614225398197845, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1853559117130787, 0.40775210831048625, 0.5438423777248111))
ob.select_set(False)

# 560
ob = bpy.context.scene.objects[560]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.774906630311812, 0, 3.5918310543543512)
# rotation
bpy.ops.transform.rotate(value=0.7927732687001259, orient_axis='X')
bpy.ops.transform.rotate(value=3.126481353070953, orient_axis='Y')
bpy.ops.transform.rotate(value=0.833776937954176, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.08254533597496283, 1.9641450595546597, 1.7681527309805558))
ob.select_set(False)

# 200
ob = bpy.context.scene.objects[200]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.4730445587273224, 0, -3.873422967255623)
# rotation
bpy.ops.transform.rotate(value=3.0590983619897165, orient_axis='X')
bpy.ops.transform.rotate(value=1.563585974377925, orient_axis='Y')
bpy.ops.transform.rotate(value=1.93634562686832, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9283031571931313, 1.8349513082384659, 0.7856967682754739))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 16.981270564432755
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_11.JPEG"
bpy.ops.render.render(write_still=True)


