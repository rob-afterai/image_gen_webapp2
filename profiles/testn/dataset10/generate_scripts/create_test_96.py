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


# 165
ob = bpy.context.scene.objects[165]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.392729246014328, 0, -3.0607344793962086)
# rotation
bpy.ops.transform.rotate(value=1.25179619128074, orient_axis='X')
bpy.ops.transform.rotate(value=2.0191786248448804, orient_axis='Y')
bpy.ops.transform.rotate(value=1.5777470623434717, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.3841268657424346, 0.8234460261429133, 0.3158945458216378))
ob.select_set(False)

# 342
ob = bpy.context.scene.objects[342]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.4381773762167405, 0, 1.1546367320216753)
# rotation
bpy.ops.transform.rotate(value=2.5493591682985404, orient_axis='X')
bpy.ops.transform.rotate(value=2.538363555707606, orient_axis='Y')
bpy.ops.transform.rotate(value=0.870270221468573, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.37465271970154035, 1.670573740687728, 1.3181318516353073))
ob.select_set(False)

# 441
ob = bpy.context.scene.objects[441]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.06086278616584995, 0, 1.7360381672221026)
# rotation
bpy.ops.transform.rotate(value=1.0885393374196952, orient_axis='X')
bpy.ops.transform.rotate(value=3.0145700984320385, orient_axis='Y')
bpy.ops.transform.rotate(value=0.5418308624426383, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.48163975644113055, 1.1897403750133124, 0.4094668197710647))
ob.select_set(False)

# 418
ob = bpy.context.scene.objects[418]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.23868581652728, 0, 4.175206696565795)
# rotation
bpy.ops.transform.rotate(value=1.314856960708166, orient_axis='X')
bpy.ops.transform.rotate(value=0.47511227984870197, orient_axis='Y')
bpy.ops.transform.rotate(value=1.178204941679747, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.29225822507065446, 0.05293579587175423, 1.801518407948605))
ob.select_set(False)

# 472
ob = bpy.context.scene.objects[472]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.7193468712347464, 0, -0.6680713634337452)
# rotation
bpy.ops.transform.rotate(value=2.2206842190942107, orient_axis='X')
bpy.ops.transform.rotate(value=0.1709929967302924, orient_axis='Y')
bpy.ops.transform.rotate(value=2.705564996014851, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.4139464911239459, 1.588230968326191, 0.25382226601934255))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 11.799071847960143
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_96.JPEG"
bpy.ops.render.render(write_still=True)


