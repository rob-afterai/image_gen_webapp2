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


# 42
ob = bpy.context.scene.objects[42]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.5946265368021502, 0, -1.6441348140807786)
# rotation
bpy.ops.transform.rotate(value=1.4513691555034176, orient_axis='X')
bpy.ops.transform.rotate(value=2.100724840225865, orient_axis='Y')
bpy.ops.transform.rotate(value=0.022626235324523198, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.391531491595424, 0.5494152219906021, 1.6207706022064976))
ob.select_set(False)

# 173
ob = bpy.context.scene.objects[173]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.4329945974073395, 0, 0.0685219333381415)
# rotation
bpy.ops.transform.rotate(value=0.3014564924644193, orient_axis='X')
bpy.ops.transform.rotate(value=2.399164307383742, orient_axis='Y')
bpy.ops.transform.rotate(value=0.04924974604427257, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.0256279617677704, 0.7757697109243797, 1.1413449967531948))
ob.select_set(False)

# 475
ob = bpy.context.scene.objects[475]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.4542694818612096, 0, 3.384548561065639)
# rotation
bpy.ops.transform.rotate(value=0.23220801763410792, orient_axis='X')
bpy.ops.transform.rotate(value=1.265067467122529, orient_axis='Y')
bpy.ops.transform.rotate(value=0.6212885018373174, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.5700117998206007, 1.9522773687420634, 1.9819186555672434))
ob.select_set(False)

# 102
ob = bpy.context.scene.objects[102]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.6331455911511101, 0, -0.03827095596408103)
# rotation
bpy.ops.transform.rotate(value=0.4939443782715068, orient_axis='X')
bpy.ops.transform.rotate(value=2.8923691268921896, orient_axis='Y')
bpy.ops.transform.rotate(value=2.002656469760458, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.3563918897283114, 0.03622776128898164, 0.8311995194674122))
ob.select_set(False)

# 24
ob = bpy.context.scene.objects[24]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.7014208543347529, 0, -3.8704711784450723)
# rotation
bpy.ops.transform.rotate(value=1.537459707256264, orient_axis='X')
bpy.ops.transform.rotate(value=1.3803034686421658, orient_axis='Y')
bpy.ops.transform.rotate(value=1.457435075086963, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.22630819361636778, 1.720194485743626, 0.2974435786509193))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 12.195118151394958
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_87.JPEG"
bpy.ops.render.render(write_still=True)


