# recreate the lorenz attractor
import bpy
import random

# declare constant variables of the lorenz attractor
a = 10
b = 28
c = 8/3 
time = 0.01

# grab the array objects and distribute them
spheresList = bpy.data.collections['Spheres'].objects
for sphere in spheresList:
    # grab the initial position
    x = sphere.location.x
    y = sphere.location.y
    z = sphere.location.z
    # define x, y and z with random start number
    # x = random.random()
    # y = random.random() 
    # z = random.random()
    sphere.location =[x, y, z]
    # movement description formulas implementation every 2 frames
    # range is the number fo frames 
    for count in range (1000):
        count += 1
        mvm1 = (a *(y - x))* time
        mvm2 = (x * (b - z) - y)* time
        mvm3 = (x * y - c * z)* time
        x += mvm1
        y += mvm2
        z += mvm3
        sphere.location = [x, y, z]
        sphere.keyframe_insert(data_path = "location", frame = count*2)