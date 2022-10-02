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


# 186
ob = bpy.context.scene.objects[186]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.6995688298267257, 0, -2.199272014523087)
# rotation
bpy.ops.transform.rotate(value=2.233823893034543, orient_axis='X')
bpy.ops.transform.rotate(value=2.8042398667218325, orient_axis='Y')
bpy.ops.transform.rotate(value=0.6710534960682165, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.4041798755278614, 1.4425505029011136, 1.6514991383965028))
ob.select_set(False)

# 384
ob = bpy.context.scene.objects[384]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.278440921987234, 0, -1.439848528627964)
# rotation
bpy.ops.transform.rotate(value=0.5395473819714647, orient_axis='X')
bpy.ops.transform.rotate(value=0.634382067205757, orient_axis='Y')
bpy.ops.transform.rotate(value=1.3090583594521654, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6680675827304006, 0.7519755185973926, 1.2392819014676009))
ob.select_set(False)

# 109
ob = bpy.context.scene.objects[109]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.7940802741383521, 0, 3.0776657350549437)
# rotation
bpy.ops.transform.rotate(value=1.5742733514935403, orient_axis='X')
bpy.ops.transform.rotate(value=1.623128052400789, orient_axis='Y')
bpy.ops.transform.rotate(value=0.2607434320940479, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.9872894006145907, 0.9715265987195736, 0.10241192637537178))
ob.select_set(False)

# 390
ob = bpy.context.scene.objects[390]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.634204351952902, 0, 0.19752449538226813)
# rotation
bpy.ops.transform.rotate(value=0.5120980152103323, orient_axis='X')
bpy.ops.transform.rotate(value=2.5412807630913825, orient_axis='Y')
bpy.ops.transform.rotate(value=2.330828278915538, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.335290683052625, 1.6142451886311602, 1.4719958672220974))
ob.select_set(False)

# 403
ob = bpy.context.scene.objects[403]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.263894091495545, 0, -1.661072502625145)
# rotation
bpy.ops.transform.rotate(value=2.804733401851314, orient_axis='X')
bpy.ops.transform.rotate(value=3.002597068253852, orient_axis='Y')
bpy.ops.transform.rotate(value=0.9298560728910775, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.9598054404083511, 0.49424138331461265, 0.7249337971081715))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 1.0018311719994788
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_44.JPEG"
bpy.ops.render.render(write_still=True)


