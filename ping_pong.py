from pygame import *

'''Необхідні класи'''
# музика
mixer.init()
mixer.music.load("stranger-things-124008.mp3")
mixer.music.play()

#текст
font.init()
font1 = font.Font(None,30)#шрифт та величина тексту
text1 = font1.render("Рахунок",True,(0,0,0))


# клас-батько для спрайтів
class GameSprite(sprite.Sprite):
    #конструктор класу
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (wight, height)) #разом 55,55 - параметри
        self.speed = player_speed
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

     
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# клас-спадкоємець для спрайту-гравця (керується стрілками)    
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

#ігрова сцена:
back = (200, 255, 255)  #колір фону (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
 
player1 = Player("racket.png ",0,150, 10, 50,200)
player2 = Player('racket.png',550,150,10,50,200)
player3 = Player('tenis_ball.png',300,150,10,70,70)

x=3
y=3
#прапорці, що відповідають за стан гри
game = True
finish = False
clock = time.Clock()
 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
  
    if finish != True:
        window.fill(back)
        player1.reset()
        player2.reset()
        player2.update_r()
        player1.update_l()
        player3.reset()

    player3.rect.x += x
    player3.rect.y += y

    if player3.rect.y > 450 or player3.rect.y <0:
        y*=-1

    if sprite.collide_rect(player3,player1) or sprite.collide_rect(player3,player2):
        x*=-1    
    window.blit(text1,(100,100))
    display.update()
    clock.tick(60)
    
