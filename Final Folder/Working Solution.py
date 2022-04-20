#Import Modules
import pygame
import time
import sys
import os

#Define Button
def button(x,y,w,h, image2, image1, action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        screen.blit(image1, (x,y,w,h))
        if click[0]==1 and action!=None:
            action()
    else:
        screen.blit(image2, (x,y,w,h))

#Define the Size of Window
size=(1024, 768)
width=1024
height=768

screen=pygame.display.set_mode((width,height))

#Loads Game Background Image
Background=pygame.image.load('Main_menu_background.png')
Background=pygame.transform.scale(Background,(1024,768))
Background2=pygame.image.load('Main_menu_background.png')
Background2=pygame.transform.scale(Background2,(1024,768))
Background3=pygame.image.load('Background.png')
Background3=pygame.transform.scale(Background3,(1024,768))

#Pygame Initialisation
pygame.init()

#Clock/Timer
clock = pygame.time.Clock()
fps = 60

#Loads the Game Button Images
instructionsbutton2=pygame.image.load("instructionbutton2.png")
startbutton2=pygame.image.load("startbutton2.png")
intructionsbutton=pygame.image.load("instructionbutton.png")
startbutton=pygame.image.load("startbutton.png")
instructions=pygame.image.load("Instructions.png")
backbutton=pygame.image.load("Backbutton.png")
backbutton2=pygame.image.load("Backbutton2.png")

#Image Scaling
instructions=pygame.transform.scale(instructions,(1024,768))
intructionsbutton = pygame.transform.scale(intructionsbutton,(400,150))
instructionsbutton2 = pygame.transform.scale(instructionsbutton2,(400,150))
backbutton = pygame.transform.scale(backbutton,(240,80))
backbutton2 = pygame.transform.scale(backbutton2,(240,80))

#Define Fonts
font30 = pygame.font.SysFont('Constantia', 30)
font20 = pygame.font.SysFont('Constantia', 20)
font40 = pygame.font.SysFont('Constantia', 40)
font60 = pygame.font.SysFont('Constantia', 60)

#define colour:
green = (0,128,0)
#--------

#Define Main Functions of the Game
def menuscreen():
   main=True
   while main:
      screen.blit(Background, (0,0))
      event()
      button(320,360,400,100,intructionsbutton,instructionsbutton2,instruction)
      button(370,180,200,100,startbutton,startbutton2,game)
      pygame.display.update()

def instruction():
    main=True
    while main:
       screen.blit(instructions,(0,0))
       button(750,600,750,600,backbutton,backbutton2,menuscreen)
       event()
       pygame.display.update()

def game():
    os.system('Game.py')
        
def event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

#def draw_text(text, font, text_col, x, y):
    #img = font.render(text, True, text_col)
    #screen.blit(img, (x, y))

#def Questions(Q, A, B, C):
    #draw_text(str(Q), font30, green, int(width / 2 - 450), int(150))
    #draw_text(("1 - " + str(A)), font30, green, int(width / 2 - 450), int(180))
    #draw_text(("2 - " + str(B)), font30, green, int(width / 2 - 450), int(220))
    #draw_text(("3 - " + str(C)), font30, green, int(width / 2 - 450), int(260))    
#---------------------------------
done=False
#Program Loop
while not done:
    menuscreen()
    instruction()
    game()
    pygame.display.flip()
pygame.quit()






