from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(50, 750), 599
        self.image1 = load_image('ball41x41.png')
        self.image2 = load_image('ball21x21.png')
        self.image_type = random.randint(0, 1)  # 0이면 큰 공, 1이면 작은 공

    def update(self):
        if self.image_type == 0:
            self.y -=random.randint(5,20)
        else:
            self.y -= random.randint(5, 30)

        if self.y < 30:  # 바닥에 닿으면 멈춤
            self.y = 30

    def draw(self):
        if self.image_type == 0:
            self.image1.draw(self.x, self.y)
        else:
            self.image2.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global world
    global team

    running = True
    world = []
    grass = Grass()
    world.append(grass)
    team = [Ball() for i in range(20)]  # 20개의 Ball
    world += team

def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code
close_canvas()
