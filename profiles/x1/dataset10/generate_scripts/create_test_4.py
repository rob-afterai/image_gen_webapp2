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


# 178
ob = bpy.context.scene.objects[178]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.16389062879587435, 0, -4.016662469423047)
# rotation
bpy.ops.transform.rotate(value=1.700060959985561, orient_axis='X')
bpy.ops.transform.rotate(value=0.29935158750209334, orient_axis='Y')
bpy.ops.transform.rotate(value=0.05283051843935828, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.35742870915550085, 0.4576578113541656, 1.4911192523670056))
ob.select_set(False)

# 529
ob = bpy.context.scene.objects[529]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.20025249810451, 0, 2.5866122253603674)
# rotation
bpy.ops.transform.rotate(value=2.4540930498087525, orient_axis='X')
bpy.ops.transform.rotate(value=1.1069123489230073, orient_axis='Y')
bpy.ops.transform.rotate(value=1.0177579135417205, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.6082060933811901, 0.8879187887108542, 0.059398339026476954))
ob.select_set(False)

# 228
ob = bpy.context.scene.objects[228]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.210561565690984, 0, 4.037596427009007)
# rotation
bpy.ops.transform.rotate(value=2.830714423130792, orient_axis='X')
bpy.ops.transform.rotate(value=0.4529129915775873, orient_axis='Y')
bpy.ops.transform.rotate(value=1.8241575842661295, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.9041317306981129, 0.21588871018951172, 0.5518358201950795))
ob.select_set(False)

# 246
ob = bpy.context.scene.objects[246]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.6020149187338166, 0, -1.4193031270160765)
# rotation
bpy.ops.transform.rotate(value=1.102885716870338, orient_axis='X')
bpy.ops.transform.rotate(value=2.4795446966579515, orient_axis='Y')
bpy.ops.transform.rotate(value=1.5179795011510135, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.14917452884557836, 1.5183503855399527, 0.7466723744955233))
ob.select_set(False)

# 306
ob = bpy.context.scene.objects[306]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.5561348136992601, 0, 2.834023828978429)
# rotation
bpy.ops.transform.rotate(value=1.869928823280518, orient_axis='X')
bpy.ops.transform.rotate(value=2.0391142674792424, orient_axis='Y')
bpy.ops.transform.rotate(value=1.6952126260710159, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.10595726329713706, 0.6884915641588092, 0.09121860417078786))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 4.068939497247985
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_4.JPEG"
bpy.ops.render.render(write_still=True)


