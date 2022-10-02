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


# 447
ob = bpy.context.scene.objects[447]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.1593426927625563, 0, 0.3370517300207583)
# rotation
bpy.ops.transform.rotate(value=2.234256801725198, orient_axis='X')
bpy.ops.transform.rotate(value=0.5271236513028424, orient_axis='Y')
bpy.ops.transform.rotate(value=0.3776629756330578, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.14672975422574575, 1.9456395484906668, 0.05439907489595419))
ob.select_set(False)

# 512
ob = bpy.context.scene.objects[512]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.112548070094374, 0, 3.3505207803667654)
# rotation
bpy.ops.transform.rotate(value=1.9176884566638168, orient_axis='X')
bpy.ops.transform.rotate(value=1.2417252743333294, orient_axis='Y')
bpy.ops.transform.rotate(value=0.08518170563330771, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.6304375842438135, 1.9750343176151341, 0.1994510952620372))
ob.select_set(False)

# 480
ob = bpy.context.scene.objects[480]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.210591235264012, 0, 2.5656958764074584)
# rotation
bpy.ops.transform.rotate(value=1.3289996327973221, orient_axis='X')
bpy.ops.transform.rotate(value=0.12443705853542486, orient_axis='Y')
bpy.ops.transform.rotate(value=1.1528535850941324, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9159946837830117, 0.4026574897884776, 0.944345640322078))
ob.select_set(False)

# 6
ob = bpy.context.scene.objects[6]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.458410841048435, 0, -3.6792965834049274)
# rotation
bpy.ops.transform.rotate(value=1.9331252468653934, orient_axis='X')
bpy.ops.transform.rotate(value=2.89310343222502, orient_axis='Y')
bpy.ops.transform.rotate(value=1.007999749229075, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.39593177481538, 0.08726669800657971, 1.0293722890067032))
ob.select_set(False)

# 181
ob = bpy.context.scene.objects[181]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.084389823411569, 0, 3.890567592802949)
# rotation
bpy.ops.transform.rotate(value=2.3239925954943463, orient_axis='X')
bpy.ops.transform.rotate(value=2.2024706235205236, orient_axis='Y')
bpy.ops.transform.rotate(value=1.8009064185431654, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.9557412160269203, 1.0473495400098691, 1.6946712916028124))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 0.8833040307816953
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_78.JPEG"
bpy.ops.render.render(write_still=True)


