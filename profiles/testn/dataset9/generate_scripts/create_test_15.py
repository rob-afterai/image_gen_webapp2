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


# 450
ob = bpy.context.scene.objects[450]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.7659728141992317, 0, -0.8884929219970159)
# rotation
bpy.ops.transform.rotate(value=0.517458149715405, orient_axis='X')
bpy.ops.transform.rotate(value=0.20130672556901463, orient_axis='Y')
bpy.ops.transform.rotate(value=0.540768384874863, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.4703211319377874, 1.3954221021863646, 0.26264120137964575))
ob.select_set(False)

# 209
ob = bpy.context.scene.objects[209]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.1690887143838218, 0, -0.49660272398726146)
# rotation
bpy.ops.transform.rotate(value=1.7070164601047229, orient_axis='X')
bpy.ops.transform.rotate(value=2.591717332006486, orient_axis='Y')
bpy.ops.transform.rotate(value=0.8705311953715894, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.507695633637891, 0.4621580299378112, 0.0533716483217368))
ob.select_set(False)

# 458
ob = bpy.context.scene.objects[458]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.7397721280356526, 0, -0.3622393902762724)
# rotation
bpy.ops.transform.rotate(value=1.5976457539928088, orient_axis='X')
bpy.ops.transform.rotate(value=0.7015232809233872, orient_axis='Y')
bpy.ops.transform.rotate(value=0.9868886814698278, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.5912118563002526, 0.09048465456721555, 0.37838920803198817))
ob.select_set(False)

# 32
ob = bpy.context.scene.objects[32]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (4.482347135840641, 0, -1.2107529195527866)
# rotation
bpy.ops.transform.rotate(value=2.917301807461434, orient_axis='X')
bpy.ops.transform.rotate(value=2.7568226357389296, orient_axis='Y')
bpy.ops.transform.rotate(value=0.1694930674375903, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9880749055033307, 1.5842888546467313, 0.7343362902468211))
ob.select_set(False)

# 544
ob = bpy.context.scene.objects[544]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.099801649641255, 0, -3.350386962477389)
# rotation
bpy.ops.transform.rotate(value=1.0851772517056537, orient_axis='X')
bpy.ops.transform.rotate(value=0.6273722542397036, orient_axis='Y')
bpy.ops.transform.rotate(value=1.5419169292191417, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.2622013871755362, 1.4158360481230328, 0.03625086939441413))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 9.111945357640298
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_15.JPEG"
bpy.ops.render.render(write_still=True)


