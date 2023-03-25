import pygame as pg
from random import randint
pg.init()
window=pg.display.set_mode((1000,800))
pg.display.set_caption('Ping-pong')
x2=randint(-5,5)
y2=randint(-5,5)
gameov=True
while x2==0 and y2==0:
	x2=randint(-5,5)
	y2=randint(-5,5)
class Game_Sprite():
	def __init__(self,img,x,y,w,h,speed):
		self.image=pg.transform.scale(pg.image.load(img),(w,h))
		self.w=w
		self.h=h
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.speed=speed
	def reset(self):
		window.blit(self.image,(self.rect.x,self.rect.y))

class Player1(Game_Sprite):
	def control(self):
		global gameov
		keys=pg.key.get_pressed()
		if keys[pg.K_w] and self.rect.y>0 and gameov==True:
			self.rect.y-=self.speed
		if keys[pg.K_s] and self.rect.y<700 and gameov==True:
			self.rect.y+=self.speed
class Player2(Game_Sprite):
	def control(self):
		global gameov
		keys=pg.key.get_pressed()
		if keys[pg.K_UP] and self.rect.y>0 and gameov==True:
			self.rect.y-=self.speed
		if keys[pg.K_DOWN] and self.rect.y<700 and gameov==True:
			self.rect.y+=self.speed

class Ball(Game_Sprite):
    def move(self):
        global player1,player2,x2,y2
        self.rect.x+=x2
        self.rect.y+=y2
        if self.rect.y>750:
            y2=-5
        if self.rect.y<0:
            y2=5
        if pg.sprite.collide_rect(self, player1):
            x2=5
        if pg.sprite.collide_rect(self, player2):
            x2=-5

bg= Game_Sprite('images/bg.jpg', 0,0, 1000,800, 0)
player1=Player1('images/pl1.png', 50,400, 50,100, 4)
player2=Player2('images/pl2.png', 900,400, 50,100, 4)
ball=Ball('images/ball.png', 300, 400, 50,50 , 2)
label=pg.font.SysFont('ComicSans', 100).render('Red win', True, 'red')
label2=pg.font.SysFont('ComicSans', 100).render('Blue win', True, 'blue')

while True:
	pg.time.Clock().tick(60)
	for i in pg.event.get():
		if i.type==pg.QUIT:
			exit()
	bg.reset()
	player1.reset()
	player1.control()
	player2.reset()
	player2.control()
	ball.reset()
	ball.move()
	if ball.rect.x<-50:
		window.blit(label,(300,275))
		gameov=False
	if ball.rect.x>1000:
		window.blit(label2,(300,275))
		gameov=False
	pg.display.flip()