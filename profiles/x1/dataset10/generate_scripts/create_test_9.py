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


# 87
ob = bpy.context.scene.objects[87]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.716055121560238, 0, 2.4055052899991143)
# rotation
bpy.ops.transform.rotate(value=2.4505105389206068, orient_axis='X')
bpy.ops.transform.rotate(value=2.4619040009964297, orient_axis='Y')
bpy.ops.transform.rotate(value=2.1246278617415726, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.13785237800759043, 0.069029583713899, 1.7540221732367351))
ob.select_set(False)

# 595
ob = bpy.context.scene.objects[595]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.430462131630243, 0, -3.3816428509499565)
# rotation
bpy.ops.transform.rotate(value=0.9755538424837081, orient_axis='X')
bpy.ops.transform.rotate(value=0.36805230946514833, orient_axis='Y')
bpy.ops.transform.rotate(value=0.10687773127730972, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6632235371386275, 0.4674257690486818, 1.344568472077099))
ob.select_set(False)

# 414
ob = bpy.context.scene.objects[414]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.3341038486009063, 0, -4.295414018568337)
# rotation
bpy.ops.transform.rotate(value=0.09799528028621929, orient_axis='X')
bpy.ops.transform.rotate(value=2.894803588216132, orient_axis='Y')
bpy.ops.transform.rotate(value=1.505290819406153, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.11338599419789674, 1.0323887744966012, 1.2890335596110802))
ob.select_set(False)

# 392
ob = bpy.context.scene.objects[392]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.830201652533157, 0, 1.0976418903731124)
# rotation
bpy.ops.transform.rotate(value=1.3822264170710028, orient_axis='X')
bpy.ops.transform.rotate(value=2.5224497310504805, orient_axis='Y')
bpy.ops.transform.rotate(value=2.1002831784945397, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1347635773665576, 0.9856411839903694, 1.2305519121671122))
ob.select_set(False)

# 464
ob = bpy.context.scene.objects[464]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.1349318636173904, 0, 4.311782770957812)
# rotation
bpy.ops.transform.rotate(value=1.1639351513764982, orient_axis='X')
bpy.ops.transform.rotate(value=0.1584889841009144, orient_axis='Y')
bpy.ops.transform.rotate(value=0.37900495576477666, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8606712580548705, 0.07045568758906606, 0.6153730386778877))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 5.075917361246997
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_9.JPEG"
bpy.ops.render.render(write_still=True)


