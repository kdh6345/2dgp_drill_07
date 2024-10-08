from pico2d import *
import random
# Game object class here
class Grass:
    # 생성자 함수 : 객체의 초기 상태를 설정
    def __init__(self):
        # 모양 없는 납작한 붕어빵의 초기 모습 결정
        self.image=load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400,30)

    pass

class Boy:
    def __init__(self):
        self.x, self.y=0,90
        self.frame=0
        self.image=load_image('run_animation.png')

    def update(self):
        self.frame=(self.frame+1)%8
        self.x+=5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)


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
    global team
    global world

    running=True
    #월드 리스트 생성
    world=[]
    grass=Grass()  # 잔디를 찍어낸다. 생성한다
    world.append(grass)
    team=[Boy() for i in range(10)]
    world+=team

running=True

def update_world():
    for o in world:
        o.update()
    pass

def render_world():
    clear_canvas()
    grass.draw()
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
