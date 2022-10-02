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


# 99
ob = bpy.context.scene.objects[99]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.338236483227296, 0, -3.7818320564849834)
# rotation
bpy.ops.transform.rotate(value=1.956968344075606, orient_axis='X')
bpy.ops.transform.rotate(value=0.44763080169492886, orient_axis='Y')
bpy.ops.transform.rotate(value=1.1092605662703154, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.631755224386657, 1.7088505950491013, 0.5500336532232628))
ob.select_set(False)

# 147
ob = bpy.context.scene.objects[147]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.6937629872496953, 0, 0.19582750531564308)
# rotation
bpy.ops.transform.rotate(value=0.7098643441791984, orient_axis='X')
bpy.ops.transform.rotate(value=2.828856330479191, orient_axis='Y')
bpy.ops.transform.rotate(value=2.541310059268547, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.3524472272057173, 0.8522422560943406, 1.6317764966852861))
ob.select_set(False)

# 79
ob = bpy.context.scene.objects[79]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.7592499695967514, 0, -3.1618731165655443)
# rotation
bpy.ops.transform.rotate(value=1.1189173154246135, orient_axis='X')
bpy.ops.transform.rotate(value=0.9744381774765766, orient_axis='Y')
bpy.ops.transform.rotate(value=2.006824164547634, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.3384996878845392, 0.928092687308357, 1.8455255318880592))
ob.select_set(False)

# 424
ob = bpy.context.scene.objects[424]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.4221353554760228, 0, -2.874373902963533)
# rotation
bpy.ops.transform.rotate(value=0.12809013487959894, orient_axis='X')
bpy.ops.transform.rotate(value=0.9647512822593813, orient_axis='Y')
bpy.ops.transform.rotate(value=2.766399327199579, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.7969788085047855, 0.36698860943921474, 0.9465647128082031))
ob.select_set(False)

# 156
ob = bpy.context.scene.objects[156]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.41112656488931876, 0, -4.4959096216557475)
# rotation
bpy.ops.transform.rotate(value=2.5329834354358036, orient_axis='X')
bpy.ops.transform.rotate(value=0.7242196658725221, orient_axis='Y')
bpy.ops.transform.rotate(value=1.2453476185221988, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.4027867689357869, 0.4987406777392629, 0.8262487786519521))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 4.542596519881135
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_37.JPEG"
bpy.ops.render.render(write_still=True)


