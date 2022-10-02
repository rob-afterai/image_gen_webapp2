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


# 432
ob = bpy.context.scene.objects[432]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.3496223094035256, 0, 1.035130077543979)
# rotation
bpy.ops.transform.rotate(value=2.1496251884169717, orient_axis='X')
bpy.ops.transform.rotate(value=3.014996309181998, orient_axis='Y')
bpy.ops.transform.rotate(value=1.3168645269939367, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6104181389047594, 1.8320962083901746, 1.605102643534864))
ob.select_set(False)

# 136
ob = bpy.context.scene.objects[136]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.175857672672287, 0, -4.347939609627702)
# rotation
bpy.ops.transform.rotate(value=2.111074027150612, orient_axis='X')
bpy.ops.transform.rotate(value=1.702007320544414, orient_axis='Y')
bpy.ops.transform.rotate(value=0.1920286881365663, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.801916017129832, 1.9757357062051415, 0.4691650823576905))
ob.select_set(False)

# 248
ob = bpy.context.scene.objects[248]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.16375163262809522, 0, -3.618394944217864)
# rotation
bpy.ops.transform.rotate(value=1.2975218075109254, orient_axis='X')
bpy.ops.transform.rotate(value=0.09034751725964073, orient_axis='Y')
bpy.ops.transform.rotate(value=2.274009955216954, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.2479865099653904, 0.0006566060771164839, 1.1228840628470598))
ob.select_set(False)

# 267
ob = bpy.context.scene.objects[267]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.489749124274313, 0, -4.08565180438711)
# rotation
bpy.ops.transform.rotate(value=0.16696783101785503, orient_axis='X')
bpy.ops.transform.rotate(value=2.4920946728512843, orient_axis='Y')
bpy.ops.transform.rotate(value=2.8663260416351997, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.0150749493591538, 0.3251152801359283, 1.1261023213222103))
ob.select_set(False)

# 114
ob = bpy.context.scene.objects[114]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.4499560693593203, 0, -3.88046621697743)
# rotation
bpy.ops.transform.rotate(value=2.212588963220642, orient_axis='X')
bpy.ops.transform.rotate(value=2.9455969091260625, orient_axis='Y')
bpy.ops.transform.rotate(value=0.5776426083042159, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.36813335252064916, 0.28606955508487997, 1.467422390073909))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 14.396767262358598
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_95.JPEG"
bpy.ops.render.render(write_still=True)


