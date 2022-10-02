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


# 240
ob = bpy.context.scene.objects[240]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.5116644170688023, 0, -2.254403171573108)
# rotation
bpy.ops.transform.rotate(value=3.0008360488969, orient_axis='X')
bpy.ops.transform.rotate(value=2.5053926895712952, orient_axis='Y')
bpy.ops.transform.rotate(value=2.887670758307015, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.9222476869622367, 0.15794667988438982, 0.5358858448054635))
ob.select_set(False)

# 163
ob = bpy.context.scene.objects[163]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.485369936511903, 0, -1.6018440649541117)
# rotation
bpy.ops.transform.rotate(value=0.1475847833821806, orient_axis='X')
bpy.ops.transform.rotate(value=2.9463125554680167, orient_axis='Y')
bpy.ops.transform.rotate(value=2.363718205985211, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.24880544131549454, 0.17260386189781407, 0.2235927905882642))
ob.select_set(False)

# 378
ob = bpy.context.scene.objects[378]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.0282641329719713, 0, -1.7857701988612877)
# rotation
bpy.ops.transform.rotate(value=0.130658592155994, orient_axis='X')
bpy.ops.transform.rotate(value=0.768978294041292, orient_axis='Y')
bpy.ops.transform.rotate(value=1.6765663280143825, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.2321751597814874, 0.3982124649462693, 0.49679219163348476))
ob.select_set(False)

# 57
ob = bpy.context.scene.objects[57]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.540490197005658, 0, 3.494314745290061)
# rotation
bpy.ops.transform.rotate(value=0.046137381731340715, orient_axis='X')
bpy.ops.transform.rotate(value=1.3211846046022047, orient_axis='Y')
bpy.ops.transform.rotate(value=2.984852513259309, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.69501277387422, 0.22361896176046492, 1.6299536655520592))
ob.select_set(False)

# 506
ob = bpy.context.scene.objects[506]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.6098746784258857, 0, 2.7864647787200862)
# rotation
bpy.ops.transform.rotate(value=1.370165492908298, orient_axis='X')
bpy.ops.transform.rotate(value=1.1207737572963556, orient_axis='Y')
bpy.ops.transform.rotate(value=2.114457962954945, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.18956037063210274, 1.0737662723171528, 1.591872744150822))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 16.163502716401645
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_26.JPEG"
bpy.ops.render.render(write_still=True)


