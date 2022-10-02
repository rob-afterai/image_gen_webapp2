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


# 373
ob = bpy.context.scene.objects[373]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.8563126286870038, 0, 0.060475296406732326)
# rotation
bpy.ops.transform.rotate(value=1.3944908449180482, orient_axis='X')
bpy.ops.transform.rotate(value=1.731401330793145, orient_axis='Y')
bpy.ops.transform.rotate(value=0.41771685530396613, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.3131761944950222, 1.2156781823308633, 0.5853315147023359))
ob.select_set(False)

# 75
ob = bpy.context.scene.objects[75]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.6867228986667047, 0, -0.2486558322810586)
# rotation
bpy.ops.transform.rotate(value=0.14522797510677524, orient_axis='X')
bpy.ops.transform.rotate(value=0.4753796074832408, orient_axis='Y')
bpy.ops.transform.rotate(value=1.431873451298766, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.3746888418446721, 1.79927448545315, 1.9547243707620567))
ob.select_set(False)

# 112
ob = bpy.context.scene.objects[112]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.205056644795552, 0, -3.907807565170668)
# rotation
bpy.ops.transform.rotate(value=0.34271436027442276, orient_axis='X')
bpy.ops.transform.rotate(value=0.8173443944166221, orient_axis='Y')
bpy.ops.transform.rotate(value=0.9529275886317168, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8228896678984263, 0.09585149300088669, 1.998562303857119))
ob.select_set(False)

# 598
ob = bpy.context.scene.objects[598]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.070272670977395, 0, 4.011415633678602)
# rotation
bpy.ops.transform.rotate(value=1.6783944664433492, orient_axis='X')
bpy.ops.transform.rotate(value=0.5315193551767975, orient_axis='Y')
bpy.ops.transform.rotate(value=1.7905703824739512, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.5584863083778164, 0.853344103230808, 0.542782246053823))
ob.select_set(False)

# 172
ob = bpy.context.scene.objects[172]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.44421560490515, 0, 1.9682354558896655)
# rotation
bpy.ops.transform.rotate(value=2.9889846294003912, orient_axis='X')
bpy.ops.transform.rotate(value=1.2427472763798173, orient_axis='Y')
bpy.ops.transform.rotate(value=1.095872363141468, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.28263865389735043, 0.8985055621753983, 1.5303074922396016))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 4.007878454099664
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_56.JPEG"
bpy.ops.render.render(write_still=True)


