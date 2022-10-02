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


# 259
ob = bpy.context.scene.objects[259]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.5254076935036203, 0, 4.473396577724689)
# rotation
bpy.ops.transform.rotate(value=1.746433230483599, orient_axis='X')
bpy.ops.transform.rotate(value=2.611521513651059, orient_axis='Y')
bpy.ops.transform.rotate(value=1.1579563726779434, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.3820418045384555, 0.9885486123007248, 0.1596904610382226))
ob.select_set(False)

# 597
ob = bpy.context.scene.objects[597]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.2482357424737494, 0, -4.0646030553669155)
# rotation
bpy.ops.transform.rotate(value=3.1260111739856216, orient_axis='X')
bpy.ops.transform.rotate(value=0.7099500334660458, orient_axis='Y')
bpy.ops.transform.rotate(value=1.581898765894587, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.8848916663805841, 1.2958688128332463, 0.3975372848388399))
ob.select_set(False)

# 118
ob = bpy.context.scene.objects[118]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.069473481735837, 0, -0.7358692650872292)
# rotation
bpy.ops.transform.rotate(value=2.5451988618529926, orient_axis='X')
bpy.ops.transform.rotate(value=2.94116381048881, orient_axis='Y')
bpy.ops.transform.rotate(value=1.3540293961154126, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9707497100972018, 0.08425731468531228, 1.4230691925300896))
ob.select_set(False)

# 616
ob = bpy.context.scene.objects[616]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.6567268379917586, 0, -4.489329483968134)
# rotation
bpy.ops.transform.rotate(value=2.2029365136091696, orient_axis='X')
bpy.ops.transform.rotate(value=2.030095949841406, orient_axis='Y')
bpy.ops.transform.rotate(value=0.6467217788465125, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.247696885677191, 0.9145444242666507, 1.052711035926542))
ob.select_set(False)

# 318
ob = bpy.context.scene.objects[318]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.6488306064501255, 0, -3.97865800781167)
# rotation
bpy.ops.transform.rotate(value=0.5437635405305821, orient_axis='X')
bpy.ops.transform.rotate(value=2.149588694542931, orient_axis='Y')
bpy.ops.transform.rotate(value=2.6949969579357806, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.7466292785735344, 1.3545346784568864, 1.2115177559344532))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 8.154029347050258
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_22.JPEG"
bpy.ops.render.render(write_still=True)


