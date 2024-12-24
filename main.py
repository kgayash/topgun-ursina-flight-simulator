from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


# Initialize the Ursina application
app = Ursina()

# sky = Sky(texture='Sky_gradient_mid_afternoon_looking_north')

# water = Entity(model='plane', scale=(200, 1, 200), position=(0, 0, 0), texture='water', collider='box')


# clouds = Clouds()

# Create a white cube (player character)

runway = Entity(model='plane', scale=(5, 1000, 5), color = color.black, position=(0, 1, 0), collider='box')

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


# Create the main body of the airplane (fuselage)
fuselage = Entity(model='cube', color=color.gray, scale=(2, 0.6, 8), position=(0, 0, 0))

# Create the wings (left and right wings)
left_wing = Entity(model='cube', color=color.blue, scale=(6, 0.2, 2), position=(-3, 0, 0))
right_wing = Entity(model='cube', color=color.blue, scale=(6, 0.2, 2), position=(3, 0, 0))

# Create the tail wing (horizontal stabilizer) - properly connected to the fuselage
tail_wing = Entity(model='cube', color=color.red, scale=(3, 0.3, 1), position   =(0, 0.5, 4))  # Tail wing connected to fuselage

# Create the vertical stabilizer (rudder) - properly connected to the tail
vertical_stabilizer = Entity(model='cube', color=color.red, scale=(1, 2, 1), position=(0, 1.25, 5))  # Rudder connected

# Create the engines (two small cylinders representing engines)
engine_left = Entity(model='cylinder', color=color.orange, scale=(0.5, 0.5, 1.5), position=(-3, 0.3, -4))
engine_right = Entity(model='cylinder', color=color.orange, scale=(0.5, 0.5, 1.5), position=(3, 0.3, -4))

# Create the nose cone (small cone at the front)
nose_cone = Entity(model='cone', color=color.green, scale=(0.7, 0.7, 1), position=(0, 0, -8))

# Create the landing gear (simple cylinders for wheels)
# landing_gear_front = Entity(model='cylinder', color=color.black, scale=(0.4, 0.4, 1), position=(0, -0.2, 3.5))
# landing_gear_left = Entity(model='cylinder', color=color.black, scale=(0.4, 0.4, 0.5), position=(-2, -0.2, 4.5))
# landing_gear_right = Entity(model='cylinder', color=color.black, scale=(0.4, 0.4, 0.5), position=(2, -0.2, 4.5))

front_landing_gear = Entity(model='cylinder', color=color.yellow, scale=(0.4, 0.4, 1), position=(0, -1.0, 3.5))  # Adjusted Y position
left_landing_gear = Entity(model='cylinder', color=color.yellow, scale=(0.4, 0.4, 0.5), position=(-1.5, -1.0, 3))  # Adjusted Y position
right_landing_gear = Entity(model='cylinder', color=color.yellow, scale=(0.4, 0.4, 0.5), position=(1.5, -1.0, 3))  # Adjusted Y position

propeller_blade1 = Entity(
    model='cube', color=color.yellow, scale=(0.2, 2, 0.05), position=(0, 0, 0), rotation=(0, 0, 0)
)
propeller_blade2 = Entity(
    model='cube', color=color.yellow, scale=(0.2, 2, 0.05), position=(0, 0, 0), rotation=(90, 0, 0)
)
# # propeller_blade3 = Entity(
# #     model='cube', color=color.yellow, scale=(0.2, 3, 0.05), position=(0, 0, 0), rotation=(-120, 0, 0)
# )

# Parent the propeller blades to the fuselage (plane body)


cube = Entity(parent=scene, position = (0,1,0))
propeller = Entity(parent=scene, position = (0,0,-4.49))
propeller_blade1.parent = propeller
propeller_blade2.parent = propeller
# propeller_blade3.parent = propeller

propeller.rotation_y = 90
propeller.parent = cube
fuselage.parent = cube
left_wing.parent = cube
right_wing.parent = cube
tail_wing.parent = cube
vertical_stabilizer.parent = cube
engine_left.parent = cube
nose_cone.parent = cube
front_landing_gear.parent = cube
left_landing_gear.parent = cube
right_landing_gear.parent = cube

# cube = Entity(model='cube', color=color.white, scale=(2, 2, 2), collider='box')

# Use FirstPersonController for player movement
player = FirstPersonController()
player.entity = player
player.cursor.scale = 0.001
player.gravity = 0  

