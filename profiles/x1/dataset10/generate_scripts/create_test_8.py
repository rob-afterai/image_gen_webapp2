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


# 448
ob = bpy.context.scene.objects[448]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.020864825558002, 0, 3.3618100836051568)
# rotation
bpy.ops.transform.rotate(value=2.3017482333566397, orient_axis='X')
bpy.ops.transform.rotate(value=1.8528837943708187, orient_axis='Y')
bpy.ops.transform.rotate(value=1.7293669818272048, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.20888539363581526, 1.7260137507149025, 1.2841364220156128))
ob.select_set(False)

# 335
ob = bpy.context.scene.objects[335]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.9694429209984827, 0, 4.059492896477671)
# rotation
bpy.ops.transform.rotate(value=2.6240963727101305, orient_axis='X')
bpy.ops.transform.rotate(value=0.7813421380251376, orient_axis='Y')
bpy.ops.transform.rotate(value=1.7421833326037002, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8495654798517347, 0.28910009564418804, 0.012652572614306079))
ob.select_set(False)

# 546
ob = bpy.context.scene.objects[546]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.6832681186581784, 0, -3.5141895211493224)
# rotation
bpy.ops.transform.rotate(value=0.44348438081620545, orient_axis='X')
bpy.ops.transform.rotate(value=1.2559894577096518, orient_axis='Y')
bpy.ops.transform.rotate(value=1.8284537533836964, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.24156502200672536, 0.37509871273325657, 0.7525614408321468))
ob.select_set(False)

# 104
ob = bpy.context.scene.objects[104]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.4359329608558093, 0, 0.5400542149344423)
# rotation
bpy.ops.transform.rotate(value=1.0997792534698596, orient_axis='X')
bpy.ops.transform.rotate(value=2.7386011782298643, orient_axis='Y')
bpy.ops.transform.rotate(value=1.286802403160431, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.779884939833155, 1.715892517717387, 1.7767999512605126))
ob.select_set(False)

# 146
ob = bpy.context.scene.objects[146]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.6220352664648368, 0, -2.575071515288633)
# rotation
bpy.ops.transform.rotate(value=0.49976311405659773, orient_axis='X')
bpy.ops.transform.rotate(value=2.040704402697084, orient_axis='Y')
bpy.ops.transform.rotate(value=0.5778908570960589, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.5295738427280676, 0.18608526818828208, 1.8396411125452086))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 6.130591369079259
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_8.JPEG"
bpy.ops.render.render(write_still=True)


