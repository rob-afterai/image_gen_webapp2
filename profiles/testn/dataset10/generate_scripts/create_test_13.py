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


# 405
ob = bpy.context.scene.objects[405]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.601387761509094, 0, -3.810232586355992)
# rotation
bpy.ops.transform.rotate(value=3.067037528511232, orient_axis='X')
bpy.ops.transform.rotate(value=0.707461320544327, orient_axis='Y')
bpy.ops.transform.rotate(value=2.5959230590845985, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9964230083477466, 1.9553700833202583, 1.5666106500732841))
ob.select_set(False)

# 581
ob = bpy.context.scene.objects[581]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.3510498655865533, 0, 3.4082626995406757)
# rotation
bpy.ops.transform.rotate(value=2.832644890776056, orient_axis='X')
bpy.ops.transform.rotate(value=0.6583982752244919, orient_axis='Y')
bpy.ops.transform.rotate(value=1.1856717221215172, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.8446039391984639, 0.2815418521216706, 1.4875373868827186))
ob.select_set(False)

# 545
ob = bpy.context.scene.objects[545]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (2.041101612135349, 0, -2.062586391938313)
# rotation
bpy.ops.transform.rotate(value=0.9312227487678143, orient_axis='X')
bpy.ops.transform.rotate(value=1.9253206108051968, orient_axis='Y')
bpy.ops.transform.rotate(value=1.1263531851485733, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.961121635322548, 1.686996752648799, 1.3310428820810865))
ob.select_set(False)

# 286
ob = bpy.context.scene.objects[286]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.5658804278546956, 0, -4.372428421025458)
# rotation
bpy.ops.transform.rotate(value=0.14239862826181504, orient_axis='X')
bpy.ops.transform.rotate(value=2.9977576750971133, orient_axis='Y')
bpy.ops.transform.rotate(value=2.9074146264279435, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.6796280215970643, 1.0243090190426491, 0.042463417983181095))
ob.select_set(False)

# 76
ob = bpy.context.scene.objects[76]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-0.25340518183926797, 0, 0.1382908305478523)
# rotation
bpy.ops.transform.rotate(value=0.6071040873383824, orient_axis='X')
bpy.ops.transform.rotate(value=2.1630970499256064, orient_axis='Y')
bpy.ops.transform.rotate(value=0.07743250134859814, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.9769017604979375, 0.03104957349962345, 1.5214853232868075))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 0.8858867699491713
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_13.JPEG"
bpy.ops.render.render(write_still=True)


