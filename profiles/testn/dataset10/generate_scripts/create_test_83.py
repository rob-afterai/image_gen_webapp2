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


# 502
ob = bpy.context.scene.objects[502]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.802604578774422, 0, -2.803401620387964)
# rotation
bpy.ops.transform.rotate(value=2.282988906951328, orient_axis='X')
bpy.ops.transform.rotate(value=2.202617063077737, orient_axis='Y')
bpy.ops.transform.rotate(value=2.3404734533539373, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.5169735019215287, 0.4773890249096213, 1.4898845698989078))
ob.select_set(False)

# 232
ob = bpy.context.scene.objects[232]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.6315026562217443, 0, -4.10493675582876)
# rotation
bpy.ops.transform.rotate(value=2.6522074263261746, orient_axis='X')
bpy.ops.transform.rotate(value=0.32971783497858104, orient_axis='Y')
bpy.ops.transform.rotate(value=0.4146702332236474, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.31139396874306247, 1.7542809687603125, 0.4553978797839173))
ob.select_set(False)

# 363
ob = bpy.context.scene.objects[363]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.8464044884699398, 0, 2.413167578496183)
# rotation
bpy.ops.transform.rotate(value=1.392081659891901, orient_axis='X')
bpy.ops.transform.rotate(value=1.5682001183728975, orient_axis='Y')
bpy.ops.transform.rotate(value=2.321735209945721, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.2743445133331042, 0.2278691035074516, 1.250626697557941))
ob.select_set(False)

# 377
ob = bpy.context.scene.objects[377]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.047437943402511, 0, -1.1429114519366874)
# rotation
bpy.ops.transform.rotate(value=0.9202008185981242, orient_axis='X')
bpy.ops.transform.rotate(value=0.6832674300538268, orient_axis='Y')
bpy.ops.transform.rotate(value=1.7434696210595273, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.9041213362589529, 0.8849003588985984, 1.1907884364384758))
ob.select_set(False)

# 474
ob = bpy.context.scene.objects[474]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.263061928348606, 0, -3.4117406360590192)
# rotation
bpy.ops.transform.rotate(value=1.661785649651193, orient_axis='X')
bpy.ops.transform.rotate(value=1.958779695798398, orient_axis='Y')
bpy.ops.transform.rotate(value=1.8354428897056023, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1224687476933364, 1.465584178880121, 1.9602189147874964))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 8.580748492168706
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_83.JPEG"
bpy.ops.render.render(write_still=True)


