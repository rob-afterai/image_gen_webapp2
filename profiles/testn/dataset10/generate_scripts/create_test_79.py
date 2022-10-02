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


# 100
ob = bpy.context.scene.objects[100]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.2064177344078342, 0, -2.66454418824214)
# rotation
bpy.ops.transform.rotate(value=0.9550711102029147, orient_axis='X')
bpy.ops.transform.rotate(value=2.581581842674972, orient_axis='Y')
bpy.ops.transform.rotate(value=1.3738299392626578, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.3448717107851522, 0.1936949535612822, 0.8515731066797143))
ob.select_set(False)

# 564
ob = bpy.context.scene.objects[564]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.5273811644744821, 0, -0.8015752232586113)
# rotation
bpy.ops.transform.rotate(value=1.3080357444949215, orient_axis='X')
bpy.ops.transform.rotate(value=2.3184777629393833, orient_axis='Y')
bpy.ops.transform.rotate(value=2.388041584722122, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.09756335859413556, 1.5756738043562981, 0.14937675289724806))
ob.select_set(False)

# 134
ob = bpy.context.scene.objects[134]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.703748376947567, 0, -0.9924510079628419)
# rotation
bpy.ops.transform.rotate(value=3.0442740955505405, orient_axis='X')
bpy.ops.transform.rotate(value=2.0747560214084784, orient_axis='Y')
bpy.ops.transform.rotate(value=1.783297246822275, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.643536497315678, 1.356860803856835, 0.894112314914884))
ob.select_set(False)

# 265
ob = bpy.context.scene.objects[265]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.61033634679033, 0, 2.5907554104427772)
# rotation
bpy.ops.transform.rotate(value=1.708891085198336, orient_axis='X')
bpy.ops.transform.rotate(value=2.6452780795629023, orient_axis='Y')
bpy.ops.transform.rotate(value=2.9228900660832413, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.35062687067102916, 0.556501368226441, 0.4512247835391383))
ob.select_set(False)

# 267
ob = bpy.context.scene.objects[267]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.040836742991725, 0, -3.4570244528375214)
# rotation
bpy.ops.transform.rotate(value=1.208200916767226, orient_axis='X')
bpy.ops.transform.rotate(value=3.0697733905761098, orient_axis='Y')
bpy.ops.transform.rotate(value=0.5029917917656607, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.2203225907102353, 0.46469352633869776, 1.129536415062122))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 12.29034137311283
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_79.JPEG"
bpy.ops.render.render(write_still=True)


