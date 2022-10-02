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


# 297
ob = bpy.context.scene.objects[297]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (1.6018842028109317, 0, 0.18989695130778905)
# rotation
bpy.ops.transform.rotate(value=1.6632775149134698, orient_axis='X')
bpy.ops.transform.rotate(value=1.7957749488431778, orient_axis='Y')
bpy.ops.transform.rotate(value=0.43943841729501315, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.3448663826904512, 1.6371615064007332, 0.2243180052808711))
ob.select_set(False)

# 322
ob = bpy.context.scene.objects[322]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (3.950206893032533, 0, 3.6122540431355503)
# rotation
bpy.ops.transform.rotate(value=1.5562197661189403, orient_axis='X')
bpy.ops.transform.rotate(value=2.5293748254562733, orient_axis='Y')
bpy.ops.transform.rotate(value=2.815964955628665, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.253840768286748, 1.3691075915646203, 1.4599945390543358))
ob.select_set(False)

# 462
ob = bpy.context.scene.objects[462]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.1401332588379134, 0, -0.1615568642035754)
# rotation
bpy.ops.transform.rotate(value=0.35706569042487385, orient_axis='X')
bpy.ops.transform.rotate(value=2.5036400251793647, orient_axis='Y')
bpy.ops.transform.rotate(value=2.007780873835132, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.0110091621200235, 0.3419303767644293, 0.9258367094892925))
ob.select_set(False)

# 584
ob = bpy.context.scene.objects[584]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.153538433375155, 0, 2.316498585442667)
# rotation
bpy.ops.transform.rotate(value=1.5139894920193095, orient_axis='X')
bpy.ops.transform.rotate(value=1.70132779351641, orient_axis='Y')
bpy.ops.transform.rotate(value=2.2129160751302006, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.369156700467388, 0.21693075378889604, 0.037973907809371044))
ob.select_set(False)

# 449
ob = bpy.context.scene.objects[449]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-4.35187043365233, 0, -1.276676297274633)
# rotation
bpy.ops.transform.rotate(value=0.517078351676566, orient_axis='X')
bpy.ops.transform.rotate(value=2.5587911745879994, orient_axis='Y')
bpy.ops.transform.rotate(value=2.5501266842801216, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.8782082646382026, 1.206902778771065, 1.9647541495202592))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 1.2081158059393715
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset9\\images\scene_12.JPEG"
bpy.ops.render.render(write_still=True)


