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


# 213
ob = bpy.context.scene.objects[213]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.5535205152690033, 0, -2.3483806087300856)
# rotation
bpy.ops.transform.rotate(value=0.30600714282627217, orient_axis='X')
bpy.ops.transform.rotate(value=2.952884959648707, orient_axis='Y')
bpy.ops.transform.rotate(value=2.0894764866444593, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.3657296416225222, 0.7323213701873583, 1.272781060066969))
ob.select_set(False)

# 438
ob = bpy.context.scene.objects[438]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.038125743989364, 0, -2.7287160174869993)
# rotation
bpy.ops.transform.rotate(value=2.128605721978841, orient_axis='X')
bpy.ops.transform.rotate(value=0.8256623737012466, orient_axis='Y')
bpy.ops.transform.rotate(value=1.7955653266698783, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.7557549666624619, 0.04839448611753805, 1.1575718882313406))
ob.select_set(False)

# 426
ob = bpy.context.scene.objects[426]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.586993363943443, 0, -0.6781036070326896)
# rotation
bpy.ops.transform.rotate(value=0.7132275564897967, orient_axis='X')
bpy.ops.transform.rotate(value=2.742779113734625, orient_axis='Y')
bpy.ops.transform.rotate(value=1.0933140287633303, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.4048616715186977, 1.06015023924258, 1.7899090106769493))
ob.select_set(False)

# 33
ob = bpy.context.scene.objects[33]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.2889964776535434, 0, 3.648072876004189)
# rotation
bpy.ops.transform.rotate(value=2.1548212169803045, orient_axis='X')
bpy.ops.transform.rotate(value=2.2125524275264774, orient_axis='Y')
bpy.ops.transform.rotate(value=2.7285717283946354, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.20120600513685938, 1.0415424983884238, 0.9644122966833197))
ob.select_set(False)

# 442
ob = bpy.context.scene.objects[442]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.8771223344835679, 0, -3.5751351434946246)
# rotation
bpy.ops.transform.rotate(value=2.527239282752907, orient_axis='X')
bpy.ops.transform.rotate(value=0.8393970224589095, orient_axis='Y')
bpy.ops.transform.rotate(value=2.8744224376430774, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.7030295224306389, 0.7080057691866892, 0.6612842058336228))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 15.323624095050787
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_94.JPEG"
bpy.ops.render.render(write_still=True)


