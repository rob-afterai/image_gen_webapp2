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


# 343
ob = bpy.context.scene.objects[343]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.83069517607127, 0, 3.344468312812701)
# rotation
bpy.ops.transform.rotate(value=0.8697600924926248, orient_axis='X')
bpy.ops.transform.rotate(value=0.2893670679858926, orient_axis='Y')
bpy.ops.transform.rotate(value=0.9028771718538875, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.3241006632863781, 1.370789499050885, 0.7509119667068926))
ob.select_set(False)

# 459
ob = bpy.context.scene.objects[459]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.467351391044902, 0, -2.810926558702011)
# rotation
bpy.ops.transform.rotate(value=1.5139487138327945, orient_axis='X')
bpy.ops.transform.rotate(value=0.777028988833968, orient_axis='Y')
bpy.ops.transform.rotate(value=0.4323524618315762, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.23473957740594864, 1.681324950302716, 0.0342912777323543))
ob.select_set(False)

# 272
ob = bpy.context.scene.objects[272]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.0798849318811827, 0, 0.14098911808036885)
# rotation
bpy.ops.transform.rotate(value=0.7507711810559221, orient_axis='X')
bpy.ops.transform.rotate(value=2.265974071069469, orient_axis='Y')
bpy.ops.transform.rotate(value=2.2227844794361657, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.06771349122719195, 1.3212606292135063, 0.6249966985670055))
ob.select_set(False)

# 216
ob = bpy.context.scene.objects[216]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.379352448028651, 0, -2.4359195168836223)
# rotation
bpy.ops.transform.rotate(value=1.452587380781707, orient_axis='X')
bpy.ops.transform.rotate(value=2.9943370371772513, orient_axis='Y')
bpy.ops.transform.rotate(value=2.450680637881277, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.739185665590242, 0.013233317195619376, 0.43272066175421786))
ob.select_set(False)

# 101
ob = bpy.context.scene.objects[101]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.117137465487934, 0, -2.801416396213749)
# rotation
bpy.ops.transform.rotate(value=2.3679930955207813, orient_axis='X')
bpy.ops.transform.rotate(value=2.385438192174822, orient_axis='Y')
bpy.ops.transform.rotate(value=2.9736477108660577, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.286975730501859, 1.5257451898164036, 1.0142469536319356))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 10.67580919799807
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_43.JPEG"
bpy.ops.render.render(write_still=True)


