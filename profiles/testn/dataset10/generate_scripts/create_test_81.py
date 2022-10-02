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


# 277
ob = bpy.context.scene.objects[277]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.6863281601393547, 0, -4.137796186770776)
# rotation
bpy.ops.transform.rotate(value=0.9341096925839915, orient_axis='X')
bpy.ops.transform.rotate(value=0.5106993076533436, orient_axis='Y')
bpy.ops.transform.rotate(value=1.3859674343922226, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.5662869158328787, 1.512760517935964, 0.845154785673722))
ob.select_set(False)

# 102
ob = bpy.context.scene.objects[102]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.7884515350453967, 0, 1.0880832931552593)
# rotation
bpy.ops.transform.rotate(value=2.7351934194423824, orient_axis='X')
bpy.ops.transform.rotate(value=1.9399368217634276, orient_axis='Y')
bpy.ops.transform.rotate(value=2.8077138509733617, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.7823996318371003, 0.27262491168079683, 0.8964483823575564))
ob.select_set(False)

# 83
ob = bpy.context.scene.objects[83]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.265719682689122, 0, -2.884700304419188)
# rotation
bpy.ops.transform.rotate(value=1.8483007314162003, orient_axis='X')
bpy.ops.transform.rotate(value=1.5280653721455575, orient_axis='Y')
bpy.ops.transform.rotate(value=1.4157024742990532, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.8609758800620255, 0.7354019919649326, 1.2616928834778118))
ob.select_set(False)

# 184
ob = bpy.context.scene.objects[184]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.8637065471884604, 0, -1.0945430522056476)
# rotation
bpy.ops.transform.rotate(value=2.215582494983866, orient_axis='X')
bpy.ops.transform.rotate(value=2.676423600411992, orient_axis='Y')
bpy.ops.transform.rotate(value=0.8155364909186334, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6813942538032454, 0.9661119919905825, 0.7857506652022108))
ob.select_set(False)

# 179
ob = bpy.context.scene.objects[179]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.07383587273686665, 0, -2.1329516085845173)
# rotation
bpy.ops.transform.rotate(value=0.08824877347105858, orient_axis='X')
bpy.ops.transform.rotate(value=1.5660825716558775, orient_axis='Y')
bpy.ops.transform.rotate(value=2.0472990546788106, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.4778178803820645, 1.9866875058011313, 0.030678487095509466))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 0.7496606622492874
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_81.JPEG"
bpy.ops.render.render(write_still=True)


