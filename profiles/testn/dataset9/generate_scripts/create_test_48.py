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


# 242
ob = bpy.context.scene.objects[242]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.0994348383733072, 0, -4.205040754434324)
# rotation
bpy.ops.transform.rotate(value=1.5231600539140178, orient_axis='X')
bpy.ops.transform.rotate(value=2.8495423995405083, orient_axis='Y')
bpy.ops.transform.rotate(value=0.4617602137285766, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.5269152348517012, 1.313565354080432, 0.2658576248531297))
ob.select_set(False)

# 504
ob = bpy.context.scene.objects[504]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.4076246772116034, 0, 2.462190689288585)
# rotation
bpy.ops.transform.rotate(value=2.4951753104733885, orient_axis='X')
bpy.ops.transform.rotate(value=1.0413691984040976, orient_axis='Y')
bpy.ops.transform.rotate(value=1.0226824249925601, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.5388185401885384, 0.2969898378849818, 0.7382124442278155))
ob.select_set(False)

# 566
ob = bpy.context.scene.objects[566]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.8195120935782336, 0, 0.15623590229893836)
# rotation
bpy.ops.transform.rotate(value=1.8120923952675438, orient_axis='X')
bpy.ops.transform.rotate(value=2.2793879506319152, orient_axis='Y')
bpy.ops.transform.rotate(value=1.5417576121197885, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.63419072753093, 1.3906229087157327, 0.11364664791317258))
ob.select_set(False)

# 271
ob = bpy.context.scene.objects[271]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.7817196047670851, 0, 3.50605750748103)
# rotation
bpy.ops.transform.rotate(value=2.2963814559371545, orient_axis='X')
bpy.ops.transform.rotate(value=1.308331107976621, orient_axis='Y')
bpy.ops.transform.rotate(value=1.7309035745792534, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.4916693658759377, 0.27785944159579246, 1.4355972758974647))
ob.select_set(False)

# 367
ob = bpy.context.scene.objects[367]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.019789103071928, 0, 1.24508313194925)
# rotation
bpy.ops.transform.rotate(value=2.3094816089539503, orient_axis='X')
bpy.ops.transform.rotate(value=2.230236212175613, orient_axis='Y')
bpy.ops.transform.rotate(value=1.5626083087896472, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.3143748735263725, 1.323828262440456, 0.5439669745431315))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 7.609168533612449
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_48.JPEG"
bpy.ops.render.render(write_still=True)


