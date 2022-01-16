from tkinter import *
import pygame
from pygame.locals import *
import random
import pyautogui

pygame.init()
window = None
HEIGHT = 700
WIDTH = 1296
run = True
PINK = (255, 192, 203)
all_cars = [pygame.image.load('Assets/Car6.jpg'),
    pygame.image.load('Assets/Car3.jpg'),
                 pygame.image.load('Assets/Car4.jpg'),
                 pygame.image.load('Assets/Car5.jpg'),
                 pygame.image.load('Assets/CarL.jpg')]
BLUECAR = all_cars[1]
GREENCAR = all_cars[4]
ORANGECAR = all_cars[3]
REDCAR = all_cars[2]
YOUR_CAR = "Car6.jpg"
BLACK = (0, 0, 0)
FPS = 40
start = 5
end = 10
track_width = 300
track_height = WIDTH
y = 525
cy1 = 525
cy2 = 525
cy3 = 525
cy4 = 525
cy5 = 525
c1 = 0
over = False
c2 = 0
c3 = 0
c4 = 0
c5 = 0
top = None
cars = {0: "Purple Car (Your car)", 1: "Blue Car (Computer)", 2: "Red Car (Computer)",
             3: "Orange Car (Computer)", 4: "Green Car (computer)"}
cars_index = {"Purple Car : (Your car)": 0, "Blue Car (Computer)": 1, "Red Car (Computer)": 2,
              "Orange Car (Computer)": 3, "Green Car (computer)": 4}
clock = pygame.time.Clock()
bg_img = pygame.image.load('Assets/Background.jpg')
bg_img = pygame.transform.scale(bg_img, (WIDTH,HEIGHT))

def drawText(text,Color,xpos,ypos,win):
    font = pygame.font.SysFont(None, 55)
    st = font.render(text, True, Color)
    win.blit(st, [xpos, ypos])
def OnOver(winner,win):
        win.fill(PINK)
        pos = [y,cy1,cy2,cy3,cy4]
        drawText("The winner of this race is",BLACK,350,50,win)
        pygame.time.delay(1000)
        drawText(winner,BLACK,370,120,win)
        car1 = pygame.image.load("Assets/"+YOUR_CAR)
        display = (WIDTH - car1.get_width()) // 2
        car2 = pygame.image.load('Assets/Car3.jpg')
        car2 = pygame.transform.scale(car2,(car1.get_width(),car1.get_height()))
        car3 = pygame.image.load('Assets/Car4.jpg')
        car3 = pygame.transform.scale(car3,(car1.get_width(),car1.get_height()))
        car4 = pygame.image.load('Assets/Car5.jpg')
        car4 = pygame.transform.scale(car4,(car1.get_width(),car1.get_height()))
        car5 = pygame.image.load('Assets/CarL.jpg')
        car5 = pygame.transform.scale(car5,(car1.get_width(),car1.get_height()))
        if (winner == cars[0]):
            win.blit(car1,(display-50,180))
        elif (winner == cars[1]):
            win.blit(car2,(display-50,180))
        elif (winner == cars[2]):
            win.blit(car3,(display-50,180))
        elif (winner == cars[3]):
            win.blit(car4,(display-50,180))
        elif (winner == cars[4]):
            win.blit(car5,(display-50,180))
        pygame.display.update()
def basic():
    global run,y, cy1, cy2, cy3, cy4, over, top, c1, c2, c3, c4, c5,blueChosen,redChosen,greenChosen,orangeChosen
    mid_height = 100
    win = pygame.display.set_mode((WIDTH,HEIGHT))
    bg_img = pygame.image.load('Assets/Background.jpg')
    bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))
    pygame.display.set_caption("Car-Racing")
    track1 = pygame.image.load('Assets/Track1.jpg')
    track1 = pygame.transform.scale(track1, (track_width, track_height))
    track2 = pygame.image.load('Assets/Track2.jpg')
    track2 = pygame.transform.scale(track1, (track_width, track_height))
    track3 = pygame.image.load('Assets/Track3.jpg')
    track3 = pygame.transform.scale(track1, (track_width, track_height))
    track4 = pygame.image.load('Assets/Track4.jpg')
    track4 = pygame.transform.scale(track1, (track_width, track_height))
    track5 = pygame.image.load('Assets/Track4.jpg')
    track5 = pygame.transform.scale(track1, (track_width, track_height))
    car1 = pygame.image.load(f'Assets/{YOUR_CAR}')
    car2 = BLUECAR
    car2 = pygame.transform.scale(car2, (car1.get_width(), car1.get_height()))
    car3 = REDCAR
    car3 = pygame.transform.scale(car3, (car1.get_width(), car1.get_height()))
    car4 = ORANGECAR
    car4 = pygame.transform.scale(car4, (car1.get_width(), car1.get_height()))
    car5 = GREENCAR
    car5 = pygame.transform.scale(car5, (car1.get_width(), car1.get_height()))
    while run:
        # Drawing Images
        win.blit(bg_img, (0, 0))
        win.blit(track1, (-25, 0))
        win.blit(track2, (230, 0))
        win.blit(track3, (500, 0))
        win.blit(track4, (750, 0))
        win.blit(track5, (1000, 0))
        win.blit(car1, (mid_height, y))
        win.blit(car2, (350, cy1))
        win.blit(car3, (620, cy2))
        win.blit(car4, (850, cy3))
        win.blit(car5, (1120, cy4))
        clock.tick(FPS)
        # Key Presses and HITTING THE BOUNDARIES and checking who wins it.
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                run = False
                pyautogui.alert("Are you sure you want to quit")
                pygame.quit()
        if (over):
            OnOver(top,win)
            pygame.time.delay(3000)
            pygame.quit()
            break
        if (pygame.key.get_pressed()[K_RETURN]):
            y = cy1 = cy2 = cy3 = cy4 = 525
            c1 = c2 = c3 = c4 = c5 = 0
        if (pygame.key.get_pressed()[K_UP]):
            if max(c1, c2, c3, c4, c5) == 5:
                over = True
                lst = [c1, c2, c3, c4, c5]
                ans = lst.index(max(lst))
                winner = cars[ans]
                top = winner
            num = random.randint(start, end + 1)
            y -= num
            if (y <= -2):
                y = 525
                c1 += 1
            num2 = random.randint(start, end + 1)
            cy1 -= num2
            if (cy1 <= -2):
                cy1 = 525
                c2 += 1
            num3 = random.randint(start, end + 1)
            cy2 -= num3
            if (cy2 <= -2):
                cy2 = 525
                c3 += 1
            num4 = random.randint(start, end + 1)
            cy3 -= num4
            if (cy3 <= -2):
                cy3 = 525
                c4 += 1
            num5 = random.randint(start, end + 1)
            cy4 -= num5
            if (cy4 <= -2):
                cy4 = 525
                c5 += 1
        pygame.display.update()

basic()
