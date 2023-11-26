import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 550

player = Rect(10, 500, 50, 50)
gravity = 0


platforms = []
platform = None
max_height = HEIGHT


def is_on_floor():
    index = player.collidelist(platforms)
    return player.collidelist(platforms) != -1 and player.bottom <= platforms[index].top


for i in range(10):
    platform = Rect(
        i * 125,
        randint(50, HEIGHT - 100),
        100,
        50
    )
    if platform.bottom < max_height:
        max_height = platform.bottom
    platforms.append(platform)


def draw():
    screen.fill("yellow")
    screen.draw.filled_rect(player, "blue")
    for platform in platforms:
        screen.draw.filled_rect(platform, "green")
    

def on_key_down():
    global gravity
    if keyboard.space:
        gravity = -20


def get_collided_platform():
    if player.collidelist(platforms) != -1:
        return platforms[player.collidelist(platforms)]


def update():
    global gravity
    global max_height
    global is_on_floor
    global platform
    
    
    if get_collided_platform() is not None:
        platform = get_collided_platform()
        
    else:
        gravity += 1
    player.y += gravity
    
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT
        

    if keyboard.a:
        player.x -= 5
    if keyboard.d:
        player.x += 5



pgzrun.go()
