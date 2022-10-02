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


# 157
ob = bpy.context.scene.objects[157]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.6638209469151466, 0, -1.7201899124129016)
# rotation
bpy.ops.transform.rotate(value=1.7298860637269045, orient_axis='X')
bpy.ops.transform.rotate(value=2.950517322224475, orient_axis='Y')
bpy.ops.transform.rotate(value=0.3277527433260283, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.21656977347217476, 1.5771220528799221, 1.9100117322441692))
ob.select_set(False)

# 502
ob = bpy.context.scene.objects[502]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.04795108187236785, 0, 1.337490961053307)
# rotation
bpy.ops.transform.rotate(value=0.48978539145341804, orient_axis='X')
bpy.ops.transform.rotate(value=0.1507817498017217, orient_axis='Y')
bpy.ops.transform.rotate(value=2.781425350197941, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.07723685821688209, 0.6147861194353892, 1.9010329052853108))
ob.select_set(False)

# 395
ob = bpy.context.scene.objects[395]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.0223530922989692, 0, -0.5157930728149402)
# rotation
bpy.ops.transform.rotate(value=2.184107410793604, orient_axis='X')
bpy.ops.transform.rotate(value=0.3128323501825914, orient_axis='Y')
bpy.ops.transform.rotate(value=0.4401936070638292, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.6527917046875211, 1.6285436798594106, 0.5940734212933936))
ob.select_set(False)

# 33
ob = bpy.context.scene.objects[33]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.546615638877601, 0, -1.8497854815687411)
# rotation
bpy.ops.transform.rotate(value=0.7903223787781315, orient_axis='X')
bpy.ops.transform.rotate(value=1.7771392564629835, orient_axis='Y')
bpy.ops.transform.rotate(value=0.3191119744697913, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.4289883988602419, 0.7026807870297538, 1.8351807974369907))
ob.select_set(False)

# 348
ob = bpy.context.scene.objects[348]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.453531631310899, 0, -1.5909544355332246)
# rotation
bpy.ops.transform.rotate(value=2.16615460765843, orient_axis='X')
bpy.ops.transform.rotate(value=2.648504149409037, orient_axis='Y')
bpy.ops.transform.rotate(value=1.6923083469272686, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.4571655197403144, 1.0146484833225657, 1.013563848930678))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 1.734099340566433
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_64.JPEG"
bpy.ops.render.render(write_still=True)


