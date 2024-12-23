from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Initialize the Ursina application
app = Ursina()

# Create a white cube (player character)

runway = Entity(model='plane', scale=(100, 1, 5), color=color.black, position=(0, 0, 0), collider='box')

runway.rotation_y = 90

# Create the main body of the airplane (fuselage)
fuselage = Entity(model='cube', color=color.gray, scale=(2, 0.6, 8), position=(0, 0, 0))

# Create the wings (left and right wings)
left_wing = Entity(model='cube', color=color.blue, scale=(6, 0.2, 2), position=(-3, 0, 0))
right_wing = Entity(model='cube', color=color.blue, scale=(6, 0.2, 2), position=(3, 0, 0))

# Create the tail wing (horizontal stabilizer) - properly connected to the fuselage
tail_wing = Entity(model='cube', color=color.red, scale=(3, 0.3, 1), position=(0, 0.5, 4))  # Tail wing connected to fuselage

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
engine_right.parent = cube
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
camera.rotation = (30, 0, 0)

cube.rotation_y = 180

turn_speed = 50


def update():
    engine = 5
    enginey = 1000
    propeller.rotation_x += enginey * time.dt
    # roll_decay = 60

    if held_keys['v']:
        enginey = 300

    # roll_velocity = 2

    cube.z += engine * time.dt
    move_speed = 1  # Set move speed
    if held_keys['left arrow']:
        cube.rotation_z += 50 * time.dt  # Move up
        # cube.rotation_y += 40 * time.dt
    if held_keys['right arrow']:
        # roll_velocity += turn_speed * time.dt  # Increase roll velocity
        cube.rotation_z -= 50 * time.dt  # Move down
        # cube.rotation_y -= 40 * time.dt
    if held_keys['up arrow']:
        cube.rotation_x += 50 * time.dt  # Move up
        # cube.rotation_y += 40 * time.dt
        cube.y += math.cos(math.radians(cube.rotation_y)) * move_speed * time.dt
    if held_keys['down arrow']:
        cube.rotation_x -= 50 * time.dt  # Move down
        # cube.rotation_y -= 40 * time.dt
        # cube.y += math.cos(math.radians(cube.rotation_y)) * move_speed * time.dt
    if held_keys['c']:
        cube.rotation_y += 10 * time.dt  # Move up
        # cube.rotation_y += 40 * time.dt
    if held_keys['z']:
        cube.rotation_y -= 10 * time.dt  # Move down
        # cube.rotation_y -= 40 * time.dt
    

    # if not held_keys['right arrow']:
    #     roll_velocity -= roll_decay * time.dt  # Gradually reduce the roll velocity
    #     if abs(roll_velocity) < 0.01:  # Stop the roll motion when it's small enough
    #         roll_velocity = 0

    cube.x -= math.sin(math.radians(cube.rotation_y)) * move_speed * time.dt
    cube.z -= math.cos(math.radians(cube.rotation_y)) * move_speed * time.dt




    # Update the cube's position based on its rotation
    # Move the cube forward along its local z-axis

    # camera.position = cube.position + Vec3(0, 5, -15)  # Follow the plane, keep distance
    # camera.look_at(cube)  # Always look at the airplane



    if held_keys['escape']:
        exit(code=None)

# Run the application
app.run()
