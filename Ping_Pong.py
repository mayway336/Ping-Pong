from pygame import *
W, H = 860, 600
winn = display.set_mode((W, H))
display.set_caption('Ping Pong')
back = (0, 180, 0)
winn.fill(back)
clock = time.Clock()
game = True
FPS = 90
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        display.update()
        clock.tick(FPS)