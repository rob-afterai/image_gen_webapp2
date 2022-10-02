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


# 46
ob = bpy.context.scene.objects[46]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.046820403651268, 0, 1.6098651956455408)
# rotation
bpy.ops.transform.rotate(value=0.2611164681910798, orient_axis='X')
bpy.ops.transform.rotate(value=1.3524917711778568, orient_axis='Y')
bpy.ops.transform.rotate(value=0.7679482265670334, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.8407208854735255, 0.7637957395135211, 0.7779287994124471))
ob.select_set(False)

# 333
ob = bpy.context.scene.objects[333]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.8736148101487391, 0, 3.494168675770001)
# rotation
bpy.ops.transform.rotate(value=0.33346025160244114, orient_axis='X')
bpy.ops.transform.rotate(value=1.0707614348882304, orient_axis='Y')
bpy.ops.transform.rotate(value=2.9417432021709264, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.6552631878991657, 1.7107186545928195, 1.6685884391177188))
ob.select_set(False)

# 324
ob = bpy.context.scene.objects[324]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.019654357656551547, 0, 2.663825798273333)
# rotation
bpy.ops.transform.rotate(value=2.8885501499411164, orient_axis='X')
bpy.ops.transform.rotate(value=1.0325488739281554, orient_axis='Y')
bpy.ops.transform.rotate(value=0.07142649748946943, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.9915244809283177, 1.4653757639872145, 0.5936533138512714))
ob.select_set(False)

# 1
ob = bpy.context.scene.objects[1]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.958227258297061, 0, 0.3355584166754628)
# rotation
bpy.ops.transform.rotate(value=2.106724584965998, orient_axis='X')
bpy.ops.transform.rotate(value=0.9879944413928727, orient_axis='Y')
bpy.ops.transform.rotate(value=1.104111955370416, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.2229932351420678, 1.9257881549100446, 1.3026406964877533))
ob.select_set(False)

# 585
ob = bpy.context.scene.objects[585]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.601513563156992, 0, -1.0051998169215381)
# rotation
bpy.ops.transform.rotate(value=2.101574524367462, orient_axis='X')
bpy.ops.transform.rotate(value=2.468301433890865, orient_axis='Y')
bpy.ops.transform.rotate(value=1.5823252510439316, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.9363812538739367, 0.05150261038407056, 0.9744320328960643))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 18.208222328273386
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_60.JPEG"
bpy.ops.render.render(write_still=True)


