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


# 288
ob = bpy.context.scene.objects[288]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.092746626325778, 0, 2.6721242897378525)
# rotation
bpy.ops.transform.rotate(value=2.3643450714587284, orient_axis='X')
bpy.ops.transform.rotate(value=2.8880645787405084, orient_axis='Y')
bpy.ops.transform.rotate(value=0.01879041976755364, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8161427555548464, 1.9356187370652576, 0.9942069987562729))
ob.select_set(False)

# 93
ob = bpy.context.scene.objects[93]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.0624931137205924, 0, -0.7994148184897836)
# rotation
bpy.ops.transform.rotate(value=0.42762919636172014, orient_axis='X')
bpy.ops.transform.rotate(value=0.15336333873366345, orient_axis='Y')
bpy.ops.transform.rotate(value=1.8614916982633305, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1514626406169368, 0.5303005592857255, 1.5208943940058526))
ob.select_set(False)

# 446
ob = bpy.context.scene.objects[446]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.779755561146672, 0, 0.14821091793400765)
# rotation
bpy.ops.transform.rotate(value=0.3356608592553274, orient_axis='X')
bpy.ops.transform.rotate(value=1.5361192121494662, orient_axis='Y')
bpy.ops.transform.rotate(value=2.4614367083273816, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.8969994181401919, 0.8548384513232878, 0.22332840753152983))
ob.select_set(False)

# 504
ob = bpy.context.scene.objects[504]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.1982964297940768, 0, 4.288466782178354)
# rotation
bpy.ops.transform.rotate(value=0.6459883629283635, orient_axis='X')
bpy.ops.transform.rotate(value=1.1854884971077444, orient_axis='Y')
bpy.ops.transform.rotate(value=2.5517102967418817, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.6355079185853898, 1.0548909512100217, 0.06952285673738023))
ob.select_set(False)

# 472
ob = bpy.context.scene.objects[472]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.166917891454977, 0, -2.3481112309897423)
# rotation
bpy.ops.transform.rotate(value=2.655635360878092, orient_axis='X')
bpy.ops.transform.rotate(value=1.3806591783065862, orient_axis='Y')
bpy.ops.transform.rotate(value=1.4151610065821774, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9944825884884483, 1.885778347509941, 1.9167128729241147))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 6.743671592537661
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_77.JPEG"
bpy.ops.render.render(write_still=True)


