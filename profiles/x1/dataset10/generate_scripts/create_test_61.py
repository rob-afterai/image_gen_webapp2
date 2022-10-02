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


# 565
ob = bpy.context.scene.objects[565]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.1112686145183335, 0, -1.4394898939825183)
# rotation
bpy.ops.transform.rotate(value=1.3509598581202142, orient_axis='X')
bpy.ops.transform.rotate(value=1.4319675005108412, orient_axis='Y')
bpy.ops.transform.rotate(value=1.427127454064221, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.7394877958956829, 1.9981797295815433, 1.6333888392240592))
ob.select_set(False)

# 183
ob = bpy.context.scene.objects[183]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.7351820240705798, 0, -0.13404232458156784)
# rotation
bpy.ops.transform.rotate(value=0.76285566834662, orient_axis='X')
bpy.ops.transform.rotate(value=0.6075194568731777, orient_axis='Y')
bpy.ops.transform.rotate(value=1.4986100086393277, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.43717018141631825, 0.9607572428284339, 1.1561555720622776))
ob.select_set(False)

# 361
ob = bpy.context.scene.objects[361]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.9238531131452525, 0, 1.2328263568934883)
# rotation
bpy.ops.transform.rotate(value=1.087347094364684, orient_axis='X')
bpy.ops.transform.rotate(value=2.970194082682109, orient_axis='Y')
bpy.ops.transform.rotate(value=2.6528555190553824, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.26495839742978, 0.22684209520642895, 1.1261349743535836))
ob.select_set(False)

# 510
ob = bpy.context.scene.objects[510]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.1723537530862167, 0, -1.415706036840894)
# rotation
bpy.ops.transform.rotate(value=0.6001933691489688, orient_axis='X')
bpy.ops.transform.rotate(value=0.8728556035827292, orient_axis='Y')
bpy.ops.transform.rotate(value=0.8028082153561142, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.5198133422821485, 0.8172468202173788, 0.7923655904412075))
ob.select_set(False)

# 36
ob = bpy.context.scene.objects[36]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.2350209133067374, 0, 2.8422594732848365)
# rotation
bpy.ops.transform.rotate(value=0.122192359111672, orient_axis='X')
bpy.ops.transform.rotate(value=2.474601236349074, orient_axis='Y')
bpy.ops.transform.rotate(value=0.7232358992733707, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.4115989087258014, 0.8026091493110099, 1.2782281947609413))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 1.1935139566125086
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_61.JPEG"
bpy.ops.render.render(write_still=True)


