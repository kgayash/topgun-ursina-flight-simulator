from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from math import radians, sin, cos
from ursina import collider


# Initialize the Ursina application
# app = Ursina()

app = Ursina(size=(1700, 1000))  # Set the window size to 800x600


# sky = Sky(model = 'plane', scale = (2000,2000,2000), position =  (0,0,0))

ah = Entity(model = 'plane', texture = '66eEH.png', scale = (2), position = (0,0,0))
# ah.rotation_z = 90
# ah.rotation_y = 90
ah.rotation_x = -90

# water = Entity(model='plane', scale=(400, 400, 400), position=(0, -15, 0), texture='water', color = color.blue, collider='box')


# clouds = Clouds()

# Create a white cube (player character)

# runway = Entity(model='plane', scale=(140, 140, 140), texture="capture.JPG", position=(0, 1, 0), collider='box')

# runway.rotation_y = 180

# runway.rotation_y = 90 

# globe = Entity(model='sphere', scale=(10000), texture = 'My1nT')

# runway = Entity(model='plane', scale=(5, 1000, 5), color=color.black, position=(0, 0, 0), collider='box')
# runway.rotation_y = 90  # Rotate to make it run east-west

# # Create taxiways (smaller path sections for planes to move)
# taxiway1 = Entity(model='plane', scale=(5, 200, 5), color=color.black, position=(20, 0, -50), collider='box')
# taxiway2 = Entity(model='plane', scale=(5, 200, 5), color=color.black, position=(-20, 0, -150), collider='box')

# # Create terminals (large rectangular building-like entities)
# terminal = Entity(model='cube', scale=(20, 6, 20), color=color.blue, position=(0, 3, 100))
# terminal2 = Entity(model='cube', scale=(20, 6, 20), color=color.blue, position=(100, 3, -100))

# # Create a control tower (simple cylindrical entity)
# control_tower = Entity(model='cylinder', scale=(1, 10, 1), color=color.white, position=(50, 5, 50))

# # Create parking spots (rectangular entities)
# parking_spots = []
# for i in range(5):
#     parking_spot = Entity(model='cube', scale=(5, 0.2, 5), color=color.green, position=(i * 15 - 25, 0.1, 100))
#     parking_spots.append(parking_spot)


# # Create the main body of the airplane (fuselage)
# fuselage = Entity(model='cube', color=color.gray, scale=(2, 0.6, 8), position=(0, 0, 0))

# # Create the wings (left and right wings)
# left_wing = Entity(model='cube', color=color.blue, scale=(6, 0.2, 2), position=(-3, 0, 0))
# right_wing = Entity(model='cube', color=color.blue, scale=(6, 0.2, 2), position=(3, 0, 0))

# # Create the tail wing (horizontal stabilizer) - properly connected to the fuselage
# tail_wing = Entity(model='cube', color=color.red, scale=(3, 0.3, 1), position   =(0, 0.5, 4))  # Tail wing connected to fuselage

# # Create the vertical stabilizer (rudder) - properly connected to the tail
# vertical_stabilizer = Entity(model='cube', color=color.red, scale=(1, 2, 1), position=(0, 1.25, 5))  # Rudder connected

# # Create the engines (two small cylinders representing engines)
# engine_left = Entity(model='cylinder', color=color.orange, scale=(0.5, 0.5, 1.5), position=(-3, 0.3, -4))
# engine_right = Entity(model='cylinder', color=color.orange, scale=(0.5, 0.5, 1.5), position=(3, 0.3, -4))

# # Create the nose cone (small cone at the front)
# nose_cone = Entity(model='cone', color=color.green, scale=(0.7, 0.7, 1), position=(0, 0, -8))

# # Create the landing gear (simple cylinders for wheels)
# # landing_gear_front = Entity(model='cylinder', color=color.black, scale=(0.4, 0.4, 1), position=(0, -0.2, 3.5))
# # landing_gear_left = Entity(model='cylinder', color=color.black, scale=(0.4, 0.4, 0.5), position=(-2, -0.2, 4.5))
# # landing_gear_right = Entity(model='cylinder', color=color.black, scale=(0.4, 0.4, 0.5), position=(2, -0.2, 4.5))

