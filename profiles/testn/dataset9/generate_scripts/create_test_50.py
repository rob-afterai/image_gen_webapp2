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


# 485
ob = bpy.context.scene.objects[485]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.7778858780490356, 0, 2.047420263318134)
# rotation
bpy.ops.transform.rotate(value=0.3540780904824069, orient_axis='X')
bpy.ops.transform.rotate(value=1.6470729346290938, orient_axis='Y')
bpy.ops.transform.rotate(value=1.4141649314956914, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1097099392607477, 0.4053552564512304, 1.7800356767066496))
ob.select_set(False)

# 556
ob = bpy.context.scene.objects[556]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.0500693718668597, 0, -3.2475890440826283)
# rotation
bpy.ops.transform.rotate(value=1.6276832476550007, orient_axis='X')
bpy.ops.transform.rotate(value=0.3027147742045732, orient_axis='Y')
bpy.ops.transform.rotate(value=1.3350571577314254, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6307063487756552, 1.4536052208691883, 1.4758500585540355))
ob.select_set(False)

# 459
ob = bpy.context.scene.objects[459]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.707533866138407, 0, 0.2984213765471342)
# rotation
bpy.ops.transform.rotate(value=2.6134295364126667, orient_axis='X')
bpy.ops.transform.rotate(value=1.9457615098744774, orient_axis='Y')
bpy.ops.transform.rotate(value=2.626099757322713, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.063251499666426, 0.7658438489084176, 0.9401814368621413))
ob.select_set(False)

# 592
ob = bpy.context.scene.objects[592]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.519769532563684, 0, -3.4279210353243323)
# rotation
bpy.ops.transform.rotate(value=0.3401661767879006, orient_axis='X')
bpy.ops.transform.rotate(value=1.1150386491477766, orient_axis='Y')
bpy.ops.transform.rotate(value=2.261088489373476, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.5714900700006358, 1.328213202646911, 1.6555219595715858))
ob.select_set(False)

# 595
ob = bpy.context.scene.objects[595]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.8049947530540682, 0, -3.8053331204642022)
# rotation
bpy.ops.transform.rotate(value=2.5553797781663765, orient_axis='X')
bpy.ops.transform.rotate(value=2.75536077572106, orient_axis='Y')
bpy.ops.transform.rotate(value=0.7982591058810382, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.1793045841086447, 1.9073992768903256, 0.7637595214192201))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 11.166332711363925
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_50.JPEG"
bpy.ops.render.render(write_still=True)


