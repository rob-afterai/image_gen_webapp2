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


# 624
ob = bpy.context.scene.objects[624]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.9982177374052084, 0, 2.9468853880488677)
# rotation
bpy.ops.transform.rotate(value=2.831524620981039, orient_axis='X')
bpy.ops.transform.rotate(value=1.5207273272769144, orient_axis='Y')
bpy.ops.transform.rotate(value=0.21850235001030213, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.9732948400379393, 0.969816688547062, 1.5164320441834827))
ob.select_set(False)

# 25
ob = bpy.context.scene.objects[25]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-2.953911418082134, 0, -3.5048213664671315)
# rotation
bpy.ops.transform.rotate(value=0.6571642352212268, orient_axis='X')
bpy.ops.transform.rotate(value=2.8405901870790697, orient_axis='Y')
bpy.ops.transform.rotate(value=2.9250074523720184, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.1649076155992324, 1.309617257879238, 0.7090395272404553))
ob.select_set(False)

# 389
ob = bpy.context.scene.objects[389]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (0.8298216447197273, 0, 4.151753602899888)
# rotation
bpy.ops.transform.rotate(value=2.2134899029928836, orient_axis='X')
bpy.ops.transform.rotate(value=1.8136896174391188, orient_axis='Y')
bpy.ops.transform.rotate(value=0.8713788495570297, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.6775186182627986, 1.2485176823158222, 0.23240706398377187))
ob.select_set(False)

# 17
ob = bpy.context.scene.objects[17]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-1.4878223900988736, 0, 3.109906851645137)
# rotation
bpy.ops.transform.rotate(value=2.160963718408891, orient_axis='X')
bpy.ops.transform.rotate(value=1.1724716860038902, orient_axis='Y')
bpy.ops.transform.rotate(value=2.4172897240104803, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(0.14963215313487233, 1.415874177267723, 0.2560341056258584))
ob.select_set(False)

# 287
ob = bpy.context.scene.objects[287]
# unhide
ob.hide_set(False)
ob.hide_render = False
ob.select_set(True)
# location
ob.location = (-3.9624885376743433, 0, -4.146134315335303)
# rotation
bpy.ops.transform.rotate(value=2.0855446364083137, orient_axis='X')
bpy.ops.transform.rotate(value=0.7652554230745588, orient_axis='Y')
bpy.ops.transform.rotate(value=1.9213290373090792, orient_axis='Z')
# scale
bpy.ops.transform.resize(value=(1.426797895320676, 1.5805682047095095, 1.3936378290944982))
ob.select_set(False)

bpy.context.scene.eevee.gtao_factor = 15.962064069309797
bpy.context.scene.render.image_settings.file_format = 'JPEG'
# render
bpy.context.scene.render.filepath = "C:\\Users\\RMSmi\\Documents\\docker\\django-website\\image_gen_website\\profiles\\testn\\dataset10\\images\scene_69.JPEG"
bpy.ops.render.render(write_still=True)


