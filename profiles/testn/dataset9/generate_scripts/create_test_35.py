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


# 322
ob = bpy.context.scene.objects[322]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.0845446436553843, 0, 1.0601167369071742)
# rotation
bpy.ops.transform.rotate(value=0.9979971244069121, orient_axis='X')
bpy.ops.transform.rotate(value=2.4496387296997706, orient_axis='Y')
bpy.ops.transform.rotate(value=1.326794316738415, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.862070101239425, 0.17852286542123696, 0.9696152102128308))
ob.select_set(False)

# 115
ob = bpy.context.scene.objects[115]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.171256425142796, 0, -1.8349524346663624)
# rotation
bpy.ops.transform.rotate(value=2.4009135124853964, orient_axis='X')
bpy.ops.transform.rotate(value=2.590389667017338, orient_axis='Y')
bpy.ops.transform.rotate(value=1.4357275060838444, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.688018070742767, 1.702519469605619, 0.18820875349687038))
ob.select_set(False)

# 455
ob = bpy.context.scene.objects[455]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.6826506389911873, 0, 2.5221815833090293)
# rotation
bpy.ops.transform.rotate(value=1.7949677188074022, orient_axis='X')
bpy.ops.transform.rotate(value=2.908337226549893, orient_axis='Y')
bpy.ops.transform.rotate(value=0.18728986599109296, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.4258046369864976, 1.6625561929675223, 0.09411013858177086))
ob.select_set(False)

# 512
ob = bpy.context.scene.objects[512]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.5574147401162715, 0, 4.454214228185609)
# rotation
bpy.ops.transform.rotate(value=2.3833752301380033, orient_axis='X')
bpy.ops.transform.rotate(value=1.626524348308534, orient_axis='Y')
bpy.ops.transform.rotate(value=0.35061541800588664, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.733006526252152, 1.0525835181383911, 0.9567682753243039))
ob.select_set(False)

# 312
ob = bpy.context.scene.objects[312]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.0581258265912554, 0, -4.483417479383717)
# rotation
bpy.ops.transform.rotate(value=3.104880306779283, orient_axis='X')
bpy.ops.transform.rotate(value=2.4862696229329333, orient_axis='Y')
bpy.ops.transform.rotate(value=0.6802545195248949, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9011887826303495, 1.0054216065025954, 0.46887852191983925))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 15.47556633038199
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_35.JPEG"
bpy.ops.render.render(write_still=True)


