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


# 339
ob = bpy.context.scene.objects[339]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.313151329162011, 0, 2.2844035004441334)
# rotation
bpy.ops.transform.rotate(value=1.653869241793109, orient_axis='X')
bpy.ops.transform.rotate(value=2.0094743061443285, orient_axis='Y')
bpy.ops.transform.rotate(value=1.9987757481542845, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.779801201422362, 1.1527170736466124, 1.3132662347867199))
ob.select_set(False)

# 53
ob = bpy.context.scene.objects[53]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.8711474447229866, 0, -3.2434207066152627)
# rotation
bpy.ops.transform.rotate(value=0.6222565305321789, orient_axis='X')
bpy.ops.transform.rotate(value=1.9842193039986946, orient_axis='Y')
bpy.ops.transform.rotate(value=0.5494914827579194, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.890122950098482, 1.2520705935667948, 1.7045186896182318))
ob.select_set(False)

# 6
ob = bpy.context.scene.objects[6]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.3560899188622564, 0, -3.925508554977255)
# rotation
bpy.ops.transform.rotate(value=0.2719372949197406, orient_axis='X')
bpy.ops.transform.rotate(value=0.030030760883009006, orient_axis='Y')
bpy.ops.transform.rotate(value=0.5523922247865218, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.585679677049027, 1.9591553355976778, 0.7270567117106161))
ob.select_set(False)

# 506
ob = bpy.context.scene.objects[506]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.8685819339804395, 0, 3.052224191638812)
# rotation
bpy.ops.transform.rotate(value=2.994732603515636, orient_axis='X')
bpy.ops.transform.rotate(value=2.551056093129925, orient_axis='Y')
bpy.ops.transform.rotate(value=1.7828548772692365, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.02568024903448185, 1.1406977538242586, 1.4281120542105583))
ob.select_set(False)

# 337
ob = bpy.context.scene.objects[337]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.173792484550229, 0, -0.17524786261070435)
# rotation
bpy.ops.transform.rotate(value=2.2670058455866657, orient_axis='X')
bpy.ops.transform.rotate(value=1.7889613887685645, orient_axis='Y')
bpy.ops.transform.rotate(value=2.407554221352419, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1825849443855478, 0.23387677004789165, 0.896914035821057))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 18.94327428468175
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_49.JPEG"
bpy.ops.render.render(write_still=True)


