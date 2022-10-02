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


# 377
ob = bpy.context.scene.objects[377]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.37352647059051414, 0, -1.8223223533731203)
# rotation
bpy.ops.transform.rotate(value=2.665040984757576, orient_axis='X')
bpy.ops.transform.rotate(value=2.140455758048948, orient_axis='Y')
bpy.ops.transform.rotate(value=1.4522653280987419, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.34332785035689617, 0.5681908793839003, 0.08256096427793191))
ob.select_set(False)

# 321
ob = bpy.context.scene.objects[321]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.251565400645153, 0, -4.342263116388832)
# rotation
bpy.ops.transform.rotate(value=2.0632836291170245, orient_axis='X')
bpy.ops.transform.rotate(value=2.260431027704304, orient_axis='Y')
bpy.ops.transform.rotate(value=2.25802532550977, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.0005578277458946346, 0.5308897354487558, 0.12163184528797366))
ob.select_set(False)

# 432
ob = bpy.context.scene.objects[432]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.3908937112823598, 0, -0.9231371219106648)
# rotation
bpy.ops.transform.rotate(value=3.054418073474821, orient_axis='X')
bpy.ops.transform.rotate(value=2.00158101850178, orient_axis='Y')
bpy.ops.transform.rotate(value=2.752688210178736, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.7570941092422783, 0.39554173139244986, 1.6748093714613552))
ob.select_set(False)

# 618
ob = bpy.context.scene.objects[618]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.19214263653989327, 0, -3.3176205549220072)
# rotation
bpy.ops.transform.rotate(value=0.749970537931082, orient_axis='X')
bpy.ops.transform.rotate(value=2.541992567170769, orient_axis='Y')
bpy.ops.transform.rotate(value=0.39892503269034046, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.2882931182660913, 1.6013529101949597, 1.8098016173598328))
ob.select_set(False)

# 560
ob = bpy.context.scene.objects[560]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.596547350135032, 0, 0.7624306081873051)
# rotation
bpy.ops.transform.rotate(value=2.865246184835075, orient_axis='X')
bpy.ops.transform.rotate(value=2.868470687819873, orient_axis='Y')
bpy.ops.transform.rotate(value=1.1051408735546984, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.5983048328319485, 0.40396347987272563, 1.9278193257782008))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 12.978000973018329
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_68.JPEG"
bpy.ops.render.render(write_still=True)


