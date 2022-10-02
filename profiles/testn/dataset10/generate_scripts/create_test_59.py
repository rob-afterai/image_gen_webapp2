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


# 288
ob = bpy.context.scene.objects[288]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.2530294395207147, 0, 1.4336801343687418)
# rotation
bpy.ops.transform.rotate(value=1.6496060599143747, orient_axis='X')
bpy.ops.transform.rotate(value=0.8869839143804351, orient_axis='Y')
bpy.ops.transform.rotate(value=1.7687037585265228, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.750432690576382, 0.7565224278171567, 0.7009992942225305))
ob.select_set(False)

# 310
ob = bpy.context.scene.objects[310]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.9902830960530045, 0, -1.0120757050554428)
# rotation
bpy.ops.transform.rotate(value=3.103626561327996, orient_axis='X')
bpy.ops.transform.rotate(value=1.6021918974465688, orient_axis='Y')
bpy.ops.transform.rotate(value=1.258212983319064, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6679296269930894, 0.5237950612188149, 1.8896304028366666))
ob.select_set(False)

# 528
ob = bpy.context.scene.objects[528]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.32641639515925736, 0, 3.019435450980491)
# rotation
bpy.ops.transform.rotate(value=0.6234723350447603, orient_axis='X')
bpy.ops.transform.rotate(value=1.3115356733796188, orient_axis='Y')
bpy.ops.transform.rotate(value=0.6654580246238991, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.9878678712895583, 0.8317023347931218, 0.7747611093278584))
ob.select_set(False)

# 203
ob = bpy.context.scene.objects[203]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.9134215588801675, 0, 0.929010344756227)
# rotation
bpy.ops.transform.rotate(value=2.9314034292270716, orient_axis='X')
bpy.ops.transform.rotate(value=0.5314025410800618, orient_axis='Y')
bpy.ops.transform.rotate(value=2.415505586281684, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.9712660368265933, 0.4506875443386258, 1.6459090752819214))
ob.select_set(False)

# 449
ob = bpy.context.scene.objects[449]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.140461737655658, 0, -0.4761072322016311)
# rotation
bpy.ops.transform.rotate(value=2.22511951075471, orient_axis='X')
bpy.ops.transform.rotate(value=1.6595368107482877, orient_axis='Y')
bpy.ops.transform.rotate(value=0.23400240943870687, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.957611733540063, 1.4506842095718415, 0.1283083123024773))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 9.917072507157126
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_59.JPEG"
bpy.ops.render.render(write_still=True)


