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
ob.location = (-3.951882066798907, 0, -4.011445326309222)
# rotation
bpy.ops.transform.rotate(value=2.3424185676198612, orient_axis='X')
bpy.ops.transform.rotate(value=1.0258364271061768, orient_axis='Y')
bpy.ops.transform.rotate(value=2.8922916648970634, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.4496730830775566, 0.9169748182383497, 1.2550570835049044))
ob.select_set(False)

# 242
ob = bpy.context.scene.objects[242]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.169107869168926, 0, -1.4557013072785177)
# rotation
bpy.ops.transform.rotate(value=1.1113960826549052, orient_axis='X')
bpy.ops.transform.rotate(value=0.8074217010444363, orient_axis='Y')
bpy.ops.transform.rotate(value=2.2541872901819175, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6049906545363659, 1.3696466178714686, 1.8358457479505363))
ob.select_set(False)

# 495
ob = bpy.context.scene.objects[495]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.2135745736705976, 0, -2.513804469951979)
# rotation
bpy.ops.transform.rotate(value=1.655242229192438, orient_axis='X')
bpy.ops.transform.rotate(value=2.962840040863038, orient_axis='Y')
bpy.ops.transform.rotate(value=2.963632195353929, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.34098785253688324, 0.8275900094041395, 1.168291910030984))
ob.select_set(False)

# 571
ob = bpy.context.scene.objects[571]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.918736971113315, 0, 1.3141306531872754)
# rotation
bpy.ops.transform.rotate(value=1.1140805624863896, orient_axis='X')
bpy.ops.transform.rotate(value=2.856702255296975, orient_axis='Y')
bpy.ops.transform.rotate(value=2.0318977989937688, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.0130273734766972, 0.5167661507030943, 1.7725963484979772))
ob.select_set(False)

# 274
ob = bpy.context.scene.objects[274]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.18185860440105017, 0, -0.5071649791875252)
# rotation
bpy.ops.transform.rotate(value=2.19286721831536, orient_axis='X')
bpy.ops.transform.rotate(value=2.827633632526386, orient_axis='Y')
bpy.ops.transform.rotate(value=1.9558944541350158, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.43443311770409765, 1.6008655971733279, 0.39399996636898393))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 10.333624005313318
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_67.JPEG"
bpy.ops.render.render(write_still=True)