# front_landing_gear = Entity(model='cylinder', color=color.yellow, scale=(10, 10, 1), position=(0, -1.0, 3.5))  # Adjusted Y position
# left_landing_gear = Entity(model='cylinder', color=color.yellow, scale=(10, 10, 0.5), position=(-1.5, -1.0, 3))  # Adjusted Y position
# right_landing_gear = Entity(model='cylinder', color=color.yellow, scale=(10, 10, 0.5), position=(1.5, -1.0, 3))  # Adjusted Y position

propeller_blade1 = Entity(
    model='cube', color=color.yellow, scale=(0.2, 2, 0.05), position=(0, 0, 0), rotation=(0, 0, 0)
)
propeller_blade2 = Entity(
    model='cube', color=color.yellow, scale=(0.2, 2, 0.05), position=(0, 0, 0), rotation=(90, 0, 0)
)
# # propeller_blade3 = Entity(
# #     model='cube', color=color.yellow, scale=(0.2, 3, 0.05), position=(0, 0, 0), rotation=(-120, 0, 0)
# )

# # Parent the propeller blades to the fuselage (plane body)


propeller = Entity(parent=scene, position = (0,0,-4.49))
propeller_blade1.parent = propeller
propeller_blade2.parent = propeller
# propeller_blade3.parent = propeller

# propeller.rotation_y = 90
# propeller.parent = cube
# fuselage.parent = cube
# left_wing.parent = cube
# right_wing.parent = cube
# tail_wing.parent = cube
# vertical_stabilizer.parent = cube
# engine_left.parent = cube
# nose_cone.parent = cube
# front_landing_gear.parent = cube
# left_landing_gear.parent = cube
# right_landing_gear.parent = cube

# f35_body = load_model('f35body.glb')
# f35body_entity = Entity(model=f35_body, position=(0,10,0), scale=(0.07,0.07,0.07))

# f35_lg = load_model('f35lgears')
# f35lg_entity = Entity(model=f35_lg)

# cube = Entity(parent=scene, position = (0,10,0), scale=(0.07,0.07,0.07), collider = 'box')

# f35body_entity.parent = cube
# f35lg_entity.parent = cube

f35 = load_model('f35_fixed.glb')

f35up = load_model('f35landinggear_fixed4.glb')

hg_carrier = load_model('gerald_ford_aircraft_carrier.glb')

hg_entity = Entity(model=hg_carrier, scale = (0.1,0.1,0.1))

# missile1 = Entity(model = 'cube', color = color.yellow, scale = (0.2,0.2,3), position = (0,16.5,11))
# missile2 = Entity(model = 'cube', color = color.yellow, scale = (0.2,0.2,3), position = (0,16.5,-11))


# f35gears = load_model('f35landinggear_fixed.glb')

# lg = Entity(model=f35gears, position = (-14.9,7,5), scale=(1, 1, 1))

# lg.rotation_y = -90

# f35.parent = y




# f35_entity = Entity(model=f35, position = (-6,15,6), scale=(0.3,0.3,0.3))
# f35_entity2 = Entity(model=f35, position = (-6,15,8), scale=(0.5,0.5,0.5))


cube = Entity(model=f35, position = (0,16.5,0), scale=(0.84, 0.84, 0.84), collider='box')
# cube = Entity()
# f35.parent = cube
# missile1.parent = cube
# missile2.parent = cube
# missile1.rotation_y = 90
# missile1.rotation_y = 90


cube.rotation_y = 180

# cube.collider = 'box'  # Simple box collider around the plane
# hg_entity.collider = 'box'  # Simple box collider around the second model

# # Add gravity or physics if needed (optional, depending on your setup)
# cube.add_component(Rigidbody)  # For physics-based objects (like falling)
# hg_carrier.add_component(Physics)  # For the second object

cube2 = Entity(model='f35', color=color.white, position = (-12,16.5,10), scale=(0.14, 0.14, 0.14), collider='box')
cube3 = Entity(model='f35', color=color.white, position = (-14.3,16.5,25), scale=(0.14, 0.14, 0.14), collider='box')
cube4 = Entity(model='f35', color=color.white, position = (-16.6,16.5,40), scale=(0.14, 0.14, 0.14), collider='box')
cube5 = Entity(model='f35', color=color.white, position = (-18.9,16.5,55), scale=(0.14, 0.14, 0.14), collider='box')
cube6 = Entity(model='f35', color=color.white, position = (-21.2,16.55,70), scale=(0.14, 0.14, 0.14), collider='box')

