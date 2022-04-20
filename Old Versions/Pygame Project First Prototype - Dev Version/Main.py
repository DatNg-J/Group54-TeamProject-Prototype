#Import Modules
import pygame
import time
import random
import sys

#Button Def
def button(x,y,w,h, image2, image1, action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        screen.blit(image1, (x,y,w,h))
        if click[0] == 1 and action!= None:
            action()
    else:
        screen.blit(image2, (x,y,w,h))

#Define Size of Window
size = (1024, 768)
gamewidth = 1024
gameheight = 768

screen = pygame.display.set_mode((gamewidth,gameheight))
clock = pygame.time.Clock()

#Game Background Image Load
gamebackground = pygame.image.load('Pygame Project Main Folder/Pngs/Main_menu_background.png')
gamebackground = pygame.transform.scale(gamebackground,(1024,768))
gamebackground2 = pygame.image.load('Pygame Project Main Folder/Pngs/Main_menu_background.png')
gamebackground2 = pygame.transform.scale(gamebackground2,(1024,768))

#Pygame Initialization 
pygame.init()
#-------------

#Game Button Image Load
button_instructions_hover = pygame.image.load("Pygame Project Main Folder/Pngs/instructionbutton2.png")
button_start_hover = pygame.image.load("Pygame Project Main Folder/Pngs/startbutton2.png")
button_intructions = pygame.image.load("Pygame Project Main Folder/Pngs/instructionbutton.png")
button_start = pygame.image.load("Pygame Project Main Folder/Pngs/startbutton.png")
instructions = pygame.image.load("Pygame Project Main Folder/Pngs/Instructions.png")
backbutton = pygame.image.load("Pygame Project Main Folder/Pngs/Backbutton.png")
easybutton = pygame.image.load("Pygame Project Main Folder/Pngs/easybutton.png")
easybutton_hover = pygame.image.load("Pygame Project Main Folder/Pngs/easybutton2.png")

#Image Scaling
instructions = pygame.transform.scale(instructions,(1024,768))
easybutton = pygame.transform.scale(easybutton, (400, 150))
easybutton_hover = pygame.transform.scale(easybutton_hover, (400, 150))

#Clock
fpsClock = pygame.time.Clock

#Defining Functions
def mainmenu():
   main=True
   while main:
        screen.blit(gamebackground, (0,0))
        event()
        #Instruction Button
        button(320,360,400,100,button_intructions,button_instructions_hover,instructionmenu)
        #Start Button
        button(370,180,200,100,button_start,button_start_hover,start)
        pygame.display.update()

def instructionmenu():
    main=True
    while main:
       screen.blit(instructions,(0,0))
       #Back Button
       button(750,600,750,600,backbutton,backbutton,mainmenu)
       event()
       pygame.display.update()

def start():
    main=True
    while main:
        screen.blit(gamebackground2, (0,0))
        #Back button
        button(750,600,750,600,backbutton,backbutton,mainmenu)
        #Easy button
        button(370,180,200,100,easybutton,easybutton_hover,easygame)
        event()
        pygame.display.update()

def easygame():
    main=True
    while main:
        screen.blit(gamebackground2, (0,0))
        #Back Button
        button(750,600,750,600,backbutton,backbutton,mainmenu)
        event()
        pygame.display.update()

def event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


# -------- Main Program Loop -----------
done = False
while not done:
    #pygame.display.update()
    mainmenu()
    instructionmenu()
    start()
    easygame()
    pygame.display.flip()
pygame.quit()






