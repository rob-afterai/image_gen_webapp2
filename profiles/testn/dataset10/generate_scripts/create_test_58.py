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


# 64
ob = bpy.context.scene.objects[64]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.3739882668888388, 0, 1.6257666853083927)
# rotation
bpy.ops.transform.rotate(value=2.101848605948078, orient_axis='X')
bpy.ops.transform.rotate(value=2.9942255365161734, orient_axis='Y')
bpy.ops.transform.rotate(value=1.630613868612476, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.8303599614854924, 0.3928055925662248, 0.4272805532754329))
ob.select_set(False)

# 387
ob = bpy.context.scene.objects[387]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.6941420940027534, 0, -1.972006402734297)
# rotation
bpy.ops.transform.rotate(value=0.8797866145189474, orient_axis='X')
bpy.ops.transform.rotate(value=0.5269360554519478, orient_axis='Y')
bpy.ops.transform.rotate(value=0.10183590524575334, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1997915255325906, 1.1893039396377423, 0.9114783028383595))
ob.select_set(False)

# 524
ob = bpy.context.scene.objects[524]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.9097226359125896, 0, 0.16061817801927525)
# rotation
bpy.ops.transform.rotate(value=2.3051587817528385, orient_axis='X')
bpy.ops.transform.rotate(value=0.5194115176040274, orient_axis='Y')
bpy.ops.transform.rotate(value=2.633706189319821, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1156554103393332, 1.0291278965521125, 0.7534660886246842))
ob.select_set(False)

# 305
ob = bpy.context.scene.objects[305]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.3523794759355807, 0, 4.366385717014934)
# rotation
bpy.ops.transform.rotate(value=0.6412652224754857, orient_axis='X')
bpy.ops.transform.rotate(value=3.0431269777468177, orient_axis='Y')
bpy.ops.transform.rotate(value=1.9876781353950068, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1770659163987875, 0.9475847516284353, 1.7894605906226995))
ob.select_set(False)

# 574
ob = bpy.context.scene.objects[574]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.9639379721243113, 0, -0.9259067842896695)
# rotation
bpy.ops.transform.rotate(value=0.9159242817782819, orient_axis='X')
bpy.ops.transform.rotate(value=2.76051163837311, orient_axis='Y')
bpy.ops.transform.rotate(value=2.487936925564982, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.4406141426738022, 1.1124127346885702, 0.9315117179930053))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 14.629147423153517
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_58.JPEG"
bpy.ops.render.render(write_still=True)


