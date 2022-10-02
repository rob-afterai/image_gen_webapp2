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


# 4
ob = bpy.context.scene.objects[4]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.30196349714797854, 0, -0.1998966360834915)
# rotation
bpy.ops.transform.rotate(value=1.7925623799619816, orient_axis='X')
bpy.ops.transform.rotate(value=2.0116474459936065, orient_axis='Y')
bpy.ops.transform.rotate(value=2.7639038866656316, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.5128160698341664, 0.06882577260554057, 1.0590710818818463))
ob.select_set(False)

# 300
ob = bpy.context.scene.objects[300]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.0983414682261694, 0, 4.250507421463848)
# rotation
bpy.ops.transform.rotate(value=0.10702532192233317, orient_axis='X')
bpy.ops.transform.rotate(value=2.9922478549455915, orient_axis='Y')
bpy.ops.transform.rotate(value=0.5766439042684592, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.7773513566765204, 0.18100727344984424, 0.6845941003870237))
ob.select_set(False)

# 66
ob = bpy.context.scene.objects[66]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.44689837999295, 0, 1.4479051605476263)
# rotation
bpy.ops.transform.rotate(value=1.9128772357041328, orient_axis='X')
bpy.ops.transform.rotate(value=2.279330059952163, orient_axis='Y')
bpy.ops.transform.rotate(value=2.1147937534299746, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.05884932053947467, 1.2172245906982833, 1.3512461405775609))
ob.select_set(False)

# 72
ob = bpy.context.scene.objects[72]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.8763069889153083, 0, -0.9906511597102332)
# rotation
bpy.ops.transform.rotate(value=0.6105103468047045, orient_axis='X')
bpy.ops.transform.rotate(value=2.08625919639342, orient_axis='Y')
bpy.ops.transform.rotate(value=1.9357569174651525, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.2690097294983445, 1.5998605035917104, 1.3655118711079965))
ob.select_set(False)

# 342
ob = bpy.context.scene.objects[342]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.632948862953084, 0, 3.8962045975027095)
# rotation
bpy.ops.transform.rotate(value=2.68997339902499, orient_axis='X')
bpy.ops.transform.rotate(value=1.2848871895083769, orient_axis='Y')
bpy.ops.transform.rotate(value=2.8801852187267074, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.7909589164004087, 0.3884940872300089, 0.8799164560109991))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 10.14531511217167
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_88.JPEG"
bpy.ops.render.render(write_still=True)


