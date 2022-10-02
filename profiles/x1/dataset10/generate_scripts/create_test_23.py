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


# 154
ob = bpy.context.scene.objects[154]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.346256443716808, 0, -4.048461142500997)
# rotation
bpy.ops.transform.rotate(value=2.553395176100497, orient_axis='X')
bpy.ops.transform.rotate(value=1.7743970309330717, orient_axis='Y')
bpy.ops.transform.rotate(value=3.134199672275788, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.2910368058187083, 1.270942031393459, 0.6111362041092019))
ob.select_set(False)

# 551
ob = bpy.context.scene.objects[551]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.7600167112289156, 0, 4.064555270057397)
# rotation
bpy.ops.transform.rotate(value=2.53090741583183, orient_axis='X')
bpy.ops.transform.rotate(value=1.622529257640805, orient_axis='Y')
bpy.ops.transform.rotate(value=1.6615253337134275, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.9228286035115225, 1.645877222503137, 0.3095775840046584))
ob.select_set(False)

# 435
ob = bpy.context.scene.objects[435]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.33050723525149817, 0, -0.45834308494481313)
# rotation
bpy.ops.transform.rotate(value=2.88132040222033, orient_axis='X')
bpy.ops.transform.rotate(value=1.1264172622062238, orient_axis='Y')
bpy.ops.transform.rotate(value=1.1235979656982633, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9561282753201854, 1.082934845055638, 0.023539845839275042))
ob.select_set(False)

# 521
ob = bpy.context.scene.objects[521]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.5816976201627426, 0, -4.197168026822571)
# rotation
bpy.ops.transform.rotate(value=0.624895649494857, orient_axis='X')
bpy.ops.transform.rotate(value=1.6387442453762209, orient_axis='Y')
bpy.ops.transform.rotate(value=1.055645576316657, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.4244053393020695, 1.5073731655966869, 0.22894252351725175))
ob.select_set(False)

# 50
ob = bpy.context.scene.objects[50]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.463435977041647, 0, -2.943667425708605)
# rotation
bpy.ops.transform.rotate(value=2.0875206573514067, orient_axis='X')
bpy.ops.transform.rotate(value=2.145601650715182, orient_axis='Y')
bpy.ops.transform.rotate(value=1.4526159647861183, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6455898424045305, 0.9496465949554429, 0.7765306763553792))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 3.4728167807911103
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_23.JPEG"
bpy.ops.render.render(write_still=True)


