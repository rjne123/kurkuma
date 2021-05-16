from pygame import* 
from random import*

window = display.set_mode((700,700))

game = True
clock = time.Clock()
FPS = 60
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x,player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def dv(self):
        press = key.get_pressed()
        if press[K_UP]:
            self.rect.y += 5
        if press[K_DOWN]:
            self.rect.y -= 5
class GameSprite1(sprite.Sprite):
    def __init__(self, player_image, player_x,player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def dv(self):
        press = key.get_pressed()
        if press[K_LEFT]:
            self.rect.y += 5
        if press[K_RIGHT]:
            self.rect.y -= 5
class GameSprite2(sprite.Sprite):
    def __init__(self, player_image, player_x,player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

sc1=0
sc2=0
dx=5
dy=3

ball = l = GameSprite2('wellness_ball_active_sitting_hero_3_3.jpg',350,350)
l = GameSprite('12838980299.jpg',100,0)
l1 = GameSprite1('12838980299.jpg',600,0)
ll = GameSprite('12838980299.jpg',100,350)
ll1 = GameSprite1('12838980299.jpg',600,350)
lll = GameSprite('12838980299.jpg',100,600)
lll1 = GameSprite1('12838980299.jpg',600,600)


k1 = transform.scale(image.load("game-over-neon-sign_1174-671.jpg"), (700,700))
win =False
while game:
    ball.rect.x +=dx
    ball.rect.y -=dy
    if ball.rect.x > 650:
        dx *= -1
        sc1+=1
    if ball.rect.y < 0:
        dy *= -1
    if ball.rect.x < 0:
        dx *= -1
        sc2+=1
    if ball.rect.y > 650:
        dy *= -1
    if sc1 == 10:
        win = True
        game=False
        print("правая ракетка победила")
    if sc2 == 10:
        win = True
        game=False
        print("левая ракетка победила")
    window.fill((10,10,100))
    for i in event.get():
        if i.type==QUIT:
            game = False
    l.reset()
    l.dv()
    l1.reset()
    l1.dv()
    ll.reset()
    ll.dv()
    ll1.reset()
    ll1.dv()

    lll.reset()
    lll.dv()
    lll1.reset()
    lll1.dv()
    ball.reset()
    if sprite.collide_rect(ball, l):
        dx *= -1
    if sprite.collide_rect(ball, l1):         
        dx *= -1
    if sprite.collide_rect(ball, ll):
        dx *= -1
    if sprite.collide_rect(ball, ll1):
        dx *= -1
    if sprite.collide_rect(ball, lll):
        dx *= -1
    if sprite.collide_rect(ball, lll1):
        dx *= -1
    clock.tick(30)
    display.update()

while win:
    window.blit(k1,(0,0))
    for i in event.get():
        if i.type==QUIT:
            win = False
    clock.tick(30)
    display.update()
