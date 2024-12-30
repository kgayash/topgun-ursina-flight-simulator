from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Initialize the Ursina application
app = Ursina()

#Will be importing 3D private U.S.A.F FA/18 from Blender in January, 2025

f35 = load_model('f35.glb')
f35_entity = Entity(model=f35, scale=(0.014,0.014,0.014))
# icps_entity.rotation_x = 90

# ambient_light = AmbientLight()
# ambient_light.intensity = 0.5


player = FirstPersonController()
player.cursor.scale = 0.0001  
player.speed = 25
player.gravity = 0
player.scale = 0.5

def update():
    if held_keys['up arrow']:
        player.y += 10 * time.dt  # Move up
    if held_keys['down arrow']:
        player.y -= 10 * time.dt  # Move down
    if held_keys['escape']:
        exit(code=None)

# Run the application
app.run()
