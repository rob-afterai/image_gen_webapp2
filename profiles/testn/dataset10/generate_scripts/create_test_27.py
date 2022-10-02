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


# 278
ob = bpy.context.scene.objects[278]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.22877460546789763, 0, -2.790333965485191)
# rotation
bpy.ops.transform.rotate(value=0.6776825258157289, orient_axis='X')
bpy.ops.transform.rotate(value=2.026828535499018, orient_axis='Y')
bpy.ops.transform.rotate(value=2.0202754963983276, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8307082491288307, 0.3996317503258531, 1.0672313221817495))
ob.select_set(False)

# 515
ob = bpy.context.scene.objects[515]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.6866803858764285, 0, -0.4239941362433539)
# rotation
bpy.ops.transform.rotate(value=1.1289474320122423, orient_axis='X')
bpy.ops.transform.rotate(value=1.8909912657376127, orient_axis='Y')
bpy.ops.transform.rotate(value=1.064776599046392, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.0866997369513791, 0.4269087159709375, 1.2661422256607795))
ob.select_set(False)

# 124
ob = bpy.context.scene.objects[124]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.23506444618994404, 0, -2.9110014938876914)
# rotation
bpy.ops.transform.rotate(value=1.269740833496065, orient_axis='X')
bpy.ops.transform.rotate(value=3.0714592516486143, orient_axis='Y')
bpy.ops.transform.rotate(value=1.1248360264679618, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.4609387720694114, 0.8025432178057934, 0.5077632263184559))
ob.select_set(False)

# 337
ob = bpy.context.scene.objects[337]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.3772067144351228, 0, -0.3868748942419602)
# rotation
bpy.ops.transform.rotate(value=2.0792839567838257, orient_axis='X')
bpy.ops.transform.rotate(value=0.7686896617745566, orient_axis='Y')
bpy.ops.transform.rotate(value=1.2177810210633135, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.9535122991410732, 0.4352015435337633, 0.5628694008667001))
ob.select_set(False)

# 260
ob = bpy.context.scene.objects[260]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.2499397952333835, 0, 0.2673483287833216)
# rotation
bpy.ops.transform.rotate(value=0.846441293153563, orient_axis='X')
bpy.ops.transform.rotate(value=2.529333696381236, orient_axis='Y')
bpy.ops.transform.rotate(value=1.4415109184751866, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.45951548066089676, 0.11335306701270476, 1.1932294324581596))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 2.465799815205836
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_27.JPEG"
bpy.ops.render.render(write_still=True)