cube2.rotation_y = 30
cube3.rotation_y = 30

cube4.rotation_y = 30
cube5.rotation_y = 30
cube6.rotation_y = 30


cube7 = Entity(model='f35', color=color.white, position = (-52,16.5,-100), scale=(0.14, 0.14, 0.14), collider='box')
cube8 = Entity(model='f35', color=color.white, position = (-48.7,16.5,-120), scale=(0.14, 0.14, 0.14), collider='box')
# cube9 = Entity(model='f35', color=color.white, position = (-45,16.5,-120), scale=(0.14, 0.14, 0.14), collider='box')
# cube9 = Entity(model='f35', color=color.white, position = (-55,16.5,30), scale=(0.14, 0.14, 0.14), collider='box')
cube10 = Entity(model='f35', color=color.white, position = (-52,16.5,-85), scale=(0.14, 0.14, 0.14), collider='box')
cube13 = Entity(model='f35', color=color.white, position = (-52,16.5,-70), scale=(0.14, 0.14, 0.14), collider='box')

# cube11 = Entity(model='f35', color=color.white, position = (47,16.5,148), scale=(0.14, 0.14, 0.14), collider='box')
# cube12 = Entity(model='f35', color=color.white, position = (47,16.5,166), scale=(0.14, 0.14, 0.14), collider='box')

cube14 = Entity(model='f35', color=color.white, position = (-52,16.5,-30), scale=(0.14, 0.14, 0.14), collider='box')
cube15 = Entity(model='f35', color=color.white, position = (-52,16.5,-23), scale=(0.14, 0.14, 0.14), collider='box')


# cube12 = Entity(model='f35', color=color.white, position = (23,16.5,-185), scale=(0.14, 0.14, 0.14), collider='box')
# cube13 = Entity(model='f35', color=color.white, position = (23,16.5,-215), scale=(0.14, 0.14, 0.14), collider='box')
# cube14 = Entity(model='f35', color=color.white, position = (23,16.5,-240), scale=(0.14, 0.14, 0.14), collider='box')


# cube11.rotation_y = 180

# cube12.rotation_y = 180

cube8.rotation_y = -28

# cube14.rotation_y = 90

# cube9.rotation_y = -37

# cube10.rotation_y = -37

# cube11 = Entity(model='f35', color=color.white, position = (-35,16.5,-132), scale=(0.14, 0.14, 0.14), collider='box')

# cube.11 


# cube2.rotation_y = 80

cube.rotation_y = -90

# Use FirstPersonController for player movement
player = FirstPersonController()
player.entity = player
player.cursor.scale = 0.000001
player.speed = 30
player.gravity = 0 

# Set up the camera to follow the player
camera.position = (0, 1, -5)
camera.rotation = (30, 90, 0)

# cube.rotation_y = 180

turn_speed = 50


global engine_speed
engine_speed = 0

global pV_speed
pV_speed = 0

alt_text = Text(
    text="Altitude: "+str(cube.y)+"ft", 
    # origin=(1, 1),  # The origin is the point of reference for positioning (top-right corner)
    position=(0.012, 0.021),  # Position it in the right top corner (relative to screen size)
    scale=0.06,  # Adjust the text size
    color=color.white  # Set the text color
    )


vel_text = Text(
    text="Velocity: "+str(engine_speed)+"kmph", 
    # origin=(1, 1),  # The origin is the point of reference for positioning (top-right corner)
    position=(0.012,0.024),  # Position it in the right top corner (relative to screen size)
    scale=0.06,  # Adjust the text size
    color=color.white  # Set the text color
    )

# vSpeed_text = Text(
#     text="Velocity: "+str(engine_speed)+"kmph", 
#     # origin=(1, 1),  # The origin is the point of reference for positioning (top-right corner)
#     position=(0.012,0.024),  # Position it in the right top corner (relative to screen size)
#     scale=0.06,  # Adjust the text size
#     color=color.white  # Set the text color
#     )


# runway.collider = 'box'  # You need to add a collider component to the plane
cube.collider = 'box'


