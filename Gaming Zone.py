# Importing the library
import pygame, sys, random
from pygame.locals import *

pygame.font.init()
  
# Initializing surface
surface = pygame.display.set_mode((500,500))
WHITE = (255,255,255)
FONT= pygame.font.Font('freesansbold.ttf', 26)
Font= pygame.font.Font('freesansbold.ttf', 22)

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
FPS = 20

#Colours
WHITE = (255,255,255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

RED = (200, 0, 0)
light_red = (255, 0, 0)

YELLOW = (200, 200, 0)
LIGHT_YELLOW = (255, 255, 0)

GREEN = (34, 177, 76)
LIGHT_GREEN = (0, 255, 0)

ADD_NEW_FLAME_RATE = 25

vs_font = pygame.font.SysFont("Times New Roman", 25)

canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#pygame.display.set_caption('Mario')
 
# Initialing Color
color = (255,0,0)

run=True
Mario=0
def txt_btn(message, color, btnx, btny, btnwidth, btnheight, size="vsmall"):
    txtSrf, textRect = txt_object(message, color, size)
    textRect.center = ((btnx + (btnwidth / 2)), btny + (btnheight / 2))
    surface.blit(txtSrf, textRect)


def txt_object(txt, color, size="small"):
    if size == "small":
        txtSrfc = s_font.render(txt, True, color)
    if size == "medium":
        txtSrfc = m_font.render(txt, True, color)
    if size == "large":
        txtSrfc = l_font.render(txt, True, color)
    if size == "vsmall":
        txtSrfc = vs_font.render(txt, True, color)

    return txtSrfc, txtSrfc.get_rect()

def btn(txt, x, y, width, height, inactive_color, active_color, action=None,size=" "):
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x + width > cursor[0] > x and y + height > cursor[1] > y:
        pygame.draw.rect(surface, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "Mario":
                import mario

            if action == "TankBattle":
                import TankGame

            if action == "Puzzle":
                import Puzzle
                

    else:
        pygame.draw.rect(surface, inactive_color, (x, y, width, height))

    txt_btn(txt, BLACK, x, y, width, height)


while run:
    text1=FONT.render("Welcome To Sudiksha And Sara's Gaming Zone !!! ",True,WHITE,BLACK)
    T1Rect = text1.get_rect()
    T1Rect.center = (350,50)
    surface.blit(text1,T1Rect)
    pygame.display.update()
    btn("The Mario Game !",100,100,200,30,WHITE,BLUE,action="Mario",)
    btn("Tank Battle Game !",100,150,200,30,WHITE,BLUE,action="TankBattle",)
    btn("Solve The Puzzle !",100,200,200,30,WHITE,BLUE,action="Puzzle",)
    btn("Quit", 950, 30, 100, 50, WHITE, RED, action="quit")

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

        '''if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                import mario'''
                

                
    
