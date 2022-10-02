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


# 59
ob = bpy.context.scene.objects[59]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.059745613402574, 0, 1.4441436432131338)
# rotation
bpy.ops.transform.rotate(value=1.728942320743082, orient_axis='X')
bpy.ops.transform.rotate(value=1.524803782661105, orient_axis='Y')
bpy.ops.transform.rotate(value=0.6190905266588015, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1453525262824058, 1.8096854039815324, 1.2840083566092473))
ob.select_set(False)

# 584
ob = bpy.context.scene.objects[584]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.2712646807626293, 0, -1.674862124187384)
# rotation
bpy.ops.transform.rotate(value=0.13714323285789098, orient_axis='X')
bpy.ops.transform.rotate(value=0.45177243418482144, orient_axis='Y')
bpy.ops.transform.rotate(value=2.323131382189263, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.3196932608701446, 1.6396123921318724, 1.3312209503329069))
ob.select_set(False)

# 459
ob = bpy.context.scene.objects[459]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.8561988908047535, 0, -3.12411198355192)
# rotation
bpy.ops.transform.rotate(value=2.2761227699923756, orient_axis='X')
bpy.ops.transform.rotate(value=0.05065567978622568, orient_axis='Y')
bpy.ops.transform.rotate(value=2.9088250892514496, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.2691940086149702, 1.777185599332743, 1.5719938682422334))
ob.select_set(False)

# 526
ob = bpy.context.scene.objects[526]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.19124268414543089, 0, -0.39492315920728505)
# rotation
bpy.ops.transform.rotate(value=0.32398207412189256, orient_axis='X')
bpy.ops.transform.rotate(value=1.4507609644416706, orient_axis='Y')
bpy.ops.transform.rotate(value=0.9478658120808365, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1298791818762526, 1.604015001468234, 0.03559495666793877))
ob.select_set(False)

# 218
ob = bpy.context.scene.objects[218]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.267551043866062, 0, -0.8470657411768845)
# rotation
bpy.ops.transform.rotate(value=0.6485289386862829, orient_axis='X')
bpy.ops.transform.rotate(value=0.09430567398572542, orient_axis='Y')
bpy.ops.transform.rotate(value=1.9762449981964296, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.21950885485449811, 1.8297001667799135, 1.2249568624791685))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 17.02483007134536
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_16.JPEG"
bpy.ops.render.render(write_still=True)


