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


# 402
ob = bpy.context.scene.objects[402]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.1691061978313435, 0, -0.24835438912341434)
# rotation
bpy.ops.transform.rotate(value=0.19550354545884616, orient_axis='X')
bpy.ops.transform.rotate(value=0.5227786160891269, orient_axis='Y')
bpy.ops.transform.rotate(value=2.5667887698750858, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.3076176651682074, 1.6234600543948525, 1.2161515350859926))
ob.select_set(False)

# 99
ob = bpy.context.scene.objects[99]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.1355898466434873, 0, -4.088497560357066)
# rotation
bpy.ops.transform.rotate(value=2.2730747077233437, orient_axis='X')
bpy.ops.transform.rotate(value=1.7176166722170771, orient_axis='Y')
bpy.ops.transform.rotate(value=1.309995688123098, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.43978882450223855, 0.869379693144569, 1.564749159915007))
ob.select_set(False)

# 235
ob = bpy.context.scene.objects[235]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.9660065435237724, 0, 0.849517989454081)
# rotation
bpy.ops.transform.rotate(value=1.7887515161587337, orient_axis='X')
bpy.ops.transform.rotate(value=1.20937029202529, orient_axis='Y')
bpy.ops.transform.rotate(value=1.1387474836301776, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.3490671503569638, 0.7447598538715803, 1.0234090412901997))
ob.select_set(False)

# 259
ob = bpy.context.scene.objects[259]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.1875076104328164, 0, -2.1270145965961484)
# rotation
bpy.ops.transform.rotate(value=2.2801317310345115, orient_axis='X')
bpy.ops.transform.rotate(value=1.829704749826562, orient_axis='Y')
bpy.ops.transform.rotate(value=1.7806433756902686, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.9008791373542773, 0.8279767619566616, 1.4896520189784686))
ob.select_set(False)

# 288
ob = bpy.context.scene.objects[288]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.72582550724416, 0, 1.1319799338714258)
# rotation
bpy.ops.transform.rotate(value=0.9580096405748484, orient_axis='X')
bpy.ops.transform.rotate(value=0.5235151559771462, orient_axis='Y')
bpy.ops.transform.rotate(value=2.8951476915662897, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6332734914530436, 1.8502388559052225, 1.9083983347895848))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 12.348865020187807
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_29.JPEG"
bpy.ops.render.render(write_still=True)