# ambient_light = AmbientLight()
# ambient_light.intensity = 0.1


cube.rottion_y =  -90


def update():

    engine = 0
    global pV_speed
    global engine_speed # Set move speed 
    propeller.rotation_x += pV_speed * time.dt

    screen_width, screen_height = window.size

    
    # Position the entity at the top-right corner
    ah.position = Vec2(screen_width / 2 - 0.1, screen_height / 2 - 0.1)
    # roll_decay = 60

    if held_keys['v']:
        enginey = 300

    # roll_velocity = 2

    # global pV_speed

    # cube.rotation_y = -90

    
    cube.position -= cube.right * engine_speed * time.dt * 100
    
    # cube.rotation_y = -90

    roll_velocity = 50

    gravity = 0

    # if cube.y == 16.5:
    #     cube.y = 16.5

    if abs(cube.y - 16.5) < 0.01:
        cube.y = 16.5  # This won't cause unnecessary updates


    if engine_speed > 10:
        cube.gravity = 0
    if engine_speed == 0 and cube.y > 15:
        cube.gravity = 5
    else:
        gravity +=  1
        cube.y -= gravity * time.dt * 10.8

    # cube.position *= engine_speed * time.dtå

    # cube.position *= engine_speed

    # Code for Fly-By-Wire system

    gravity = 5

    # alt_text.Text = ""
    if cube.y >= 17:
        if held_keys['left arrow']:

            cube.rotation_x -= 30 * time.dt  # Move up
            # cube.rotation_y += 40 * time.dt
            # cube.y += 4 * time.dt
            # tail_wing.rotation_x -= 0.14
            
        if held_keys['right arrow']:
            
            

            cube.rotation_x += 30 * time.dt  # Move down
            # tail_wing.rotation_x += 0.14
            # cube.rotation_y -= 40 * time.dt
            # cube.y += math.cos(math.radians(cube.rotation_y)) * engine_speed * time.dt

    if held_keys['up arrow']:
        cube.rotation_z += 30 * time.dt  # Move up

    

        # right_wing.rotation_x -= 0.12
        # cube.rotation_y -= 40 * time.dt
    # if cube.y >= 2:
    if held_keys['down arrow']:
            
        cube.rotation_z -= 30 * time.dt  # Move up
            # cube.rotation_y += 40 * time.dt
        #     left_wing.rotation_x -= 0.12
        #     right_wing.rotation_x -= -0.12
    if held_keys['c']:
        cube.rotation_y += 30 * time.dt  # Move up
        # cube.rotation_y += 40 * time.dt
    if held_keys['z']:
        cube.rotation_y -= 30 * time.dt  # Move down
        # cube.rotation_y -= 40 * time.dt

    # def on_input(key):
    #     if key == 'v':  # Check if the 'v ' key was pressed
    #         engine_speed += 10

    if held_keys['i']:
        player.y += 10 * time.dt  # Move up
    if held_keys['k']:
        player.y -= 10 * time.dt  # Move up

    alt_text.text = ""
    alt_text.text = "Altitude: "+str(round(cube.y,1))+"feet"


    # if not held_keys['left arrow']:
    #     roll_velocity -= 5 * time.dt  # Gradually reduce the roll velocity
    #     if abs(roll_velocity) < 0.01:  # Stop the roll motion when it's small enough
    #         roll_velocity = 0

    # Code for angular trigonometrical craft movements that correspond to Fly-By-Wire system

    # cube.x -= math.sin(math.radians(cube.rotation_y)) * engine_speed * time.dt
    # cube.z -= math.cos(math.radians(cube.rotation_y)) * engine_speed * time.dt
    # cube.y -= math.cos(math.radians(cube.rotation_x)) * engine_speed * time.dt

    if held_keys['p']:
        pV_speed += 1 * time.dt * 200

    if pV_speed > 500:
        APU_text = Text(
        text="APU start completed; engine at sufficient speed to taxi", 
        # origin=(1, 1),  # The origin is the point of reference for positioning (top-right corner)
        position=(-0.0195,0.01),  # Position it in the right top corner (relative to screen size)
        scale=0.06,  # Adjust the text size
        color=color.yellow  # Set the text color
        )
        # time.sleep(5)
        # APU_text.text = 

    if held_keys['v']:
        if pV_speed > 500:
            engine_speed += 1 * time.dt * 1.08
            vel_text.text="Velocity: "+str(round(engine_speed,1))+"knots"
            # pV_speed += 1 * time.dt * 50

    if held_keys['b']:
        if engine_speed > 0:
            engine_speed -= 1 * time.dt * 1.08
            vel_text.text="Velocity: "+str(round(engine_speed,1))+"knots"


    if engine_speed > 0:
        APU_text.color = color.dark_gray
    # else:
    #     APU_text.enabled = True    

    
    if engine_speed > 10:
        takeoff_text = Text(
        text="Velocity above 10knots; ready to rotate for take-off", 
        # origin=(1, 1),  # The origin is the point of reference for positioning (top-right corner)
        position=(-0.0195,0.01),  # Position it in the right top corner (relative to screen size)
        scale=0.06,  # Adjust the text size
        color=color.yellow  # Set the text color
        )
        # time.sleep(5)
        # APU_text.text =

    # if cube.y > 1:
    #     takeoff_text.color = color.dark_gray

    if held_keys['l']:
        cube.model = f35up
        cube.scale = (3,3,3)


    



    # cube.x += math.sin(math.radians(cube.rotation_y)) * engine_speed * time.dt
    # cube.z += math.cos(math.radians(cube.rotation_y)) * engine_speed * time.dt

    # cube.position += cube.forward * speed * time.dt  # cube.forward gives the direction


    # Update the cube's position based on its rotation
    # Move the cube forward along its local z-axis

    camera.position = cube.position + Vec3(0, 5, -20)  # Follow the plane, keep distance
    camera.look_at(cube)  # Always look at the airplane

    # camera_distance = 15  # The distance the camera will stay in front of the cube
    # camera_offset = Vec3(0, 5, camera_distance)  # Camera's offset from the cube

    # # # Calculate the camera position based on the cube's yaw (rotation_y)
    # # camera_x = cube.x + camera_offset.x * cos(radians(cube.rotation_y))
    # camera_z = cube.z + camera_offset.z * sin(radians(cube.rotation_y))

    # # # Update camera position, keeping it 180 degrees in front of the cube
    # camera.position = Vec3(camera.x, cube.y + 5, camera_z)

    # # Ensure the camera always looks at the cube
    # camera.look_at(cube)

    # camera_distance = 15  # The distance the camera will stay behind the cube
    # camera_offset = Vec3(0, 5, -camera_distance)  # Camera's offset behind the cube (negative Z-axis)

    # camera.rotation_y = 180

    # camera.rotation_x = 90

    # Calculate the camera position based on the cube's yaw (rotation_y)
    # camera_x = cube.x + camera_offset.x * cos(radians(cube.rotation_y))
    # camera_z = cube.z + camera_offset.z * sin(radians(cube.rotation_y))

    # Update camera position, keeping it 180 degrees behind the cube
    # camera.position = Vec3(camera_x, cube.y + 5, camera_z)

    # camera.position = lerp(camera.position, Vec3(camera_x, cube.y + 5, camera_z), 0.1)


    # Ensure the camera always looks at the cube
    # camera.look_at(cube)

    # camera.rotation = Vec3(30, cube.rotation_y, 0)  # Align camera with the plane's yaw but fix pitch and roll
    # camera.position = cube.position + Vec3(0, 5, -15)  # Maintain the camera distance from the plane

    # camera.position = cube.position + Vec3(0, 5, -15)  # Camera follows behind the plane
    # camera.rotation = Vec3(30, cube.rotation_y, 0)  # Keep camera's yaw the same as the plane's rotation (yaw follows plane's turning)

    # camera.position = cube.position + Vec3(0, 5, -15)  # Camera stays behind the plane
    # camera.rotation = Vec3(30, cube.rotation_y, 0)  # Follow plane's yaw, keep camera's pitch fixed at 30 degrees

    # # Make sure the camera is always looking at the plane
    # camera.look_at(cube)



    # camera.rotation_y  = cube.rotation_y/2.8

    # camera.rotation = lerp(camera.rotation, cube.rotation, 0.1)  # Adjust 0.1 for speed of smoothing
    
    # camera.look_at(cube.position)

    if held_keys['escape']:
        exit(code=None)


# Run the application
app.run()
