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


# 188
ob = bpy.context.scene.objects[188]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.156734459744569, 0, -2.75179364595601)
# rotation
bpy.ops.transform.rotate(value=0.6883540209023912, orient_axis='X')
bpy.ops.transform.rotate(value=0.6813312770488683, orient_axis='Y')
bpy.ops.transform.rotate(value=1.4125938197646555, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6395933802936238, 1.2182339406338114, 0.8223227231788162))
ob.select_set(False)

# 186
ob = bpy.context.scene.objects[186]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.4398387614717905, 0, -4.404754843329304)
# rotation
bpy.ops.transform.rotate(value=2.324423030556132, orient_axis='X')
bpy.ops.transform.rotate(value=0.7441450202370927, orient_axis='Y')
bpy.ops.transform.rotate(value=1.990055491884512, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9222337879653, 1.8684540228062056, 1.6502054722892217))
ob.select_set(False)

# 514
ob = bpy.context.scene.objects[514]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.3577160135606423, 0, 0.1773365723414555)
# rotation
bpy.ops.transform.rotate(value=1.0405768484573392, orient_axis='X')
bpy.ops.transform.rotate(value=1.6885632729306408, orient_axis='Y')
bpy.ops.transform.rotate(value=0.8917905350658601, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.4164432245334186, 1.3777473141074303, 0.09996100063052316))
ob.select_set(False)

# 56
ob = bpy.context.scene.objects[56]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.7019487674722749, 0, 2.1528031880869554)
# rotation
bpy.ops.transform.rotate(value=1.1341433287700837, orient_axis='X')
bpy.ops.transform.rotate(value=2.36260109381356, orient_axis='Y')
bpy.ops.transform.rotate(value=3.006656680241092, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.5216007795315567, 1.4460020595993046, 0.416942311993745))
ob.select_set(False)

# 68
ob = bpy.context.scene.objects[68]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.8226498925937316, 0, -2.7287133651022915)
# rotation
bpy.ops.transform.rotate(value=0.6755690585352369, orient_axis='X')
bpy.ops.transform.rotate(value=2.6761348583601103, orient_axis='Y')
bpy.ops.transform.rotate(value=2.1583274258963843, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.0989185862809605, 1.4831540160307837, 0.7348526277472889))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 15.740937083494721
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_98.JPEG"
bpy.ops.render.render(write_still=True)


