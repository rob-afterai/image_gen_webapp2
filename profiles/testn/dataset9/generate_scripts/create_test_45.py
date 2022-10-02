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


# 336
ob = bpy.context.scene.objects[336]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.52819345231509, 0, 1.4980473657848812)
# rotation
bpy.ops.transform.rotate(value=1.6205806098489572, orient_axis='X')
bpy.ops.transform.rotate(value=1.9936553765681253, orient_axis='Y')
bpy.ops.transform.rotate(value=2.5616398825988638, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.13030781609894926, 1.0998304212842351, 0.015973539019745076))
ob.select_set(False)

# 131
ob = bpy.context.scene.objects[131]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.2889552470523027, 0, -3.8008369777915356)
# rotation
bpy.ops.transform.rotate(value=1.7384492606971527, orient_axis='X')
bpy.ops.transform.rotate(value=1.748826184091445, orient_axis='Y')
bpy.ops.transform.rotate(value=1.499516163379929, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8295415035273184, 0.11717276467765991, 0.5854199402854099))
ob.select_set(False)

# 578
ob = bpy.context.scene.objects[578]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.35491007240367, 0, -3.018209621296812)
# rotation
bpy.ops.transform.rotate(value=2.7754934838007936, orient_axis='X')
bpy.ops.transform.rotate(value=0.47015158729333106, orient_axis='Y')
bpy.ops.transform.rotate(value=1.1055641843808794, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.5709453160851945, 0.5615595330402199, 0.4572067553671397))
ob.select_set(False)

# 31
ob = bpy.context.scene.objects[31]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.313258500830716, 0, 2.3496236658218965)
# rotation
bpy.ops.transform.rotate(value=0.8801587194174559, orient_axis='X')
bpy.ops.transform.rotate(value=2.0599146367766195, orient_axis='Y')
bpy.ops.transform.rotate(value=1.1104241811806035, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.239975122348035, 1.0038057821386992, 0.9903573949116151))
ob.select_set(False)

# 550
ob = bpy.context.scene.objects[550]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.2235279185303325, 0, -1.0195549675273021)
# rotation
bpy.ops.transform.rotate(value=2.4805673300304627, orient_axis='X')
bpy.ops.transform.rotate(value=0.6605597730299257, orient_axis='Y')
bpy.ops.transform.rotate(value=1.595782284929306, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.3408612230994825, 0.1005365505479403, 1.614345915119134))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 18.0970054937171
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_45.JPEG"
bpy.ops.render.render(write_still=True)


