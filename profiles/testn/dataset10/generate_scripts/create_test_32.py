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


# 343
ob = bpy.context.scene.objects[343]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.5212564138089366, 0, -4.011927870381621)
# rotation
bpy.ops.transform.rotate(value=1.0267953676390131, orient_axis='X')
bpy.ops.transform.rotate(value=1.5612499525511185, orient_axis='Y')
bpy.ops.transform.rotate(value=0.7910547137436968, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6694127919466855, 0.8907327363291806, 1.699050391904932))
ob.select_set(False)

# 44
ob = bpy.context.scene.objects[44]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.6725358459122246, 0, 3.1617624626659424)
# rotation
bpy.ops.transform.rotate(value=1.7988248075093785, orient_axis='X')
bpy.ops.transform.rotate(value=1.2951013710137405, orient_axis='Y')
bpy.ops.transform.rotate(value=0.9483853443281143, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.7884466199077638, 0.19212409085974214, 0.9494399847032471))
ob.select_set(False)

# 369
ob = bpy.context.scene.objects[369]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.5476819148611405, 0, 4.083542855944289)
# rotation
bpy.ops.transform.rotate(value=1.0103767525658278, orient_axis='X')
bpy.ops.transform.rotate(value=1.1325130251719104, orient_axis='Y')
bpy.ops.transform.rotate(value=2.627130954804373, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.6768402976217265, 0.7319248062869395, 0.7938008498829279))
ob.select_set(False)

# 5
ob = bpy.context.scene.objects[5]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.963975979168646, 0, 2.5688923087916153)
# rotation
bpy.ops.transform.rotate(value=1.8041310876699437, orient_axis='X')
bpy.ops.transform.rotate(value=1.5628200020801684, orient_axis='Y')
bpy.ops.transform.rotate(value=1.5667753626693415, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8591323977848377, 0.28985333922140954, 1.1129784413699386))
ob.select_set(False)

# 518
ob = bpy.context.scene.objects[518]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.4004389834613704, 0, -0.9595848140176537)
# rotation
bpy.ops.transform.rotate(value=1.2263027298183373, orient_axis='X')
bpy.ops.transform.rotate(value=0.6597400908316517, orient_axis='Y')
bpy.ops.transform.rotate(value=1.9394309572321322, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.7138827849262581, 0.8068151665678678, 0.2923662238282734))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 10.925324728565366
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_32.JPEG"
bpy.ops.render.render(write_still=True)


