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


# 575
ob = bpy.context.scene.objects[575]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.638556010550717, 0, -2.9592900004498226)
# rotation
bpy.ops.transform.rotate(value=0.23422680377742933, orient_axis='X')
bpy.ops.transform.rotate(value=1.1201709940841946, orient_axis='Y')
bpy.ops.transform.rotate(value=2.0350510028919837, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.7651282387226725, 1.3232220219344237, 1.2459022784069518))
ob.select_set(False)

# 366
ob = bpy.context.scene.objects[366]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.7961075890287947, 0, 1.291009662708504)
# rotation
bpy.ops.transform.rotate(value=2.608679987576781, orient_axis='X')
bpy.ops.transform.rotate(value=0.9396592821324705, orient_axis='Y')
bpy.ops.transform.rotate(value=1.7821422567333396, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.7296629136467476, 0.558963744563804, 0.9966536845390463))
ob.select_set(False)

# 6
ob = bpy.context.scene.objects[6]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.3372960406461667, 0, 0.9458771692392736)
# rotation
bpy.ops.transform.rotate(value=0.4739491570946709, orient_axis='X')
bpy.ops.transform.rotate(value=1.4739074353228703, orient_axis='Y')
bpy.ops.transform.rotate(value=2.9317825724613513, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.7027172009781566, 0.2432653912702003, 1.1082176762615978))
ob.select_set(False)

# 465
ob = bpy.context.scene.objects[465]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.8471990415557986, 0, -0.1540064066956477)
# rotation
bpy.ops.transform.rotate(value=0.9121272491120351, orient_axis='X')
bpy.ops.transform.rotate(value=3.0254950550060427, orient_axis='Y')
bpy.ops.transform.rotate(value=2.1568829196590147, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6045369745661056, 0.3078459344168962, 1.4563697087517615))
ob.select_set(False)

# 481
ob = bpy.context.scene.objects[481]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.2965204715614522, 0, -2.7523886783961866)
# rotation
bpy.ops.transform.rotate(value=3.117361453722013, orient_axis='X')
bpy.ops.transform.rotate(value=2.760959571755631, orient_axis='Y')
bpy.ops.transform.rotate(value=1.2020628354837466, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.20540970532278346, 0.24671256242192574, 0.9801788392093245))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 6.881552997502736
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_57.JPEG"
bpy.ops.render.render(write_still=True)


