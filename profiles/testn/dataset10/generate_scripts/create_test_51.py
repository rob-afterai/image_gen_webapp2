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


# 584
ob = bpy.context.scene.objects[584]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.116821735908416, 0, 2.5196034015599986)
# rotation
bpy.ops.transform.rotate(value=1.514950623339419, orient_axis='X')
bpy.ops.transform.rotate(value=2.9065769157357098, orient_axis='Y')
bpy.ops.transform.rotate(value=2.8248767660712235, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1127211661044603, 1.2675674441515525, 0.5776507779882889))
ob.select_set(False)

# 531
ob = bpy.context.scene.objects[531]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.20557283088338618, 0, 0.828131921663851)
# rotation
bpy.ops.transform.rotate(value=0.6472282245461134, orient_axis='X')
bpy.ops.transform.rotate(value=2.9737505073409727, orient_axis='Y')
bpy.ops.transform.rotate(value=0.9172068255347524, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.43216475159548495, 0.3409807723320959, 1.78925329371677))
ob.select_set(False)

# 517
ob = bpy.context.scene.objects[517]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.055623929287089, 0, -3.125839408544237)
# rotation
bpy.ops.transform.rotate(value=1.311136144353622, orient_axis='X')
bpy.ops.transform.rotate(value=1.805814967833403, orient_axis='Y')
bpy.ops.transform.rotate(value=1.136738863717863, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.7648036827502247, 1.671327470985618, 1.4161372975189956))
ob.select_set(False)

# 92
ob = bpy.context.scene.objects[92]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.1349604247362093, 0, 1.9092449997491983)
# rotation
bpy.ops.transform.rotate(value=0.28745465937392406, orient_axis='X')
bpy.ops.transform.rotate(value=2.43961422449735, orient_axis='Y')
bpy.ops.transform.rotate(value=1.1372652719290792, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.7811678364897594, 0.003779035688574739, 0.6887882683098909))
ob.select_set(False)

# 393
ob = bpy.context.scene.objects[393]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.439168645604215, 0, 1.3992516651090954)
# rotation
bpy.ops.transform.rotate(value=2.9152129622544076, orient_axis='X')
bpy.ops.transform.rotate(value=0.6141533509124563, orient_axis='Y')
bpy.ops.transform.rotate(value=1.0837036572981291, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.938617915523903, 0.9112286149965696, 0.08175607630621151))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 8.35522364888055
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_51.JPEG"
bpy.ops.render.render(write_still=True)


