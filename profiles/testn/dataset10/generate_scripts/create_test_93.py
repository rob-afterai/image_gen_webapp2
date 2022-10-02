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


# 422
ob = bpy.context.scene.objects[422]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.07540169807457, 0, 0.8443918004681858)
# rotation
bpy.ops.transform.rotate(value=0.5319678779819981, orient_axis='X')
bpy.ops.transform.rotate(value=2.198023085684481, orient_axis='Y')
bpy.ops.transform.rotate(value=0.14797499501959693, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.4561332233432593, 0.5156322436541885, 1.9180801597142498))
ob.select_set(False)

# 479
ob = bpy.context.scene.objects[479]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.781740759056288, 0, -1.7647058153891866)
# rotation
bpy.ops.transform.rotate(value=1.7915942748926479, orient_axis='X')
bpy.ops.transform.rotate(value=2.2563451303778947, orient_axis='Y')
bpy.ops.transform.rotate(value=0.622676959916468, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.17350138267554005, 1.443755797122041, 1.2159245667527678))
ob.select_set(False)

# 279
ob = bpy.context.scene.objects[279]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.7531675837838501, 0, -1.8286283512591903)
# rotation
bpy.ops.transform.rotate(value=1.6497381943920095, orient_axis='X')
bpy.ops.transform.rotate(value=1.279819056197471, orient_axis='Y')
bpy.ops.transform.rotate(value=1.690712524219543, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1490705118729831, 1.0245173170529762, 1.9781784458562826))
ob.select_set(False)

# 217
ob = bpy.context.scene.objects[217]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.7364330710821, 0, 3.380809967990677)
# rotation
bpy.ops.transform.rotate(value=1.9658144378105913, orient_axis='X')
bpy.ops.transform.rotate(value=1.4540646246205382, orient_axis='Y')
bpy.ops.transform.rotate(value=1.017626600836694, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.104260552966882, 1.7150808989810176, 0.8579280049949876))
ob.select_set(False)

# 457
ob = bpy.context.scene.objects[457]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.9968437019117005, 0, 4.001482049674939)
# rotation
bpy.ops.transform.rotate(value=1.3335923100657494, orient_axis='X')
bpy.ops.transform.rotate(value=2.44330338584302, orient_axis='Y')
bpy.ops.transform.rotate(value=2.755778910695634, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9504598076053266, 1.849619913296686, 0.18246033905060433))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 10.70115216913376
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_93.JPEG"
bpy.ops.render.render(write_still=True)


