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


# 315
ob = bpy.context.scene.objects[315]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.29601850873282043, 0, -1.5975615555829177)
# rotation
bpy.ops.transform.rotate(value=2.3029276694483913, orient_axis='X')
bpy.ops.transform.rotate(value=0.9308365220924618, orient_axis='Y')
bpy.ops.transform.rotate(value=0.4337192303806056, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.2060302295541339, 1.1064120237368547, 0.3096641153380457))
ob.select_set(False)

# 85
ob = bpy.context.scene.objects[85]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.8697591894706385, 0, -1.0496448695487253)
# rotation
bpy.ops.transform.rotate(value=0.05653956438118432, orient_axis='X')
bpy.ops.transform.rotate(value=2.020491698411332, orient_axis='Y')
bpy.ops.transform.rotate(value=1.80025083887483, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1115443920888644, 1.574424877003681, 0.9012717338366136))
ob.select_set(False)

# 343
ob = bpy.context.scene.objects[343]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.8108646245758324, 0, -3.849141744128878)
# rotation
bpy.ops.transform.rotate(value=0.769964972190465, orient_axis='X')
bpy.ops.transform.rotate(value=1.8772117200053275, orient_axis='Y')
bpy.ops.transform.rotate(value=2.9631896804947093, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.7862132163784403, 0.5639811834530255, 0.38934077104189657))
ob.select_set(False)

# 622
ob = bpy.context.scene.objects[622]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.851813731358439, 0, -2.8199305426019503)
# rotation
bpy.ops.transform.rotate(value=0.3459908548437804, orient_axis='X')
bpy.ops.transform.rotate(value=1.3383763134102462, orient_axis='Y')
bpy.ops.transform.rotate(value=0.8016908274456228, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.2774435244062263, 0.9976261411740537, 1.6532117258364751))
ob.select_set(False)

# 53
ob = bpy.context.scene.objects[53]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.343847379382482, 0, -0.20950453197161156)
# rotation
bpy.ops.transform.rotate(value=0.6594237080702651, orient_axis='X')
bpy.ops.transform.rotate(value=1.856761120977305, orient_axis='Y')
bpy.ops.transform.rotate(value=0.9479898167212315, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.4122137941040203, 0.8414709631733122, 1.5018450371984635))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 16.972304272948552
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_70.JPEG"
bpy.ops.render.render(write_still=True)


