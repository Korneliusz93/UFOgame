import pygame
import os
import random
import math 

pygame.init()

szer = 1280
wys = 800

ekran = pygame.display.set_mode((szer,wys))

class planeta():
    def __init__(self,radius):
        self.x = random.randint(0,1280)
        self.y = random.randint(0,800)
        self.center = (self.x,self.y)
        self.r = radius
        self.dx = random.choice([-1,1])
        self.dy = random.choice([-1,1])
        #self.kierunek = (self.dx,self.dy)
        self.predkosc = 2
        self.kolor = (random.randint(40,254),random.randint(40,254),random.randint(40,254))
        self.ksztalt = pygame.Rect(self.x-self.r/2,self.y-self.r/2,self.r,self.r)
    def rysuj(self):
        pygame.draw.circle(ekran, self.kolor, self.center, self.r, 0)
    def ruch(self):
        if self.x == 1280:
            self.dx = -1*self.predkosc
#            self.kierunek = (dx,dy)
        if self.x == 0:
            self.dx = 1*self.predkosc
#            self.kierunek = (dx,dy)
        if self.y == 800:
            self.dy = -1*self.predkosc
#            self.kierunek = (dx,dy)
        if self.y == 0:
            self.dy = 1*self.predkosc
 #           self.kierunek = (dx,dy)
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.center = (self.x, self.y)
        self.ksztalt = pygame.Rect(self.x-self.r/2,self.y-self.r/2,self.r,self.r)

    def kolizja(self,player):
        if self.ksztalt.colliderect(player):return True
        else: return False

class spaceship():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.szerokosc = 50
        self.wysokosc = 30
        self.ksztalt = pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)
        self.grafika = pygame.image.load(os.path.join('spaceship.png'))
    def rysuj(self):
        ekran.blit(self.grafika, (self.x, self.y))
    def ruch(self,vx,vy):
        self.x = self.x + vx
        self.y = self.y + vy
        self.ksztalt = pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)

    
def napis(tekst,rozmiar, xnapis, ynapis):
    obiekt = pygame.font.SysFont("Helvetica", rozmiar)
    rndr = obiekt.render(tekst,0,(250,250,250))
    x = xnapis
    y = ynapis
    ekran.blit(rndr, (x,y))

planety = []
for ran in range(31):
    planety.append(planeta(random.randint(4,16)))

#widok = "menu"
#test
widok = "menu"

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                mvy = -1
            if event.key == pygame.K_DOWN:
                mvy = 1
            if event.key == pygame.K_LEFT:
                mvx = -1
            if event.key == pygame.K_RIGHT:
                mvx = 1
            if event.key == pygame.K_SPACE:
                if widok != "rozgrywka":
                    gracz = spaceship(640,400)
                    mvx = 0
                    mvy = 0
                    widok = "rozgrywka"
                    punkty = 0
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if widok == "menu":
        napis("Aby zacząć wciśnij spację ... ",60,400,400)
        grafika = pygame.image.load(os.path.join('logo.png'))
        ekran.blit(grafika,((szer - grafika.get_rect().width)/2,(wys - grafika.get_rect().height)/8))

    if widok == "rozgrywka":
        ekran.fill((0,0,0))
        for p in planety:
            p.ruch()
            p.rysuj()
            punkty = punkty + math.fabs(mvy)
            if p.kolizja(gracz.ksztalt) is True:
                widok = "koniec"
        gracz.rysuj()
        gracz.ruch(mvx,mvy)
        #pygame.display.update()
        napis(str(punkty),40,10,10 )
    elif widok == "koniec":
        napis("Niestety przegrałeś..",60,400,400)
        napis(".. by wznowić wciścnij spację",60,400,600)
        grafika = pygame.image.load(os.path.join('logo.png'))
        ekran.blit(grafika,((szer - grafika.get_rect().width)/2,(wys - grafika.get_rect().height)/8))
    pygame.display.update()
