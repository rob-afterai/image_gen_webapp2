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


# 334
ob = bpy.context.scene.objects[334]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.896946240403571, 0, -4.4237865391151585)
# rotation
bpy.ops.transform.rotate(value=2.516533360901459, orient_axis='X')
bpy.ops.transform.rotate(value=1.2560899626981517, orient_axis='Y')
bpy.ops.transform.rotate(value=2.002393092298537, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.4185662482747656, 1.1763664936349068, 1.8562079421799678))
ob.select_set(False)

# 580
ob = bpy.context.scene.objects[580]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.0692706092134316, 0, 2.6550858786245604)
# rotation
bpy.ops.transform.rotate(value=1.074859624286433, orient_axis='X')
bpy.ops.transform.rotate(value=2.535654551247561, orient_axis='Y')
bpy.ops.transform.rotate(value=0.9143872003591843, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.7577993327190395, 0.3925627737252846, 1.1936892897889022))
ob.select_set(False)

# 421
ob = bpy.context.scene.objects[421]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.6981438374202718, 0, -3.781264485423666)
# rotation
bpy.ops.transform.rotate(value=2.8934421916430138, orient_axis='X')
bpy.ops.transform.rotate(value=2.2134191485881436, orient_axis='Y')
bpy.ops.transform.rotate(value=1.3957600113520472, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.2586759984629778, 1.820260353589968, 1.9974133523964448))
ob.select_set(False)

# 48
ob = bpy.context.scene.objects[48]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.1846338941874297, 0, -1.3012465727676408)
# rotation
bpy.ops.transform.rotate(value=0.7630195013480113, orient_axis='X')
bpy.ops.transform.rotate(value=0.8751422949648187, orient_axis='Y')
bpy.ops.transform.rotate(value=2.413060931286536, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8861463414620863, 1.4850537744540822, 0.23594391431618966))
ob.select_set(False)

# 86
ob = bpy.context.scene.objects[86]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.0157485409660598, 0, 3.691421534944631)
# rotation
bpy.ops.transform.rotate(value=2.04090669784657, orient_axis='X')
bpy.ops.transform.rotate(value=1.8194805461097572, orient_axis='Y')
bpy.ops.transform.rotate(value=0.09052800716656362, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8531423862007785, 1.4378627288515469, 0.13963507852546342))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 8.44565999508501
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_73.JPEG"
bpy.ops.render.render(write_still=True)


