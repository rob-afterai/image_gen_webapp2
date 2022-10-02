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


# 420
ob = bpy.context.scene.objects[420]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.3429746702703396, 0, 1.0606437952197112)
# rotation
bpy.ops.transform.rotate(value=1.445708931342644, orient_axis='X')
bpy.ops.transform.rotate(value=2.9643597300659015, orient_axis='Y')
bpy.ops.transform.rotate(value=1.8709181927641922, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.3092081536066713, 1.2697541545423412, 0.1595755462165429))
ob.select_set(False)

# 313
ob = bpy.context.scene.objects[313]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.6268620474961875, 0, -4.309514456570152)
# rotation
bpy.ops.transform.rotate(value=2.5298289710049064, orient_axis='X')
bpy.ops.transform.rotate(value=2.1125042948902366, orient_axis='Y')
bpy.ops.transform.rotate(value=1.4364830524738281, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8097514288910659, 1.610606585887264, 0.11221311788821176))
ob.select_set(False)

# 389
ob = bpy.context.scene.objects[389]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.8254195552957033, 0, -3.516727573028686)
# rotation
bpy.ops.transform.rotate(value=2.45530358579249, orient_axis='X')
bpy.ops.transform.rotate(value=1.4757591773114622, orient_axis='Y')
bpy.ops.transform.rotate(value=0.6238226248234854, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.6258422437258915, 0.6344946713463744, 1.4089382358071185))
ob.select_set(False)

# 199
ob = bpy.context.scene.objects[199]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.870390964154461, 0, 4.160635835457491)
# rotation
bpy.ops.transform.rotate(value=0.07401937344511925, orient_axis='X')
bpy.ops.transform.rotate(value=0.584129794165701, orient_axis='Y')
bpy.ops.transform.rotate(value=1.1208990772152843, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.040560037280154004, 1.4580394011078, 1.343866477323543))
ob.select_set(False)

# 380
ob = bpy.context.scene.objects[380]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.356322545333834, 0, -3.1818955577308277)
# rotation
bpy.ops.transform.rotate(value=1.108739314784778, orient_axis='X')
bpy.ops.transform.rotate(value=1.3236840402370156, orient_axis='Y')
bpy.ops.transform.rotate(value=1.1446012401805599, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.8646205743429369, 1.6177374979148114, 0.4905074767232902))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 19.732792754643956
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_89.JPEG"
bpy.ops.render.render(write_still=True)


