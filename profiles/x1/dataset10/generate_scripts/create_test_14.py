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


# 473
ob = bpy.context.scene.objects[473]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.8331127297945358, 0, 2.1263170639193705)
# rotation
bpy.ops.transform.rotate(value=1.6390532999415692, orient_axis='X')
bpy.ops.transform.rotate(value=2.90849847685365, orient_axis='Y')
bpy.ops.transform.rotate(value=2.948851279409672, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.5934425733289388, 0.28449516473337466, 0.20401437632871566))
ob.select_set(False)

# 550
ob = bpy.context.scene.objects[550]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.072477510301967, 0, -3.8137892646867946)
# rotation
bpy.ops.transform.rotate(value=0.47917738103222324, orient_axis='X')
bpy.ops.transform.rotate(value=2.967589493465812, orient_axis='Y')
bpy.ops.transform.rotate(value=2.1860157241222553, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6224297668219569, 0.609812822149393, 1.5286765946014171))
ob.select_set(False)

# 601
ob = bpy.context.scene.objects[601]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.9753146756551994, 0, 2.372208972366157)
# rotation
bpy.ops.transform.rotate(value=0.9924091654795157, orient_axis='X')
bpy.ops.transform.rotate(value=1.644345227200078, orient_axis='Y')
bpy.ops.transform.rotate(value=2.2338589860626534, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.4097824501226883, 1.0759374188238413, 1.1912790344024646))
ob.select_set(False)

# 257
ob = bpy.context.scene.objects[257]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.9381964968534366, 0, 2.13794631110867)
# rotation
bpy.ops.transform.rotate(value=2.8014165680357586, orient_axis='X')
bpy.ops.transform.rotate(value=2.277125813769207, orient_axis='Y')
bpy.ops.transform.rotate(value=0.3788947251630964, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.05022080220489222, 1.0973773505925186, 0.14525269669805385))
ob.select_set(False)

# 522
ob = bpy.context.scene.objects[522]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.8079151946209198, 0, -3.3681176213870714)
# rotation
bpy.ops.transform.rotate(value=3.121074404105699, orient_axis='X')
bpy.ops.transform.rotate(value=1.2694098646778635, orient_axis='Y')
bpy.ops.transform.rotate(value=0.31881009637718827, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.702844527827108, 1.414456189173677, 1.8811229506818954))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 6.880115215830052
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_14.JPEG"
bpy.ops.render.render(write_still=True)


