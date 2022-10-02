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


# 455
ob = bpy.context.scene.objects[455]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.535312207520886, 0, -3.1411509589538102)
# rotation
bpy.ops.transform.rotate(value=2.8799929494027667, orient_axis='X')
bpy.ops.transform.rotate(value=0.4340069508557982, orient_axis='Y')
bpy.ops.transform.rotate(value=0.18738123775917373, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8744833511235428, 1.243049931789245, 0.588830027919941))
ob.select_set(False)

# 605
ob = bpy.context.scene.objects[605]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.5241566561242186, 0, -2.1315795898222367)
# rotation
bpy.ops.transform.rotate(value=2.8757613662684736, orient_axis='X')
bpy.ops.transform.rotate(value=2.6409080608318556, orient_axis='Y')
bpy.ops.transform.rotate(value=2.7932493306028663, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1273495731500691, 1.1530555779196523, 0.8413848029955346))
ob.select_set(False)

# 182
ob = bpy.context.scene.objects[182]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.4111452226302807, 0, -2.9754376138091323)
# rotation
bpy.ops.transform.rotate(value=1.6439521493256317, orient_axis='X')
bpy.ops.transform.rotate(value=2.9174361533318356, orient_axis='Y')
bpy.ops.transform.rotate(value=0.325962286382986, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9503280611139502, 1.6693270669721905, 1.3902601708163902))
ob.select_set(False)

# 376
ob = bpy.context.scene.objects[376]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.4876203061875302, 0, -3.407069410633083)
# rotation
bpy.ops.transform.rotate(value=1.7054829517469294, orient_axis='X')
bpy.ops.transform.rotate(value=2.216921704408006, orient_axis='Y')
bpy.ops.transform.rotate(value=2.2803259459462604, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.036399458187642564, 1.8038935284548874, 1.6835908260743873))
ob.select_set(False)

# 46
ob = bpy.context.scene.objects[46]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.9581662649287415, 0, 2.220037711507592)
# rotation
bpy.ops.transform.rotate(value=2.6047862915954685, orient_axis='X')
bpy.ops.transform.rotate(value=1.5450467596011228, orient_axis='Y')
bpy.ops.transform.rotate(value=2.577902694529617, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9803258636837435, 0.22233124250148517, 1.3515445060792846))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 18.91675487406566
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_72.JPEG"
bpy.ops.render.render(write_still=True)


