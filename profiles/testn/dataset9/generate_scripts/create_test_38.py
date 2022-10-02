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


# 21
ob = bpy.context.scene.objects[21]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.437411567386558, 0, 0.9098588865539785)
# rotation
bpy.ops.transform.rotate(value=0.5492637364746493, orient_axis='X')
bpy.ops.transform.rotate(value=0.16668274006900163, orient_axis='Y')
bpy.ops.transform.rotate(value=2.529221839335911, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.2438852125949893, 1.244583636176894, 0.7042464239037236))
ob.select_set(False)

# 242
ob = bpy.context.scene.objects[242]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.5036507916447994, 0, -4.176438523859397)
# rotation
bpy.ops.transform.rotate(value=2.256608767765384, orient_axis='X')
bpy.ops.transform.rotate(value=2.713288743146434, orient_axis='Y')
bpy.ops.transform.rotate(value=2.5917891565437072, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6896598877574125, 0.6144864231418681, 1.833107217255501))
ob.select_set(False)

# 119
ob = bpy.context.scene.objects[119]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.3927718659082995, 0, -2.001525603703503)
# rotation
bpy.ops.transform.rotate(value=0.05358508927524861, orient_axis='X')
bpy.ops.transform.rotate(value=0.10706080149750793, orient_axis='Y')
bpy.ops.transform.rotate(value=1.0262077983950035, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.7419616387435506, 0.19301766739102444, 0.3862404479580239))
ob.select_set(False)

# 584
ob = bpy.context.scene.objects[584]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.715037151691491, 0, -3.2896496663542063)
# rotation
bpy.ops.transform.rotate(value=2.731933224960524, orient_axis='X')
bpy.ops.transform.rotate(value=0.5067774835528588, orient_axis='Y')
bpy.ops.transform.rotate(value=1.5946721742073886, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.2143201541230166, 1.5375973068636637, 0.34243637922602455))
ob.select_set(False)

# 1
ob = bpy.context.scene.objects[1]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.0626834536444871, 0, -0.7114509149913362)
# rotation
bpy.ops.transform.rotate(value=1.089985762802704, orient_axis='X')
bpy.ops.transform.rotate(value=1.0998027421742518, orient_axis='Y')
bpy.ops.transform.rotate(value=0.22427462588472777, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.7610989533511034, 1.5770060828014785, 1.8742212611606324))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 9.188240015898897
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_38.JPEG"
bpy.ops.render.render(write_still=True)


