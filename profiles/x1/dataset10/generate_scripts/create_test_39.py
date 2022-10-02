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


# 156
ob = bpy.context.scene.objects[156]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.271393516977163, 0, -1.389921094234018)
# rotation
bpy.ops.transform.rotate(value=2.8474799190099858, orient_axis='X')
bpy.ops.transform.rotate(value=0.3136093333899479, orient_axis='Y')
bpy.ops.transform.rotate(value=3.1346642214031215, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.13718547800828929, 1.1835951375568317, 1.7984454103458656))
ob.select_set(False)

# 484
ob = bpy.context.scene.objects[484]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.9162306302081982, 0, -3.79778936114388)
# rotation
bpy.ops.transform.rotate(value=0.5539484796249634, orient_axis='X')
bpy.ops.transform.rotate(value=1.9684916405027832, orient_axis='Y')
bpy.ops.transform.rotate(value=2.05759488820605, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.9671630879878346, 1.906248900584381, 1.3928172783353197))
ob.select_set(False)

# 350
ob = bpy.context.scene.objects[350]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.5463074715799348, 0, -0.4592876339532328)
# rotation
bpy.ops.transform.rotate(value=3.026120554737971, orient_axis='X')
bpy.ops.transform.rotate(value=2.505982447517143, orient_axis='Y')
bpy.ops.transform.rotate(value=2.070805663364991, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.41075186399420094, 0.8458919704328189, 1.625014691402247))
ob.select_set(False)

# 342
ob = bpy.context.scene.objects[342]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.896246685472609, 0, -1.1548814301202883)
# rotation
bpy.ops.transform.rotate(value=0.2505785854308053, orient_axis='X')
bpy.ops.transform.rotate(value=1.8861156487730628, orient_axis='Y')
bpy.ops.transform.rotate(value=0.1677066923361985, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.09356404729189549, 1.113547678696371, 0.7422582032914229))
ob.select_set(False)

# 206
ob = bpy.context.scene.objects[206]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.6311436894897628, 0, 3.440781547924522)
# rotation
bpy.ops.transform.rotate(value=3.0030851724948184, orient_axis='X')
bpy.ops.transform.rotate(value=0.3490232304871888, orient_axis='Y')
bpy.ops.transform.rotate(value=2.4794134235936314, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9853335540082473, 1.0772992442539724, 0.028450717817429805))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 10.758169612193623
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_39.JPEG"
bpy.ops.render.render(write_still=True)


