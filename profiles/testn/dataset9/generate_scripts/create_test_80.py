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


# 163
ob = bpy.context.scene.objects[163]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.0601451654761131, 0, -1.3478479972581137)
# rotation
bpy.ops.transform.rotate(value=2.6724949098587003, orient_axis='X')
bpy.ops.transform.rotate(value=0.3900316365060513, orient_axis='Y')
bpy.ops.transform.rotate(value=2.5510284839057973, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.047710480772419, 1.8887964433943512, 1.4225535839219008))
ob.select_set(False)

# 1
ob = bpy.context.scene.objects[1]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.120943114380269, 0, 2.1555582267671376)
# rotation
bpy.ops.transform.rotate(value=0.08423231204681039, orient_axis='X')
bpy.ops.transform.rotate(value=2.542069059357257, orient_axis='Y')
bpy.ops.transform.rotate(value=1.8535161261158792, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6142588539618226, 1.830211918697978, 1.844955816412943))
ob.select_set(False)

# 619
ob = bpy.context.scene.objects[619]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.47307066801150555, 0, -3.130732362116101)
# rotation
bpy.ops.transform.rotate(value=1.3142669963492442, orient_axis='X')
bpy.ops.transform.rotate(value=0.6460309915805638, orient_axis='Y')
bpy.ops.transform.rotate(value=2.957076006380866, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.7706500318040639, 1.1416653493146522, 1.9699239685492984))
ob.select_set(False)

# 232
ob = bpy.context.scene.objects[232]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.6264461373690358, 0, -1.368234557356252)
# rotation
bpy.ops.transform.rotate(value=2.309619361194158, orient_axis='X')
bpy.ops.transform.rotate(value=0.710081054743542, orient_axis='Y')
bpy.ops.transform.rotate(value=2.9803695285496445, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.6257390631248303, 0.9601787593880675, 0.16897004900737222))
ob.select_set(False)

# 89
ob = bpy.context.scene.objects[89]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.9147886000157968, 0, 0.6975758140234065)
# rotation
bpy.ops.transform.rotate(value=2.3106394841733873, orient_axis='X')
bpy.ops.transform.rotate(value=2.514979016750916, orient_axis='Y')
bpy.ops.transform.rotate(value=2.6203864095276312, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.873190663681352, 1.1386007067663266, 0.8812731493748218))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 4.859985541946788
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_80.JPEG"
bpy.ops.render.render(write_still=True)


