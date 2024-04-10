from pygame import *

white = (255, 255, 255)
'''КЛАССЫ'''
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.image.set_colorkey(self.image, [255,255,255])
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        winn.blit(self.image, (self.rect.x, self.rect.y))


class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.y < H - 85:
            self.rect.x += self.speed
    

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.y < H - 85:
            self.rect.x += self.speed


class Ball(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0 or self.rect.x > W:
            self.kill()


'''НАСТРОЙКИ ОКНА'''
W, H = 860, 600
winn = display.set_mode((W, H))
display.set_caption('Ping Pong')
back = (0, 180, 0)
winn.fill(back)


'''ИГРОВЫЕ НАСТРОЙКИ'''
font.init()
font1 = font.SysFont('Arial', 25)
font2 = font.SysFont('Arial', 100)
text_win1 = font2.render('Win Player 1', True, (0, 0, 255))
text_win2 = font2.render('Win Player 2', True, (0, 0, 255))

max_s = 5
score1 = 0
sccore2 = 0


'''Спрайты'''
wall_one = Player1('Wall.png', W//2, H//2, 80, 100, 10)
wall_two = Player2('Wall.png', W, H//2, 80, 100, 10)
ball_one = Ball('Ball.png', W//2, H//2, 50, 50, 5)

'''ИГРОВОЙ ЦИКЛ'''
clock = time.Clock()
game = True
FPS = 90
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    wall_one.reset()
    wall_one.update()
    wall_two.update()
    ball_one.update()
    display.update()
    clock.tick(FPS)