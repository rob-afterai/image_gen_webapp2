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


# 373
ob = bpy.context.scene.objects[373]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.9953738417641311, 0, 4.1516754715237365)
# rotation
bpy.ops.transform.rotate(value=2.370713859274711, orient_axis='X')
bpy.ops.transform.rotate(value=1.0044796922689783, orient_axis='Y')
bpy.ops.transform.rotate(value=1.0427478637967453, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.2908589507801573, 1.300826470228117, 1.4691133317626905))
ob.select_set(False)

# 516
ob = bpy.context.scene.objects[516]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.0958905717801954, 0, -1.6366620880463625)
# rotation
bpy.ops.transform.rotate(value=2.3930882352236416, orient_axis='X')
bpy.ops.transform.rotate(value=1.695707045795609, orient_axis='Y')
bpy.ops.transform.rotate(value=1.9191597397915878, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.48923680477163733, 1.968174446464649, 1.2658774223717104))
ob.select_set(False)

# 359
ob = bpy.context.scene.objects[359]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.1930628851207334, 0, 2.3116418453356635)
# rotation
bpy.ops.transform.rotate(value=2.5046128429159538, orient_axis='X')
bpy.ops.transform.rotate(value=0.41370983435754827, orient_axis='Y')
bpy.ops.transform.rotate(value=0.5526674938082785, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1014367849927102, 1.7979090912848534, 0.181035655064967))
ob.select_set(False)

# 165
ob = bpy.context.scene.objects[165]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.628105280279426, 0, -3.767681235886124)
# rotation
bpy.ops.transform.rotate(value=2.1685475879272493, orient_axis='X')
bpy.ops.transform.rotate(value=0.677841439265402, orient_axis='Y')
bpy.ops.transform.rotate(value=2.071874140518493, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.5318014916913885, 0.8685950465941474, 1.8819675899769557))
ob.select_set(False)

# 448
ob = bpy.context.scene.objects[448]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.005896001358725, 0, 3.4683916561877925)
# rotation
bpy.ops.transform.rotate(value=0.6648516451831074, orient_axis='X')
bpy.ops.transform.rotate(value=1.874268868826962, orient_axis='Y')
bpy.ops.transform.rotate(value=2.8243676854134647, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.5200639664240567, 0.3961493447316473, 1.981541360723711))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 9.846662840075833
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_84.JPEG"
bpy.ops.render.render(write_still=True)


