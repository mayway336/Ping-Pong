from pygame import *
from random import randint


'''КЛАССЫ'''
white = (255, 255, 255)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        winn.blit(self.image, (self.rect.x, self.rect.y))


class Player1(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < H - 90:
            self.rect.y += self.speed

    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < H - 90:
            self.rect.y += self.speed





'''НАСТРОЙКИ ОКНА'''
W, H = 860, 600
winn = display.set_mode((W, H))
display.set_caption('Ping Pong')
background = transform.scale(image.load('background.webp'), (W, H))


'''ИГРОВЫЕ НАСТРОЙКИ'''
font.init()
font1 = font.SysFont('Arial', 40)
font2 = font.SysFont('Arial', 100)
text_win1 = font2.render('Win Player 1', True, (0, 0, 0))
text_win2 = font2.render('Win Player 2', True, (0, 0, 0))

max_s = 1
score1 = 0
score2 = 0
speed_y = 2
speed_x = 2

'''Спрайты'''
wall_one = Player1('platform.png', W//10, H//2, 20, 100, 10)
wall_two = Player1('racket.png', W*0.9, H//2, 20, 100, 10)


balls = sprite.Group()
for i in range(1):
    ball = GameSprite('ball.png', W//2, H//2, 50, 50, 5)
    balls.add(ball)

'''ИГРОВОЙ ЦИКЛ'''
clock = time.Clock()
game = True
finish = False
FPS = 90
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        winn.blit(background, (0, 0))
        if score1 >= max_s:
            winn.blit(text_win1, (200, 200))
            finish = True
        if score2 >= max_s:
            winn.blit(text_win2, (200, 200))
            finish = True
        ball.rect.y += speed_y
        ball.rect.x += speed_x

        

        if ball.rect.x < 0:
            score2 += 1
            ball.kill()
            ball = GameSprite('ball.png', W//2, H//2, 50, 50, 5)
            balls.add(ball)
        
        if ball.rect.x > W:
            score1 += 1
            ball.kill()     
            ball = GameSprite('ball.png', W//2, H//2, 50, 50, 5)
            balls.add(ball)   

        if ball.rect.y > H-50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(wall_one, ball) or sprite.collide_rect(wall_two, ball):
            speed_x *= -1
            speed_y *= 1
        text_score = font1.render('Очки: ' + str(score1), True, (0, 0, 0))
        text_lost = font1.render('Очки: ' + str(score2), True, (0, 0, 0))
        winn.blit(text_lost, (740, 10))
        winn.blit(text_score, (10, 10))
        balls.update()
        balls.draw(winn)
        wall_one.reset()
        wall_one.update1()
        wall_two.reset()
        wall_two.update2()
        ball.reset()
        ball.update()
    display.update()
    clock.tick(FPS)