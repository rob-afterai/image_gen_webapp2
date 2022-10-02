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


# 31
ob = bpy.context.scene.objects[31]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.896079671165366, 0, 2.374934170170559)
# rotation
bpy.ops.transform.rotate(value=0.2849806928111154, orient_axis='X')
bpy.ops.transform.rotate(value=1.2462863679309006, orient_axis='Y')
bpy.ops.transform.rotate(value=1.3640687889811691, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.017295674664536964, 1.0119533338996811, 0.5581247735858532))
ob.select_set(False)

# 200
ob = bpy.context.scene.objects[200]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.5133433335631725, 0, -1.037658757986808)
# rotation
bpy.ops.transform.rotate(value=1.7737733623544725, orient_axis='X')
bpy.ops.transform.rotate(value=1.2442655172444863, orient_axis='Y')
bpy.ops.transform.rotate(value=0.47773932812793657, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.0345669199310354, 0.08809446739335125, 1.7175113142684266))
ob.select_set(False)

# 188
ob = bpy.context.scene.objects[188]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.142928731290008, 0, -1.7967386493170139)
# rotation
bpy.ops.transform.rotate(value=2.192421435129138, orient_axis='X')
bpy.ops.transform.rotate(value=2.347169092144324, orient_axis='Y')
bpy.ops.transform.rotate(value=0.7707697812884309, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.5576328651293903, 0.6642043345855193, 0.12756696110907173))
ob.select_set(False)

# 194
ob = bpy.context.scene.objects[194]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.8004057043107293, 0, -0.1435414978361509)
# rotation
bpy.ops.transform.rotate(value=1.2530425600331712, orient_axis='X')
bpy.ops.transform.rotate(value=2.887601459713459, orient_axis='Y')
bpy.ops.transform.rotate(value=1.660451056789338, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.4099914753709286, 1.709019318547759, 0.5620385873774303))
ob.select_set(False)

# 238
ob = bpy.context.scene.objects[238]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.642292225526175, 0, -1.423321572073987)
# rotation
bpy.ops.transform.rotate(value=1.0890091454736712, orient_axis='X')
bpy.ops.transform.rotate(value=2.113991922168064, orient_axis='Y')
bpy.ops.transform.rotate(value=1.9547314096560227, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.5917287375200833, 0.23743526922964264, 1.7278367223799749))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 1.1732044871195324
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_5.JPEG"
bpy.ops.render.render(write_still=True)


