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


# 46
ob = bpy.context.scene.objects[46]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.2442088477164441, 0, -2.805696934953136)
# rotation
bpy.ops.transform.rotate(value=1.5610162750471341, orient_axis='X')
bpy.ops.transform.rotate(value=2.477560510455067, orient_axis='Y')
bpy.ops.transform.rotate(value=0.4723215012581562, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9494408794530569, 1.2837257466823309, 0.7868096005282037))
ob.select_set(False)

# 253
ob = bpy.context.scene.objects[253]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.6039550576214703, 0, -3.580179136817228)
# rotation
bpy.ops.transform.rotate(value=1.0719032033469862, orient_axis='X')
bpy.ops.transform.rotate(value=2.6523115132873123, orient_axis='Y')
bpy.ops.transform.rotate(value=1.0580516317290238, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.8301439303997609, 0.06350318434383317, 1.4199185623158754))
ob.select_set(False)

# 358
ob = bpy.context.scene.objects[358]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.4846468208821455, 0, -3.2431774587325695)
# rotation
bpy.ops.transform.rotate(value=1.2922894143082908, orient_axis='X')
bpy.ops.transform.rotate(value=0.43888888089926936, orient_axis='Y')
bpy.ops.transform.rotate(value=2.872966830493328, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.7775399501399423, 1.8636413095019513, 0.359192400584569))
ob.select_set(False)

# 118
ob = bpy.context.scene.objects[118]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.5840628643032755, 0, -2.419032785067581)
# rotation
bpy.ops.transform.rotate(value=2.645629089015074, orient_axis='X')
bpy.ops.transform.rotate(value=1.1606098481621852, orient_axis='Y')
bpy.ops.transform.rotate(value=1.1456959126080883, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.3617237707466081, 1.8464090140763454, 0.32715081860866646))
ob.select_set(False)

# 79
ob = bpy.context.scene.objects[79]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.86822384309845, 0, -2.1885852765318328)
# rotation
bpy.ops.transform.rotate(value=0.21548706733683362, orient_axis='X')
bpy.ops.transform.rotate(value=1.4083122305098963, orient_axis='Y')
bpy.ops.transform.rotate(value=2.138011634436953, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9012767180668213, 0.9246487756417878, 0.8200190959535192))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 8.358840629104085
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "/code/profiles/x1/dataset10/images/scene_99.JPEG"
bpy.ops.render.render(write_still=True)


