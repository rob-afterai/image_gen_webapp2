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


# 45
ob = bpy.context.scene.objects[45]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.267610624034357, 0, -2.22101721841578)
# rotation
bpy.ops.transform.rotate(value=3.1267333933271217, orient_axis='X')
bpy.ops.transform.rotate(value=2.6047136462767986, orient_axis='Y')
bpy.ops.transform.rotate(value=0.7221710852823587, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.06607674558525867, 1.996753730267768, 1.6087798937878337))
ob.select_set(False)

# 294
ob = bpy.context.scene.objects[294]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.0984372170438852, 0, 2.976037052072919)
# rotation
bpy.ops.transform.rotate(value=0.8260925909658758, orient_axis='X')
bpy.ops.transform.rotate(value=2.2814524107954495, orient_axis='Y')
bpy.ops.transform.rotate(value=0.4873166351162474, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8064979594292585, 0.9895251348904441, 1.6388347645346153))
ob.select_set(False)

# 193
ob = bpy.context.scene.objects[193]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.1733333912042694, 0, 4.391576702283194)
# rotation
bpy.ops.transform.rotate(value=1.4699789241193224, orient_axis='X')
bpy.ops.transform.rotate(value=1.3409963192060357, orient_axis='Y')
bpy.ops.transform.rotate(value=2.881596955276418, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.009735466517599, 1.3258842308369085, 1.5938970405273325))
ob.select_set(False)

# 100
ob = bpy.context.scene.objects[100]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.522363834184755, 0, -3.4124974181140217)
# rotation
bpy.ops.transform.rotate(value=1.6728499320960233, orient_axis='X')
bpy.ops.transform.rotate(value=2.992406349584199, orient_axis='Y')
bpy.ops.transform.rotate(value=2.7234939423090547, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.6257432922997033, 0.2945768156685866, 1.952357235533253))
ob.select_set(False)

# 374
ob = bpy.context.scene.objects[374]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.946589878179645, 0, 4.034370468136029)
# rotation
bpy.ops.transform.rotate(value=0.5708082954174736, orient_axis='X')
bpy.ops.transform.rotate(value=2.874524952190227, orient_axis='Y')
bpy.ops.transform.rotate(value=1.462294807039216, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.329675920001957, 1.5626937699140595, 1.5547132854011279))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 13.396511191184995
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_24.JPEG"
bpy.ops.render.render(write_still=True)


