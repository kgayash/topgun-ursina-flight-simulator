from ursina import *

# Initialize the Ursina application
app = Ursina()

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
landing_gear_front = Entity(model='cylinder', color=color.black, scale=(0.4, 0.4, 1), position=(0, -0.2, 3.5))
landing_gear_left = Entity(model='cylinder', color=color.black, scale=(0.4, 0.4, 0.5), position=(-2, -0.2, 4.5))
landing_gear_right = Entity(model='cylinder', color=color.black, scale=(0.4, 0.4, 0.5), position=(2, -0.2, 4.5))

# Group all parts together (all parts will move as one airplane)
airplane = Entity(parent=scene)
fuselage.parent = airplane
left_wing.parent = airplane
right_wing.parent = airplane
tail_wing.parent = airplane
vertical_stabilizer.parent = airplane
engine_left.parent = airplane
engine_right.parent = airplane
nose_cone.parent = airplane
landing_gear_front.parent = airplane
landing_gear_left.parent = airplane
landing_gear_right.parent = airplane

# Movement and rotation
speed = 5
turn_speed = 100

def update():
    # Move the airplane forward in the direction it is facing (along its z-axis)
    airplane.z += speed * time.dt

    # Rotate the airplane using arrow keys (yaw, pitch, and roll)
    if held_keys['left arrow']:
        airplane.rotation_y += turn_speed * time.dt  # Turn left (yaw)
    if held_keys['right arrow']:
        airplane.rotation_y -= turn_speed * time.dt  # Turn right (yaw)

    if held_keys['up arrow']:
        airplane.rotation_x += turn_speed * time.dt  # Nose up (pitch)
    if held_keys['down arrow']:
        airplane.rotation_x -= turn_speed * time.dt  # Nose down (pitch)

# Run the application
app.run()
