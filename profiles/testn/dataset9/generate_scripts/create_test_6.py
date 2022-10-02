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


# 323
ob = bpy.context.scene.objects[323]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.6934120267912816, 0, -1.4817956891133335)
# rotation
bpy.ops.transform.rotate(value=3.070901001327767, orient_axis='X')
bpy.ops.transform.rotate(value=2.9710319840897297, orient_axis='Y')
bpy.ops.transform.rotate(value=0.395074723975143, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.85414955109755, 0.9165086796584829, 1.6735447409144575))
ob.select_set(False)

# 488
ob = bpy.context.scene.objects[488]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.0602074545228466, 0, -1.0119933440057416)
# rotation
bpy.ops.transform.rotate(value=1.3966271812682463, orient_axis='X')
bpy.ops.transform.rotate(value=2.43955454329206, orient_axis='Y')
bpy.ops.transform.rotate(value=1.6899267884421116, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.7496075108794575, 0.11059636361016989, 0.9777009086362769))
ob.select_set(False)

# 442
ob = bpy.context.scene.objects[442]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.6464234165723126, 0, 1.382921343640322)
# rotation
bpy.ops.transform.rotate(value=0.12422774586470407, orient_axis='X')
bpy.ops.transform.rotate(value=0.6615070592204428, orient_axis='Y')
bpy.ops.transform.rotate(value=1.3608183006781578, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6263924651697919, 1.4842345548735527, 1.2437808628930838))
ob.select_set(False)

# 299
ob = bpy.context.scene.objects[299]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.7838403547565065, 0, 4.194539380283576)
# rotation
bpy.ops.transform.rotate(value=0.6207282204084623, orient_axis='X')
bpy.ops.transform.rotate(value=2.3718635240295356, orient_axis='Y')
bpy.ops.transform.rotate(value=0.12522065075289665, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.6937843587904613, 0.9671380468449435, 1.9577073823935596))
ob.select_set(False)

# 367
ob = bpy.context.scene.objects[367]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.771461486884321, 0, -3.1996385519951005)
# rotation
bpy.ops.transform.rotate(value=2.3852821143070377, orient_axis='X')
bpy.ops.transform.rotate(value=1.171018302137237, orient_axis='Y')
bpy.ops.transform.rotate(value=2.830468853115723, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8137002184023048, 0.8208855294459714, 0.619170672408528))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 13.119136057603292
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_6.JPEG"
bpy.ops.render.render(write_still=True)


