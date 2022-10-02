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


# 95
ob = bpy.context.scene.objects[95]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.020822317064118856, 0, 2.8971618146220566)
# rotation
bpy.ops.transform.rotate(value=0.7838762442743307, orient_axis='X')
bpy.ops.transform.rotate(value=0.2745816445703709, orient_axis='Y')
bpy.ops.transform.rotate(value=0.13668411776102043, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.8420330722402078, 1.3165250245299598, 1.5966430263942248))
ob.select_set(False)

# 450
ob = bpy.context.scene.objects[450]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.9332396063917683, 0, -3.176243370996956)
# rotation
bpy.ops.transform.rotate(value=0.6797509260604855, orient_axis='X')
bpy.ops.transform.rotate(value=0.9027050834518713, orient_axis='Y')
bpy.ops.transform.rotate(value=2.577760282440189, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.844778177844411, 1.5504325976850246, 0.5071773951927423))
ob.select_set(False)

# 7
ob = bpy.context.scene.objects[7]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.879365506600804, 0, -1.5966721982516594)
# rotation
bpy.ops.transform.rotate(value=1.9602831927183189, orient_axis='X')
bpy.ops.transform.rotate(value=0.08271821464291025, orient_axis='Y')
bpy.ops.transform.rotate(value=2.0549410315401224, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.7719110741040067, 0.6460360611003879, 1.123168728720994))
ob.select_set(False)

# 142
ob = bpy.context.scene.objects[142]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.7288578390642195, 0, -3.029915079482958)
# rotation
bpy.ops.transform.rotate(value=0.5139154263267156, orient_axis='X')
bpy.ops.transform.rotate(value=0.8004077801394677, orient_axis='Y')
bpy.ops.transform.rotate(value=1.8667640764596525, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.5438993224792952, 1.9353146894633928, 1.1668725408154197))
ob.select_set(False)

# 498
ob = bpy.context.scene.objects[498]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.707813001551341, 0, -1.2431968329549696)
# rotation
bpy.ops.transform.rotate(value=3.090293062175498, orient_axis='X')
bpy.ops.transform.rotate(value=1.2001824151654013, orient_axis='Y')
bpy.ops.transform.rotate(value=1.6669647871713658, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.4161145472045191, 0.8076324660933887, 0.24851609395903296))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 1.65516224444604
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_10.JPEG"
bpy.ops.render.render(write_still=True)


