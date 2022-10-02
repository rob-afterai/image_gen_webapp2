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


# 474
ob = bpy.context.scene.objects[474]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.4675454474317746, 0, 2.852325375850251)
# rotation
bpy.ops.transform.rotate(value=0.6164836200795022, orient_axis='X')
bpy.ops.transform.rotate(value=2.357247755529561, orient_axis='Y')
bpy.ops.transform.rotate(value=2.957626112774669, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.0377210563155563, 0.822430321160097, 0.43552656773529175))
ob.select_set(False)

# 604
ob = bpy.context.scene.objects[604]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.7978743483314723, 0, 1.3012269403023629)
# rotation
bpy.ops.transform.rotate(value=2.09903215027139, orient_axis='X')
bpy.ops.transform.rotate(value=2.2098207806152934, orient_axis='Y')
bpy.ops.transform.rotate(value=0.1254927060265351, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.024689609371897125, 0.11661756655781552, 0.9361446269981604))
ob.select_set(False)

# 277
ob = bpy.context.scene.objects[277]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.1700087752449004, 0, -4.3793309794378255)
# rotation
bpy.ops.transform.rotate(value=2.250390812305437, orient_axis='X')
bpy.ops.transform.rotate(value=2.0580043491320428, orient_axis='Y')
bpy.ops.transform.rotate(value=3.1080202026211308, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.3380567411930084, 0.2343945488151864, 1.9132323391039685))
ob.select_set(False)

# 318
ob = bpy.context.scene.objects[318]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.1207162579131973, 0, 3.340143860953594)
# rotation
bpy.ops.transform.rotate(value=2.6443679480624853, orient_axis='X')
bpy.ops.transform.rotate(value=1.8479438747034411, orient_axis='Y')
bpy.ops.transform.rotate(value=0.15247392954470307, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.17402270599251146, 0.2727521733129856, 0.5221920892482546))
ob.select_set(False)

# 455
ob = bpy.context.scene.objects[455]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.1107728422669845, 0, -0.929530921696827)
# rotation
bpy.ops.transform.rotate(value=2.075631985991813, orient_axis='X')
bpy.ops.transform.rotate(value=0.22824645600593743, orient_axis='Y')
bpy.ops.transform.rotate(value=0.22903567619062856, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6758517967868112, 1.0428020785388912, 0.33097077418189214))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 11.0804988262748
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_34.JPEG"
bpy.ops.render.render(write_still=True)