# Set up the camera to follow the player
camera.position = (0, 1, -5)
# camera.rotation = (30, 0, 0)

cube.rotation_y = 180

turn_speed = 50


global engine_speed
engine_speed = 0

global pV_speed
pV_speed = 0


alt_text = Text(
    text="Altitude: 2000ft", 
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


def update():
    engine = 0
    global pV_speed
    global engine_speed # Set move speed 
    propeller.rotation_x += pV_speed * time.dt
    # roll_decay = 60

    if held_keys['v']:
        enginey = 300

    # roll_velocity = 2

    # global pV_speed

    cube.position -= cube.forward * engine_speed * time.dt 

    roll_velocity = 50


    # cube.position *= engine_speed * time.dtå

    # cube.position *= engine_speed

    # Code for Fly-By-Wire system

    if held_keys['left arrow']:
        cube.rotation_z += 50 * time.dt  # Move up
        # cube.rotation_y += 40 * time.dt
    #     left_wing.rotation_x -= 0.12
    #     right_wing.rotation_x -= -0.12
    if held_keys['right arrow']:
        # roll_velocity += turn_speed * time.dt  # Increase roll velocity
        cube.rotation_z -= 50 * time.dt  # Move down
        # left_wing.rotation_x -= -0.12
        # right_wing.rotation_x -= 0.12
        # cube.rotation_y -= 40 * time.dt
    if held_keys['up arrow']:
        cube.rotation_x += 30 * time.dt  # Move up
        # cube.rotation_y += 40 * time.dt
        # cube.y += 4 * time.dt
        # tail_wing.rotation_x -= 0.14
    if held_keys['down arrow']:
        cube.rotation_x -= 30 * time.dt  # Move down
        # tail_wing.rotation_x += 0.14
        # cube.rotation_y -= 40 * time.dt
        # cube.y += math.cos(math.radians(cube.rotation_y)) * engine_speed * time.dt
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


    # if not held_keys['left arrow']:
    #     roll_velocity -= 5 * time.dt  # Gradually reduce the roll velocity
    #     if abs(roll_velocity) < 0.01:  # Stop the roll motion when it's small enough
    #         roll_velocity = 0

    # Code for angular trigonometrical craft movements that correspond to Fly-By-Wire system

    # cube.x -= math.sin(math.radians(cube.rotation_y)) * engine_speed * time.dt
    # cube.z -= math.cos(math.radians(cube.rotation_y)) * engine_speed * time.dt
    # cube.y -= math.cos(math.radians(cube.rotation_x)) * engine_speed * time.dt

    

    if held_keys['v']:
        engine_speed += 1 * time.dt * 1.3
        vel_text.text="Velocity: "+str(round(engine_speed,2))+"kmph"
        pV_speed += 1 * time.dt * 50

    # cube.x += math.sin(math.radians(cube.rotation_y)) * engine_speed * time.dt
    # cube.z += math.cos(math.radians(cube.rotation_y)) * engine_speed * time.dt

    # cube.position += cube.forward * speed * time.dt  # cube.forward gives the direction


    # Update the cube's position based on its rotation
    # Move the cube forward along its local z-axis

    # camera.position = cube.position + Vec3(0, 5, -40)  # Follow the plane, keep distance
    # camera.look_at(cube)  # Always look at the airplane


    # camera.rotation = Vec3(30, cube.rotation_y, 0)  # Align camera with the plane's yaw but fix pitch and roll
    # camera.position = cube.position + Vec3(0, 5, -15)  # Maintain the camera distance from the plane

    # camera.position = cube.position + Vec3(0, 5, -15)  # Camera follows behind the plane
    # camera.rotation = Vec3(30, cube.rotation_y, 0)  # Keep camera's yaw the same as the plane's rotation (yaw follows plane's turning)

    # camera.position = cube.position + Vec3(0, 5, -15)  # Camera stays behind the plane
    # camera.rotation = Vec3(30, cube.rotation_y, 0)  # Follow plane's yaw, keep camera's pitch fixed at 30 degrees

    # # Make sure the camera is always looking at the plane
    # camera.look_at(cube)



    # camera.rotation_z  = cube.rotation_z

    # camera.rotation = lerp(camera.rotation, cube.rotation, 0.1)  # Adjust 0.1 for speed of smoothing
    
    # camera.look_at(cube.position)

    if held_keys['escape']:
        exit(code=None)



# Run the application
app.run()
