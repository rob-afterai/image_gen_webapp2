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


# 101
ob = bpy.context.scene.objects[101]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.6698587116397334, 0, 0.18853566319717885)
# rotation
bpy.ops.transform.rotate(value=1.5616520617509824, orient_axis='X')
bpy.ops.transform.rotate(value=1.322332205279914, orient_axis='Y')
bpy.ops.transform.rotate(value=1.5169666449660704, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6932399132228539, 1.7118787770304358, 1.0396476531371126))
ob.select_set(False)

# 455
ob = bpy.context.scene.objects[455]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.8782682336336363, 0, 1.5390492933677793)
# rotation
bpy.ops.transform.rotate(value=1.1521312446619867, orient_axis='X')
bpy.ops.transform.rotate(value=1.0628147208508327, orient_axis='Y')
bpy.ops.transform.rotate(value=2.843356228355097, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.0310816318646303, 0.20752040687811246, 0.7296668697826219))
ob.select_set(False)

# 399
ob = bpy.context.scene.objects[399]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.16815828401647437, 0, -0.954242149157853)
# rotation
bpy.ops.transform.rotate(value=0.10758332418455013, orient_axis='X')
bpy.ops.transform.rotate(value=0.3538767853182937, orient_axis='Y')
bpy.ops.transform.rotate(value=1.6677140584194514, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.264844930352677, 0.9771245675996041, 1.5941031429042523))
ob.select_set(False)

# 495
ob = bpy.context.scene.objects[495]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.6114069408493386, 0, -4.269789221900438)
# rotation
bpy.ops.transform.rotate(value=0.06371304278790402, orient_axis='X')
bpy.ops.transform.rotate(value=1.4525694889656366, orient_axis='Y')
bpy.ops.transform.rotate(value=1.8979328221723504, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9157722153583927, 1.4018181349404797, 0.7734670288753958))
ob.select_set(False)

# 559
ob = bpy.context.scene.objects[559]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.127272835430453, 0, 2.9077896352115715)
# rotation
bpy.ops.transform.rotate(value=2.3884569984822397, orient_axis='X')
bpy.ops.transform.rotate(value=1.305965458186283, orient_axis='Y')
bpy.ops.transform.rotate(value=0.26460135475876156, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.22597773479202576, 1.3518609653376257, 0.6093764479761654))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 11.320583181157694
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_25.JPEG"
bpy.ops.render.render(write_still=True)


