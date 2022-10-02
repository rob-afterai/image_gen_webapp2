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


# 197
ob = bpy.context.scene.objects[197]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.1196159678475937, 0, 0.9935834055327515)
# rotation
bpy.ops.transform.rotate(value=1.7037592499778758, orient_axis='X')
bpy.ops.transform.rotate(value=2.748415222537757, orient_axis='Y')
bpy.ops.transform.rotate(value=0.26849373998572884, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.5266610943337491, 1.7539610494364553, 1.8373674011321561))
ob.select_set(False)

# 451
ob = bpy.context.scene.objects[451]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.811190939477311, 0, -1.770602337265617)
# rotation
bpy.ops.transform.rotate(value=2.2670996856534864, orient_axis='X')
bpy.ops.transform.rotate(value=2.0794997823178547, orient_axis='Y')
bpy.ops.transform.rotate(value=1.3090562936011894, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.3602128675683482, 0.8515284031332819, 0.5059860806128631))
ob.select_set(False)

# 72
ob = bpy.context.scene.objects[72]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.474991983565552, 0, 3.1691088190235988)
# rotation
bpy.ops.transform.rotate(value=0.6117204115992314, orient_axis='X')
bpy.ops.transform.rotate(value=1.8049255677099791, orient_axis='Y')
bpy.ops.transform.rotate(value=0.6934363783362565, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.8302121753778493, 1.4002215550789059, 0.6179354307590152))
ob.select_set(False)

# 550
ob = bpy.context.scene.objects[550]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.51476958969623, 0, -0.6858746074092639)
# rotation
bpy.ops.transform.rotate(value=0.9373764705003764, orient_axis='X')
bpy.ops.transform.rotate(value=0.22446701502164515, orient_axis='Y')
bpy.ops.transform.rotate(value=2.3877479670313533, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.653424686598479, 1.5069178451218144, 1.032876818955526))
ob.select_set(False)

# 39
ob = bpy.context.scene.objects[39]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.3828945628092892, 0, -2.8856063061209976)
# rotation
bpy.ops.transform.rotate(value=2.7435475036267576, orient_axis='X')
bpy.ops.transform.rotate(value=1.4418587137182086, orient_axis='Y')
bpy.ops.transform.rotate(value=1.2446566534933192, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6625575581626282, 0.1181003150156048, 0.2683451340255605))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 17.24195708895431
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_18.JPEG"
bpy.ops.render.render(write_still=True)


