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


# 84
ob = bpy.context.scene.objects[84]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.321345144820127, 0, 1.5454550411785162)
# rotation
bpy.ops.transform.rotate(value=2.276131396333381, orient_axis='X')
bpy.ops.transform.rotate(value=0.10306310488372263, orient_axis='Y')
bpy.ops.transform.rotate(value=1.8237357892544344, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.9836200188467132, 1.111986473575082, 1.8698649981233055))
ob.select_set(False)

# 288
ob = bpy.context.scene.objects[288]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.144825143796896, 0, 0.38426727413879114)
# rotation
bpy.ops.transform.rotate(value=2.0674937779032097, orient_axis='X')
bpy.ops.transform.rotate(value=2.4115493848509315, orient_axis='Y')
bpy.ops.transform.rotate(value=1.4995982974372188, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.3521352862343172, 1.724173185705367, 0.1461282364212877))
ob.select_set(False)

# 259
ob = bpy.context.scene.objects[259]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.22892857574276526, 0, -2.6477069855382624)
# rotation
bpy.ops.transform.rotate(value=1.143209683573657, orient_axis='X')
bpy.ops.transform.rotate(value=1.87676476627007, orient_axis='Y')
bpy.ops.transform.rotate(value=1.2520282240642224, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9304079943521355, 0.06331494808469418, 0.26775589894115615))
ob.select_set(False)

# 437
ob = bpy.context.scene.objects[437]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.856681241296921, 0, -0.6314396839575909)
# rotation
bpy.ops.transform.rotate(value=2.0024787232551877, orient_axis='X')
bpy.ops.transform.rotate(value=0.5883759436397062, orient_axis='Y')
bpy.ops.transform.rotate(value=0.1992262027656132, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1021116236959467, 1.6408840904312374, 1.3007744274329893))
ob.select_set(False)

# 391
ob = bpy.context.scene.objects[391]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.5814290975744552, 0, -2.7321185238162187)
# rotation
bpy.ops.transform.rotate(value=1.2872879671410744, orient_axis='X')
bpy.ops.transform.rotate(value=0.08283797584751522, orient_axis='Y')
bpy.ops.transform.rotate(value=1.4512985283330524, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.397274369806291, 0.3558744624664816, 0.8910597787878938))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 12.587404115349406
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_7.JPEG"
bpy.ops.render.render(write_still=True)


