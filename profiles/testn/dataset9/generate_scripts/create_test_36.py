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


# 159
ob = bpy.context.scene.objects[159]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.6932012827616587, 0, 1.97838783509465)
# rotation
bpy.ops.transform.rotate(value=0.7605239620932678, orient_axis='X')
bpy.ops.transform.rotate(value=2.1581261100560676, orient_axis='Y')
bpy.ops.transform.rotate(value=0.7766596249682179, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6731242704676821, 0.18015336631235512, 0.8743280432234792))
ob.select_set(False)

# 204
ob = bpy.context.scene.objects[204]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.6096826489953298, 0, 0.447365267489201)
# rotation
bpy.ops.transform.rotate(value=1.1114220783752335, orient_axis='X')
bpy.ops.transform.rotate(value=0.8414751285206921, orient_axis='Y')
bpy.ops.transform.rotate(value=0.9307828376935013, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.4394937649304587, 1.0868165493448299, 0.9284620727913733))
ob.select_set(False)

# 153
ob = bpy.context.scene.objects[153]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.4318182887749829, 0, -3.35632336581034)
# rotation
bpy.ops.transform.rotate(value=1.2868760598046727, orient_axis='X')
bpy.ops.transform.rotate(value=2.124207412322793, orient_axis='Y')
bpy.ops.transform.rotate(value=0.12284777526820025, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.5163662984375597, 1.29167716758012, 0.6392945417179738))
ob.select_set(False)

# 419
ob = bpy.context.scene.objects[419]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.3312356519548847, 0, 1.0411972869868116)
# rotation
bpy.ops.transform.rotate(value=2.3080293791780444, orient_axis='X')
bpy.ops.transform.rotate(value=2.5621199100327376, orient_axis='Y')
bpy.ops.transform.rotate(value=0.1475422551716939, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9854064830155458, 0.28462481391340777, 0.44393064231875523))
ob.select_set(False)

# 604
ob = bpy.context.scene.objects[604]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.6231549837738415, 0, -4.006018608456441)
# rotation
bpy.ops.transform.rotate(value=0.3508623137275739, orient_axis='X')
bpy.ops.transform.rotate(value=1.7399505695638482, orient_axis='Y')
bpy.ops.transform.rotate(value=2.1592586382274614, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.164777587658207, 0.09898949858290185, 1.9949966773878338))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 18.28422973805115
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_36.JPEG"
bpy.ops.render.render(write_still=True)


