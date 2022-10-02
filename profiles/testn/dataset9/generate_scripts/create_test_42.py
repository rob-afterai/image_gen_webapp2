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


# 383
ob = bpy.context.scene.objects[383]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.0681461670921806, 0, -1.2846903565476864)
# rotation
bpy.ops.transform.rotate(value=2.9131105215150312, orient_axis='X')
bpy.ops.transform.rotate(value=1.5117871299739059, orient_axis='Y')
bpy.ops.transform.rotate(value=1.740987548278493, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.4246257553270181, 1.3145933511676826, 1.4572863623303125))
ob.select_set(False)

# 148
ob = bpy.context.scene.objects[148]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.6312999843235971, 0, -3.883990231749092)
# rotation
bpy.ops.transform.rotate(value=0.7922485688765797, orient_axis='X')
bpy.ops.transform.rotate(value=2.4750925553796677, orient_axis='Y')
bpy.ops.transform.rotate(value=2.8785757362701427, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.2561831778012211, 0.1863697162296265, 0.05760071698383484))
ob.select_set(False)

# 192
ob = bpy.context.scene.objects[192]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.8683447200167436, 0, -0.7487977114239817)
# rotation
bpy.ops.transform.rotate(value=2.5033667366357424, orient_axis='X')
bpy.ops.transform.rotate(value=1.3576197643561136, orient_axis='Y')
bpy.ops.transform.rotate(value=1.5446835583598826, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.8389953701690704, 1.042733287803427, 1.0513960966547655))
ob.select_set(False)

# 232
ob = bpy.context.scene.objects[232]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.2004815671646165, 0, -0.44089993611584877)
# rotation
bpy.ops.transform.rotate(value=0.5667403549505448, orient_axis='X')
bpy.ops.transform.rotate(value=0.9877514239872768, orient_axis='Y')
bpy.ops.transform.rotate(value=2.6980719703700062, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9618433407831506, 1.5400116367432275, 1.4640457707401167))
ob.select_set(False)

# 507
ob = bpy.context.scene.objects[507]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.8541020504973567, 0, 3.436813613406298)
# rotation
bpy.ops.transform.rotate(value=1.6034430587285937, orient_axis='X')
bpy.ops.transform.rotate(value=0.02935710425285491, orient_axis='Y')
bpy.ops.transform.rotate(value=2.447239802340613, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.8168744712577041, 1.0145051240529885, 0.6080938498102455))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 11.78213029511858
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_42.JPEG"
bpy.ops.render.render(write_still=True)


