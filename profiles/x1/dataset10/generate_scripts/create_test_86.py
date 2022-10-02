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


# 7
ob = bpy.context.scene.objects[7]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.4004578005111661, 0, 3.272846433008718)
# rotation
bpy.ops.transform.rotate(value=1.8514444397117538, orient_axis='X')
bpy.ops.transform.rotate(value=3.0888584741994043, orient_axis='Y')
bpy.ops.transform.rotate(value=0.22146622524486786, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.8462072873956072, 1.133570313104874, 0.5736185652392234))
ob.select_set(False)

# 303
ob = bpy.context.scene.objects[303]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.6810307676184677, 0, -3.9092231738361165)
# rotation
bpy.ops.transform.rotate(value=0.024771023653112356, orient_axis='X')
bpy.ops.transform.rotate(value=2.6429188115235602, orient_axis='Y')
bpy.ops.transform.rotate(value=0.6831206452246915, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1850804402467863, 1.2204911264738085, 1.5889729699699016))
ob.select_set(False)

# 391
ob = bpy.context.scene.objects[391]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.940096050062527, 0, 0.8736771747724106)
# rotation
bpy.ops.transform.rotate(value=0.577441632178031, orient_axis='X')
bpy.ops.transform.rotate(value=0.08205824824525612, orient_axis='Y')
bpy.ops.transform.rotate(value=2.263348046727956, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.4579270516063694, 0.4147390209555897, 1.3805039876934049))
ob.select_set(False)

# 348
ob = bpy.context.scene.objects[348]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.7869013414867587, 0, -1.0732263065860517)
# rotation
bpy.ops.transform.rotate(value=0.851530125852485, orient_axis='X')
bpy.ops.transform.rotate(value=2.0723790164845743, orient_axis='Y')
bpy.ops.transform.rotate(value=2.5193122348409145, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1439943954052683, 0.6763898732466884, 0.3925766628569649))
ob.select_set(False)

# 477
ob = bpy.context.scene.objects[477]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.2008347552108765, 0, 0.8682030506164509)
# rotation
bpy.ops.transform.rotate(value=2.6882869749286624, orient_axis='X')
bpy.ops.transform.rotate(value=2.65768565440047, orient_axis='Y')
bpy.ops.transform.rotate(value=1.7900417457966056, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6714853105142911, 0.4433768019723625, 1.1466703180302298))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 2.875254121156554
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_86.JPEG"
bpy.ops.render.render(write_still=True)


