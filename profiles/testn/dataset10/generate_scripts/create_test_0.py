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


# 411
ob = bpy.context.scene.objects[411]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.290721802988389, 0, 4.104308447003245)
# rotation
bpy.ops.transform.rotate(value=0.747208929068539, orient_axis='X')
bpy.ops.transform.rotate(value=0.7411910017755444, orient_axis='Y')
bpy.ops.transform.rotate(value=1.9559113219536641, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.586680167523326, 0.6476655296663247, 0.4534117187620976))
ob.select_set(False)

# 384
ob = bpy.context.scene.objects[384]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.3329337796648071, 0, 0.6426233522092213)
# rotation
bpy.ops.transform.rotate(value=1.4204717980208306, orient_axis='X')
bpy.ops.transform.rotate(value=1.490151931082041, orient_axis='Y')
bpy.ops.transform.rotate(value=0.8132866639865871, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.21365707540331136, 1.930484283104246, 0.7230455498281503))
ob.select_set(False)

# 492
ob = bpy.context.scene.objects[492]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.19785518741243902, 0, -2.868616230001008)
# rotation
bpy.ops.transform.rotate(value=2.1261750961528487, orient_axis='X')
bpy.ops.transform.rotate(value=2.843708583187995, orient_axis='Y')
bpy.ops.transform.rotate(value=0.5179413666762416, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9164187596345457, 1.8497305032518905, 1.424685975653837))
ob.select_set(False)

# 596
ob = bpy.context.scene.objects[596]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.1073392784865264, 0, 2.2256213960095526)
# rotation
bpy.ops.transform.rotate(value=2.036281270733693, orient_axis='X')
bpy.ops.transform.rotate(value=0.35468551435315193, orient_axis='Y')
bpy.ops.transform.rotate(value=1.7210938289687352, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.0781631292116212, 0.0245564947959509, 0.15484356770660823))
ob.select_set(False)

# 218
ob = bpy.context.scene.objects[218]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.6329558082318583, 0, 0.26041844646371093)
# rotation
bpy.ops.transform.rotate(value=1.7229010617216018, orient_axis='X')
bpy.ops.transform.rotate(value=1.0321196344739276, orient_axis='Y')
bpy.ops.transform.rotate(value=2.1414943202462506, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.2789473894406407, 0.41970248907303453, 0.9172134187741228))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 17.5573580747802
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_0.JPEG"
bpy.ops.render.render(write_still=True)


