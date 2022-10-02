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


# 564
ob = bpy.context.scene.objects[564]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.731251565740512, 0, -0.5585310837237456)
# rotation
bpy.ops.transform.rotate(value=2.136034272043765, orient_axis='X')
bpy.ops.transform.rotate(value=2.591814894800561, orient_axis='Y')
bpy.ops.transform.rotate(value=2.0724563561687033, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.06814107005270431, 0.6952256661368332, 1.2165035411282599))
ob.select_set(False)

# 501
ob = bpy.context.scene.objects[501]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.763968667925035, 0, -1.0790059540800265)
# rotation
bpy.ops.transform.rotate(value=2.2544710632177503, orient_axis='X')
bpy.ops.transform.rotate(value=3.085240664727219, orient_axis='Y')
bpy.ops.transform.rotate(value=2.330352661313108, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.957084637496315, 1.739814375339409, 1.362817646599212))
ob.select_set(False)

# 193
ob = bpy.context.scene.objects[193]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.633701104189589, 0, -1.7230321644199011)
# rotation
bpy.ops.transform.rotate(value=0.4683180606406114, orient_axis='X')
bpy.ops.transform.rotate(value=0.13884603763352363, orient_axis='Y')
bpy.ops.transform.rotate(value=1.6479495317345423, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.058876202394564814, 1.382841016815693, 0.9652898374649921))
ob.select_set(False)

# 133
ob = bpy.context.scene.objects[133]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.5581673305688817, 0, -2.557980733101542)
# rotation
bpy.ops.transform.rotate(value=0.751234443175686, orient_axis='X')
bpy.ops.transform.rotate(value=0.6625732260201129, orient_axis='Y')
bpy.ops.transform.rotate(value=0.8457026676173837, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.1247116470451366, 0.7004443952982828, 0.09590017393074435))
ob.select_set(False)

# 584
ob = bpy.context.scene.objects[584]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.027188574204402904, 0, -4.443005742541236)
# rotation
bpy.ops.transform.rotate(value=1.6209770167399205, orient_axis='X')
bpy.ops.transform.rotate(value=0.145375804931449, orient_axis='Y')
bpy.ops.transform.rotate(value=0.7260440181892127, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.14741803079424787, 0.6764587327362053, 0.9863093924506587))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 17.710545055755837
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_47.JPEG"
bpy.ops.render.render(write_still=True)


