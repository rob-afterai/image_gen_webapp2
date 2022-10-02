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


# 276
ob = bpy.context.scene.objects[276]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.0272848229592295, 0, 1.4363111513664126)
# rotation
bpy.ops.transform.rotate(value=1.9312024137914223, orient_axis='X')
bpy.ops.transform.rotate(value=0.057812626579196134, orient_axis='Y')
bpy.ops.transform.rotate(value=2.8827915018166492, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.266421799544613, 1.3472283393685294, 1.265725578993539))
ob.select_set(False)

# 387
ob = bpy.context.scene.objects[387]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.6459502080199098, 0, -0.2104000103183088)
# rotation
bpy.ops.transform.rotate(value=2.5598762564017736, orient_axis='X')
bpy.ops.transform.rotate(value=2.5965246373723065, orient_axis='Y')
bpy.ops.transform.rotate(value=2.1656599028965466, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.14657725241258124, 0.9967786976960318, 0.5402837204762672))
ob.select_set(False)

# 73
ob = bpy.context.scene.objects[73]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.9379097416891358, 0, -0.5938624691920387)
# rotation
bpy.ops.transform.rotate(value=1.8679932212260575, orient_axis='X')
bpy.ops.transform.rotate(value=1.486262412614739, orient_axis='Y')
bpy.ops.transform.rotate(value=0.6792895138915123, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.1312796257660518, 0.4258739997402399, 0.23782827786472382))
ob.select_set(False)

# 208
ob = bpy.context.scene.objects[208]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.028149256005871592, 0, 1.5893374821498654)
# rotation
bpy.ops.transform.rotate(value=1.348677073309827, orient_axis='X')
bpy.ops.transform.rotate(value=1.8196582891523205, orient_axis='Y')
bpy.ops.transform.rotate(value=1.3067810695916904, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.7084329251913009, 0.4776949603025804, 1.687449075935375))
ob.select_set(False)

# 373
ob = bpy.context.scene.objects[373]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.27942154081885384, 0, 1.9248928751732635)
# rotation
bpy.ops.transform.rotate(value=0.7247907659809423, orient_axis='X')
bpy.ops.transform.rotate(value=2.472067977235734, orient_axis='Y')
bpy.ops.transform.rotate(value=2.0800718048047195, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.678416396197232, 1.6860883913129132, 0.4493387508412525))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 5.493594645278517
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_82.JPEG"
bpy.ops.render.render(write_still=True)


