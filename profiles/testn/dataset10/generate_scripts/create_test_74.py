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


# 90
ob = bpy.context.scene.objects[90]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.6516226330527126, 0, -3.137617688746634)
# rotation
bpy.ops.transform.rotate(value=2.3162973834201144, orient_axis='X')
bpy.ops.transform.rotate(value=2.082283989023826, orient_axis='Y')
bpy.ops.transform.rotate(value=0.6527241545848602, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1932401797114853, 1.5414455399359261, 0.1190262722703368))
ob.select_set(False)

# 470
ob = bpy.context.scene.objects[470]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.077161316824126, 0, 2.6986738677226336)
# rotation
bpy.ops.transform.rotate(value=1.8333834523751464, orient_axis='X')
bpy.ops.transform.rotate(value=2.560318368626467, orient_axis='Y')
bpy.ops.transform.rotate(value=2.4520005379072596, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.07358961090355742, 1.330257675128857, 0.6211960061953923))
ob.select_set(False)

# 468
ob = bpy.context.scene.objects[468]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.4992632603548799, 0, 0.6357843194161346)
# rotation
bpy.ops.transform.rotate(value=0.4743845192104629, orient_axis='X')
bpy.ops.transform.rotate(value=1.6337143531233793, orient_axis='Y')
bpy.ops.transform.rotate(value=2.0286863357950833, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.4524851962929068, 0.7044853201905443, 0.21404633709752718))
ob.select_set(False)

# 115
ob = bpy.context.scene.objects[115]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.378911846632086, 0, -3.6458891356935026)
# rotation
bpy.ops.transform.rotate(value=0.07317257052297604, orient_axis='X')
bpy.ops.transform.rotate(value=2.119913844536465, orient_axis='Y')
bpy.ops.transform.rotate(value=2.7695456664602416, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.139575555404023, 1.1500174532354785, 1.4986719042587648))
ob.select_set(False)

# 518
ob = bpy.context.scene.objects[518]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.2506713978501853, 0, 0.6703626489121577)
# rotation
bpy.ops.transform.rotate(value=1.089617907746155, orient_axis='X')
bpy.ops.transform.rotate(value=2.97481814245256, orient_axis='Y')
bpy.ops.transform.rotate(value=0.1480822803452711, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.7947327058946341, 1.3515515471349355, 1.2777529228755837))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 6.245533538356605
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_74.JPEG"
bpy.ops.render.render(write_still=True)


