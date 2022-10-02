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


# 326
ob = bpy.context.scene.objects[326]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.139589764311019, 0, -2.726425333267756)
# rotation
bpy.ops.transform.rotate(value=1.6853463538622335, orient_axis='X')
bpy.ops.transform.rotate(value=1.9650401219815765, orient_axis='Y')
bpy.ops.transform.rotate(value=0.0023361522364022426, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1377899327476813, 1.9417006631419074, 1.9116762779396552))
ob.select_set(False)

# 224
ob = bpy.context.scene.objects[224]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.0405998857491596, 0, 3.5039492966989236)
# rotation
bpy.ops.transform.rotate(value=2.0640722078513436, orient_axis='X')
bpy.ops.transform.rotate(value=2.5970076407230276, orient_axis='Y')
bpy.ops.transform.rotate(value=2.856281696780463, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.4034589258280292, 0.18400436069094028, 1.9094873382959257))
ob.select_set(False)

# 352
ob = bpy.context.scene.objects[352]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.43620489439785093, 0, -2.818083035362618)
# rotation
bpy.ops.transform.rotate(value=2.362021854334332, orient_axis='X')
bpy.ops.transform.rotate(value=2.6236616098788947, orient_axis='Y')
bpy.ops.transform.rotate(value=0.5608306488862635, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.2870659481878366, 0.628152482463225, 0.2489563207866845))
ob.select_set(False)

# 111
ob = bpy.context.scene.objects[111]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.2436550952778918, 0, 2.3806784926188005)
# rotation
bpy.ops.transform.rotate(value=1.8071218114005196, orient_axis='X')
bpy.ops.transform.rotate(value=0.4653221845578098, orient_axis='Y')
bpy.ops.transform.rotate(value=1.550324369208643, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.0074454527320666, 1.7805303888921518, 1.441967394088032))
ob.select_set(False)

# 121
ob = bpy.context.scene.objects[121]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.142840361887394, 0, -3.63163404156403)
# rotation
bpy.ops.transform.rotate(value=1.8423602511312718, orient_axis='X')
bpy.ops.transform.rotate(value=3.011178543324423, orient_axis='Y')
bpy.ops.transform.rotate(value=0.6563968630433784, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.83490894777196, 1.788939042071141, 1.0838450748648898))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 8.6815357339317
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_62.JPEG"
bpy.ops.render.render(write_still=True)


