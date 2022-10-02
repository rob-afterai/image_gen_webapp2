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


# 136
ob = bpy.context.scene.objects[136]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.7758218698267512, 0, 0.2604919307192155)
# rotation
bpy.ops.transform.rotate(value=1.2480875328717482, orient_axis='X')
bpy.ops.transform.rotate(value=1.2181644757799381, orient_axis='Y')
bpy.ops.transform.rotate(value=0.9343721275422752, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9705173355150216, 0.8112312846738279, 1.6125400349295127))
ob.select_set(False)

# 274
ob = bpy.context.scene.objects[274]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.9761538389209967, 0, -1.5613441281855565)
# rotation
bpy.ops.transform.rotate(value=2.1645714309161797, orient_axis='X')
bpy.ops.transform.rotate(value=2.744200043786078, orient_axis='Y')
bpy.ops.transform.rotate(value=1.5128732633376185, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.4060490648523793, 0.6628480255364704, 0.33538931366773395))
ob.select_set(False)

# 241
ob = bpy.context.scene.objects[241]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.2689218151890125, 0, 3.2388000941842474)
# rotation
bpy.ops.transform.rotate(value=1.1524753354244195, orient_axis='X')
bpy.ops.transform.rotate(value=0.5219133276798944, orient_axis='Y')
bpy.ops.transform.rotate(value=2.3460193656227375, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.5307323002160895, 0.10025822100206239, 1.6817893329654499))
ob.select_set(False)

# 381
ob = bpy.context.scene.objects[381]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.520026783160236, 0, 1.121539943262139)
# rotation
bpy.ops.transform.rotate(value=0.05540669890129027, orient_axis='X')
bpy.ops.transform.rotate(value=0.39063975740673434, orient_axis='Y')
bpy.ops.transform.rotate(value=1.6772550096811418, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.7611666125928584, 1.2294937891544255, 0.583034032919197))
ob.select_set(False)

# 511
ob = bpy.context.scene.objects[511]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.9891005401903783, 0, 2.4608023915726926)
# rotation
bpy.ops.transform.rotate(value=1.6113166395807708, orient_axis='X')
bpy.ops.transform.rotate(value=0.5136325794964189, orient_axis='Y')
bpy.ops.transform.rotate(value=0.7478292681928517, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.5205356590973806, 0.5527896131126033, 1.4947615409094985))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 3.1086350996333345
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_17.JPEG"
bpy.ops.render.render(write_still=True)


