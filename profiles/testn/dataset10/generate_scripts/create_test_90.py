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


# 192
ob = bpy.context.scene.objects[192]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.5491376857156354, 0, -2.6267203164417277)
# rotation
bpy.ops.transform.rotate(value=0.555778546711765, orient_axis='X')
bpy.ops.transform.rotate(value=2.897825226023401, orient_axis='Y')
bpy.ops.transform.rotate(value=0.6422454522399449, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.020426288810142, 0.49718711140284366, 0.799726220667131))
ob.select_set(False)

# 368
ob = bpy.context.scene.objects[368]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.1524663725996422, 0, -2.641590900163674)
# rotation
bpy.ops.transform.rotate(value=0.3883780770424137, orient_axis='X')
bpy.ops.transform.rotate(value=2.6300803814175127, orient_axis='Y')
bpy.ops.transform.rotate(value=0.4849892775768177, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6208159934409319, 0.3456539202093909, 1.3070799376068971))
ob.select_set(False)

# 214
ob = bpy.context.scene.objects[214]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.0829792939240046, 0, -4.164178663133537)
# rotation
bpy.ops.transform.rotate(value=0.6142732703929032, orient_axis='X')
bpy.ops.transform.rotate(value=1.6102861987319865, orient_axis='Y')
bpy.ops.transform.rotate(value=1.086204203185195, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8746462350316002, 1.793369444321117, 0.6429898303621233))
ob.select_set(False)

# 559
ob = bpy.context.scene.objects[559]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.8162347869879834, 0, 0.7945978258968776)
# rotation
bpy.ops.transform.rotate(value=1.9444025100764457, orient_axis='X')
bpy.ops.transform.rotate(value=2.220682174391373, orient_axis='Y')
bpy.ops.transform.rotate(value=0.8565864867929959, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.3133646647136301, 1.6860621004261145, 0.5677993216753014))
ob.select_set(False)

# 291
ob = bpy.context.scene.objects[291]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.9724308592798314, 0, -2.0259658114835166)
# rotation
bpy.ops.transform.rotate(value=1.1506877813949299, orient_axis='X')
bpy.ops.transform.rotate(value=0.5256726505567304, orient_axis='Y')
bpy.ops.transform.rotate(value=2.1401132336335698, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.3570678055538785, 0.01330430488708867, 0.8502031967404029))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 2.813900209006057
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_90.JPEG"
bpy.ops.render.render(write_still=True)


