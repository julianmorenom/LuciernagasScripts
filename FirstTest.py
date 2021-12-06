import bpy

bpy.ops.mesh.primitive_cube_add()
selObj = bpy.context.active_object

# move it
selObj.location[1] = 5 