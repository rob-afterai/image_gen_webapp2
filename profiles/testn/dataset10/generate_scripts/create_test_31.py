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


# 530
ob = bpy.context.scene.objects[530]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.9161087977125311, 0, -3.7875360487476284)
# rotation
bpy.ops.transform.rotate(value=2.2898372885049243, orient_axis='X')
bpy.ops.transform.rotate(value=0.8629966456400276, orient_axis='Y')
bpy.ops.transform.rotate(value=1.6897699494151641, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.3328796932120379, 1.54789570124715, 1.1358501711849043))
ob.select_set(False)

# 518
ob = bpy.context.scene.objects[518]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.02045695537147285, 0, -3.185204047382052)
# rotation
bpy.ops.transform.rotate(value=2.1955896543135833, orient_axis='X')
bpy.ops.transform.rotate(value=2.47947168310019, orient_axis='Y')
bpy.ops.transform.rotate(value=2.3003081490229538, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.8686224108125262, 0.7765554839667987, 1.0940280574235497))
ob.select_set(False)

# 115
ob = bpy.context.scene.objects[115]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.0902335611347409, 0, -3.2653590150780483)
# rotation
bpy.ops.transform.rotate(value=1.2111692382125296, orient_axis='X')
bpy.ops.transform.rotate(value=0.2841058225229087, orient_axis='Y')
bpy.ops.transform.rotate(value=0.24298542434882828, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.38388054565660923, 1.933326852435342, 0.24597985263236732))
ob.select_set(False)

# 400
ob = bpy.context.scene.objects[400]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.444997407423122, 0, 4.249128142593941)
# rotation
bpy.ops.transform.rotate(value=0.2045291822869367, orient_axis='X')
bpy.ops.transform.rotate(value=0.2635154439551863, orient_axis='Y')
bpy.ops.transform.rotate(value=2.3199697702777007, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.138107982779364, 0.6945737764308602, 0.45312318977777544))
ob.select_set(False)

# 13
ob = bpy.context.scene.objects[13]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.298790707693983, 0, -3.4370683466401237)
# rotation
bpy.ops.transform.rotate(value=2.0488001039151964, orient_axis='X')
bpy.ops.transform.rotate(value=0.7818566008166815, orient_axis='Y')
bpy.ops.transform.rotate(value=0.6953818407673122, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.12110933144063085, 1.4663080794836563, 1.7781016787688138))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 7.1998388725848095
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_31.JPEG"
bpy.ops.render.render(write_still=True)


