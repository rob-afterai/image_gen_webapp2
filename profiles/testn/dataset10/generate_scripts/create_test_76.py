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


# 228
ob = bpy.context.scene.objects[228]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.131432378571095, 0, -0.27692874442842097)
# rotation
bpy.ops.transform.rotate(value=1.7454518710738856, orient_axis='X')
bpy.ops.transform.rotate(value=1.3686618276207194, orient_axis='Y')
bpy.ops.transform.rotate(value=0.8166038498625932, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.039204617893538574, 0.7012616978320212, 0.3404464235777698))
ob.select_set(False)

# 239
ob = bpy.context.scene.objects[239]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.41581169691407016, 0, 0.01439266256020666)
# rotation
bpy.ops.transform.rotate(value=2.579718540505428, orient_axis='X')
bpy.ops.transform.rotate(value=0.25080476757188036, orient_axis='Y')
bpy.ops.transform.rotate(value=1.470263404699504, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.24982273495069918, 1.170278700675688, 0.6802321235401161))
ob.select_set(False)

# 79
ob = bpy.context.scene.objects[79]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.9442827842597907, 0, 0.35335920693489786)
# rotation
bpy.ops.transform.rotate(value=0.15182638829308595, orient_axis='X')
bpy.ops.transform.rotate(value=0.6117048869165047, orient_axis='Y')
bpy.ops.transform.rotate(value=0.6308297203089449, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.513364519582289, 0.5493874524843843, 1.1717286655962151))
ob.select_set(False)

# 237
ob = bpy.context.scene.objects[237]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.9965122564334372, 0, -2.465410862468657)
# rotation
bpy.ops.transform.rotate(value=0.45023706522617185, orient_axis='X')
bpy.ops.transform.rotate(value=1.0978021656312766, orient_axis='Y')
bpy.ops.transform.rotate(value=0.5787462368883457, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.2218354838429966, 0.023337817785110015, 0.286326720307545))
ob.select_set(False)

# 590
ob = bpy.context.scene.objects[590]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.921046505314032, 0, -1.8295666063183935)
# rotation
bpy.ops.transform.rotate(value=1.9005144658076716, orient_axis='X')
bpy.ops.transform.rotate(value=1.8318843356060908, orient_axis='Y')
bpy.ops.transform.rotate(value=1.0273474360433204, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.20465882056130313, 1.0181532552045696, 0.983260700476223))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 1.9719636977342203
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_76.JPEG"
bpy.ops.render.render(write_still=True)


