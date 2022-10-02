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


# 386
ob = bpy.context.scene.objects[386]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.3557671567073477, 0, -4.349449164759492)
# rotation
bpy.ops.transform.rotate(value=1.6832867581244124, orient_axis='X')
bpy.ops.transform.rotate(value=2.980526148458082, orient_axis='Y')
bpy.ops.transform.rotate(value=1.7778813437336123, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8633673108294617, 1.4070387374578464, 0.24191361308297643))
ob.select_set(False)

# 215
ob = bpy.context.scene.objects[215]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.930905341273707, 0, 2.040669531930254)
# rotation
bpy.ops.transform.rotate(value=1.5838561693242117, orient_axis='X')
bpy.ops.transform.rotate(value=1.6130837880299274, orient_axis='Y')
bpy.ops.transform.rotate(value=0.9432271847669391, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.7990970504271613, 0.43966139419855477, 1.1745451671751874))
ob.select_set(False)

# 336
ob = bpy.context.scene.objects[336]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.8969257975147706, 0, -3.7305692328024187)
# rotation
bpy.ops.transform.rotate(value=2.097071024496353, orient_axis='X')
bpy.ops.transform.rotate(value=1.8549169753761747, orient_axis='Y')
bpy.ops.transform.rotate(value=2.3470620327800886, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.42701403732887155, 1.4916259145435544, 1.471214978193794))
ob.select_set(False)

# 182
ob = bpy.context.scene.objects[182]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.8439746285788874, 0, -3.7881720686813134)
# rotation
bpy.ops.transform.rotate(value=2.566159397360283, orient_axis='X')
bpy.ops.transform.rotate(value=0.8895970204861181, orient_axis='Y')
bpy.ops.transform.rotate(value=1.3935022847887275, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.33278882349211547, 1.5893912170671, 1.4950270321450907))
ob.select_set(False)

# 32
ob = bpy.context.scene.objects[32]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.020223095916607647, 0, 2.5861110070136624)
# rotation
bpy.ops.transform.rotate(value=0.812898965339162, orient_axis='X')
bpy.ops.transform.rotate(value=1.7284540244725268, orient_axis='Y')
bpy.ops.transform.rotate(value=0.1925999182004863, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.420044629050994, 0.5099828853316688, 1.5261551631392876))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 6.905128148143211
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_55.JPEG"
bpy.ops.render.render(write_still=True)


