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


# 603
ob = bpy.context.scene.objects[603]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.7142866182076504, 0, 0.09016656069131557)
# rotation
bpy.ops.transform.rotate(value=0.1644217003919652, orient_axis='X')
bpy.ops.transform.rotate(value=3.0168515762114305, orient_axis='Y')
bpy.ops.transform.rotate(value=2.826182808148755, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.145153478685283, 0.08915158975668103, 1.8800681807016915))
ob.select_set(False)

# 242
ob = bpy.context.scene.objects[242]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.7748799161036173, 0, 0.17800147704168268)
# rotation
bpy.ops.transform.rotate(value=0.9904664928428177, orient_axis='X')
bpy.ops.transform.rotate(value=1.2950265175784361, orient_axis='Y')
bpy.ops.transform.rotate(value=1.550634522386536, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.9682375121582845, 1.3390700723764806, 1.151432416272861))
ob.select_set(False)

# 540
ob = bpy.context.scene.objects[540]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.848700831574763, 0, -2.759072985968551)
# rotation
bpy.ops.transform.rotate(value=0.004741942529736465, orient_axis='X')
bpy.ops.transform.rotate(value=2.4227955506527583, orient_axis='Y')
bpy.ops.transform.rotate(value=1.6243876244511126, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1651768787663552, 1.8127423105229243, 0.8965344434273395))
ob.select_set(False)

# 465
ob = bpy.context.scene.objects[465]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.334281502792405, 0, -3.299983499508201)
# rotation
bpy.ops.transform.rotate(value=1.9004532244619525, orient_axis='X')
bpy.ops.transform.rotate(value=1.2669955084260554, orient_axis='Y')
bpy.ops.transform.rotate(value=0.22327757349653315, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.647614483928176, 1.4131474704983489, 1.9553066455765582))
ob.select_set(False)

# 400
ob = bpy.context.scene.objects[400]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.440309080590309, 0, -2.671719242620253)
# rotation
bpy.ops.transform.rotate(value=1.8239829607193705, orient_axis='X')
bpy.ops.transform.rotate(value=1.5316275636202716, orient_axis='Y')
bpy.ops.transform.rotate(value=1.92056025252814, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.3685046128061613, 0.7890397633704223, 0.245074026350381))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 6.863644629638655
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_3.JPEG"
bpy.ops.render.render(write_still=True)


