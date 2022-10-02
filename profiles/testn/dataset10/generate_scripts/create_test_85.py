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


# 440
ob = bpy.context.scene.objects[440]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.478952623083039, 0, 2.4478915937460686)
# rotation
bpy.ops.transform.rotate(value=0.036451097587673134, orient_axis='X')
bpy.ops.transform.rotate(value=3.0868102179928165, orient_axis='Y')
bpy.ops.transform.rotate(value=0.5612193511718971, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.5513555579478056, 0.11367327599687349, 1.7030343262787213))
ob.select_set(False)

# 195
ob = bpy.context.scene.objects[195]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.7683148348078825, 0, 3.7047347009622182)
# rotation
bpy.ops.transform.rotate(value=0.17149248117252763, orient_axis='X')
bpy.ops.transform.rotate(value=1.4223986509003852, orient_axis='Y')
bpy.ops.transform.rotate(value=2.6673779004790186, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.9965165477305429, 0.6530586618698324, 1.2044859518285214))
ob.select_set(False)

# 602
ob = bpy.context.scene.objects[602]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.155787782858814, 0, -3.1239109616083915)
# rotation
bpy.ops.transform.rotate(value=0.7323993667145365, orient_axis='X')
bpy.ops.transform.rotate(value=1.2473209468653006, orient_axis='Y')
bpy.ops.transform.rotate(value=1.4241298119974357, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.6698178393993655, 1.4966278555429737, 0.7277886441306485))
ob.select_set(False)

# 489
ob = bpy.context.scene.objects[489]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.145918999463893, 0, -2.1276619957896505)
# rotation
bpy.ops.transform.rotate(value=2.945905372221519, orient_axis='X')
bpy.ops.transform.rotate(value=2.96046808685544, orient_axis='Y')
bpy.ops.transform.rotate(value=2.1888238668701883, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.19179225923766263, 0.2955777434289233, 0.031612813295566644))
ob.select_set(False)

# 273
ob = bpy.context.scene.objects[273]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.848222309315818, 0, -2.137523200066771)
# rotation
bpy.ops.transform.rotate(value=0.01868438899350349, orient_axis='X')
bpy.ops.transform.rotate(value=2.5804285115618124, orient_axis='Y')
bpy.ops.transform.rotate(value=1.405887479069217, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8787101087203495, 1.4153334390221368, 1.5266722131216))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 2.841259701003691
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_85.JPEG"
bpy.ops.render.render(write_still=True)


