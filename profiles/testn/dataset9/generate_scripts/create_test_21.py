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


# 564
ob = bpy.context.scene.objects[564]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.6991672434667233, 0, 3.3848394200095875)
# rotation
bpy.ops.transform.rotate(value=2.089329290013817, orient_axis='X')
bpy.ops.transform.rotate(value=2.025616982337571, orient_axis='Y')
bpy.ops.transform.rotate(value=0.17600120283770082, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.2046256381088607, 0.7790836094751259, 1.6800851441159856))
ob.select_set(False)

# 424
ob = bpy.context.scene.objects[424]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.473156005070477, 0, 2.9024212543501164)
# rotation
bpy.ops.transform.rotate(value=1.8206001605357003, orient_axis='X')
bpy.ops.transform.rotate(value=2.5541401446047756, orient_axis='Y')
bpy.ops.transform.rotate(value=1.2707862558641454, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8321587705122249, 0.4982027092757033, 0.43451890002243987))
ob.select_set(False)

# 229
ob = bpy.context.scene.objects[229]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.171631130082686, 0, 0.26270644833306456)
# rotation
bpy.ops.transform.rotate(value=1.7975162174886032, orient_axis='X')
bpy.ops.transform.rotate(value=0.43408184468219685, orient_axis='Y')
bpy.ops.transform.rotate(value=2.682468835865913, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1299895457390667, 1.1629846521308296, 0.6115777929131452))
ob.select_set(False)

# 488
ob = bpy.context.scene.objects[488]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.898074689505882, 0, 3.810342513472966)
# rotation
bpy.ops.transform.rotate(value=2.586104028488756, orient_axis='X')
bpy.ops.transform.rotate(value=1.2612932178505136, orient_axis='Y')
bpy.ops.transform.rotate(value=1.298688965908195, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.48950122963320375, 0.6957596474540366, 1.094729122667329))
ob.select_set(False)

# 488
ob = bpy.context.scene.objects[488]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.232024065871506, 0, 0.17428492396269757)
# rotation
bpy.ops.transform.rotate(value=1.5804175804587208, orient_axis='X')
bpy.ops.transform.rotate(value=2.2523415984779396, orient_axis='Y')
bpy.ops.transform.rotate(value=0.6943108524414475, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.602259256595075, 0.15548403243890663, 1.9943616704089315))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 1.8460189900029134
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_21.JPEG"
bpy.ops.render.render(write_still=True)


