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


# 100
ob = bpy.context.scene.objects[100]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.755585255788764, 0, -1.7030991931198427)
# rotation
bpy.ops.transform.rotate(value=2.555602957519116, orient_axis='X')
bpy.ops.transform.rotate(value=1.1944293278343951, orient_axis='Y')
bpy.ops.transform.rotate(value=2.049868116685661, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6683551785395132, 1.4261922780679008, 0.0567066083436123))
ob.select_set(False)

# 398
ob = bpy.context.scene.objects[398]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.95314535389637, 0, -3.8388578406139393)
# rotation
bpy.ops.transform.rotate(value=0.916812678012664, orient_axis='X')
bpy.ops.transform.rotate(value=2.4804642780791144, orient_axis='Y')
bpy.ops.transform.rotate(value=1.6149987691106467, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.983443383534829, 0.8819431764359342, 1.062523903308439))
ob.select_set(False)

# 50
ob = bpy.context.scene.objects[50]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.141098632993035, 0, 0.3869175782368268)
# rotation
bpy.ops.transform.rotate(value=2.697697754283886, orient_axis='X')
bpy.ops.transform.rotate(value=0.8430671205504527, orient_axis='Y')
bpy.ops.transform.rotate(value=0.1862047302675405, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.138168834014485, 1.8979398570144215, 0.2076189239798676))
ob.select_set(False)

# 391
ob = bpy.context.scene.objects[391]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.1162017072867911, 0, -0.389036932907457)
# rotation
bpy.ops.transform.rotate(value=1.928290191612388, orient_axis='X')
bpy.ops.transform.rotate(value=0.3851081090750907, orient_axis='Y')
bpy.ops.transform.rotate(value=0.39944972303737025, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1067189395579757, 0.7575623031706187, 1.154776724055808))
ob.select_set(False)

# 301
ob = bpy.context.scene.objects[301]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.6720080769854286, 0, 4.198081821229248)
# rotation
bpy.ops.transform.rotate(value=2.852849150332796, orient_axis='X')
bpy.ops.transform.rotate(value=1.6747834585561476, orient_axis='Y')
bpy.ops.transform.rotate(value=0.46685814980093343, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.05227034527468688, 0.1493752044194967, 1.2957795331305682))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 7.10957744468693
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_30.JPEG"
bpy.ops.render.render(write_still=True)


