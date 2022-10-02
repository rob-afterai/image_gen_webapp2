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


# 107
ob = bpy.context.scene.objects[107]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.4746585001570054, 0, 4.150270899501923)
# rotation
bpy.ops.transform.rotate(value=1.9493594092405915, orient_axis='X')
bpy.ops.transform.rotate(value=3.135170721108705, orient_axis='Y')
bpy.ops.transform.rotate(value=0.10515796292055153, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.5568300310679608, 1.682813776993675, 0.17493634317179363))
ob.select_set(False)

# 467
ob = bpy.context.scene.objects[467]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.396857787095064, 0, -1.069385993534707)
# rotation
bpy.ops.transform.rotate(value=3.05647810413296, orient_axis='X')
bpy.ops.transform.rotate(value=0.32822122358547257, orient_axis='Y')
bpy.ops.transform.rotate(value=0.5399208281769845, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6034435333592068, 0.9726118130811894, 0.9009890376379537))
ob.select_set(False)

# 618
ob = bpy.context.scene.objects[618]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.435993194486223, 0, -4.1170764851898145)
# rotation
bpy.ops.transform.rotate(value=1.7682370988534877, orient_axis='X')
bpy.ops.transform.rotate(value=0.6332900164854267, orient_axis='Y')
bpy.ops.transform.rotate(value=0.6710915246525122, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.338217975364655, 1.099011623813549, 0.8656201356718787))
ob.select_set(False)

# 622
ob = bpy.context.scene.objects[622]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.13772828764175848, 0, 2.7686212311067777)
# rotation
bpy.ops.transform.rotate(value=0.9619928198790766, orient_axis='X')
bpy.ops.transform.rotate(value=1.8421258093123174, orient_axis='Y')
bpy.ops.transform.rotate(value=1.5030024369010229, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.2790561017688213, 1.3508033038027027, 1.1429715899681097))
ob.select_set(False)

# 532
ob = bpy.context.scene.objects[532]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.687836330485327, 0, -1.7310844774335497)
# rotation
bpy.ops.transform.rotate(value=1.2584605434638376, orient_axis='X')
bpy.ops.transform.rotate(value=1.7620035458092116, orient_axis='Y')
bpy.ops.transform.rotate(value=2.8382120133120132, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.8229383122506324, 1.7477737842567822, 1.3427252694429508))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 18.997288583441453
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_19.JPEG"
bpy.ops.render.render(write_still=True)


