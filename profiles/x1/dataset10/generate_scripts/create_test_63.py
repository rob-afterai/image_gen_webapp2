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


# 231
ob = bpy.context.scene.objects[231]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.2191350669875582, 0, -1.443310214150873)
# rotation
bpy.ops.transform.rotate(value=0.31928333437308365, orient_axis='X')
bpy.ops.transform.rotate(value=1.9641508023600958, orient_axis='Y')
bpy.ops.transform.rotate(value=0.9290146899423841, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8445208702088438, 1.2501302159900314, 0.548909773293252))
ob.select_set(False)

# 189
ob = bpy.context.scene.objects[189]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.092679041888939, 0, 0.04780587470491149)
# rotation
bpy.ops.transform.rotate(value=2.2804179227319326, orient_axis='X')
bpy.ops.transform.rotate(value=0.7598064996238031, orient_axis='Y')
bpy.ops.transform.rotate(value=2.1481569659351916, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.0688829715034325, 1.8311208885495702, 0.8406954028280527))
ob.select_set(False)

# 408
ob = bpy.context.scene.objects[408]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.0948924554227, 0, 1.1246166776684055)
# rotation
bpy.ops.transform.rotate(value=2.9385001031605458, orient_axis='X')
bpy.ops.transform.rotate(value=2.584916742243328, orient_axis='Y')
bpy.ops.transform.rotate(value=2.712316032186061, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9712362447844354, 0.023013933318905666, 1.1012391576605942))
ob.select_set(False)

# 415
ob = bpy.context.scene.objects[415]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.026489147531888, 0, -1.5109905275514692)
# rotation
bpy.ops.transform.rotate(value=1.0167306902485802, orient_axis='X')
bpy.ops.transform.rotate(value=2.4255909966187374, orient_axis='Y')
bpy.ops.transform.rotate(value=1.8771457372923503, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.692150938279929, 1.7281085637196285, 0.10596056820828093))
ob.select_set(False)

# 622
ob = bpy.context.scene.objects[622]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.9764924067188767, 0, -1.6033721009729458)
# rotation
bpy.ops.transform.rotate(value=0.9731300555991529, orient_axis='X')
bpy.ops.transform.rotate(value=0.33645447950802787, orient_axis='Y')
bpy.ops.transform.rotate(value=0.009317088491521306, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.0084241904947906, 1.963759537553873, 1.9758264339840994))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 16.536348649629403
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_63.JPEG"
bpy.ops.render.render(write_still=True)


