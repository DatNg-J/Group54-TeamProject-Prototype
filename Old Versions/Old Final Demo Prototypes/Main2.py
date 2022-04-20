#Import modules
import pygame
import time
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

#Game Background Image Load
Background = pygame.image.load('Main_menu_background.png')
Background = pygame.transform.scale(Background,(1024,768))
Background2 = pygame.image.load('Main_menu_background.png')
Background2 = pygame.transform.scale(Background2,(1024,768))
Background3=pygame.image.load('Background.png')
Background3=pygame.transform.scale(Background3,(1024,768))


#Pygame Initialization 
pygame.init()
#-------------

#clock/timer
clock = pygame.time.Clock()
fps = 60

#Game Button Image Load
instructionsbutton2 = pygame.image.load("instructionbutton2.png")
startbutton2 = pygame.image.load("startbutton2.png")
intructionsbutton = pygame.image.load("instructionbutton.png")
startbutton = pygame.image.load("startbutton.png")
instructions = pygame.image.load("Instructions.png")
backbutton = pygame.image.load("Backbutton.png")
backbutton2 = pygame.image.load("Backbutton2.png")

#Image Scaling
instructions = pygame.transform.scale(instructions,(1024,768))
backbutton = pygame.transform.scale(backbutton,(240,80))
intructionsbutton = pygame.transform.scale(intructionsbutton,(400,150))
instructionsbutton2 = pygame.transform.scale(instructionsbutton2,(400,150))
backbutton2 = pygame.transform.scale(backbutton2,(240,80))

#define fonts
font40 = pygame.font.SysFont('Constantia', 40)
font60 = pygame.font.SysFont('Constantia', 60)


#Defining Functions
def menuscreen():
   main=True
   while main:
        screen.blit(Background, (0,0))
        event()
        #Instruction Button
        button(320,360,400,100,intructionsbutton,instructionsbutton2,instructions)
        #Start Button
        button(370,180,200,100,startbutton,startbutton2,game)
        pygame.display.update()

def Instructions():
    main=True
    while main:
       screen.blit(instructions,(0,0))
       #Back Button
       button(750,600,750,600,backbutton,backbutton2,menuscreen)
       event()
       pygame.display.update()

def game():
    #define colour:
    green = (0,128,0)
    #--------
    #varible:
    countdown = 5
    last_count = pygame.time.get_ticks()
    #--------
    main=True
    while main:
        #gamebackground
        screen.blit(Background3, (0,0))
        
        #clock countdown
        if countdown > 0:
            draw_text(str(countdown), font40, green, int(32), int(48))
            count_timer = pygame.time.get_ticks()
            if count_timer - last_count > 1000:
                countdown -= 1
                last_count = count_timer
        else:
            draw_text('You Failed! Try Better Next Time!', font60, green, int(gamewidth / 2 - 450), int(gameheight / 2 + 50))
            button(750,600,750,600,backbutton,backbutton2,menuscreen)
        #----------
            
        
        clock.tick(60)
        event()
        pygame.display.update()
        
def event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()                              
    
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# -------- Main Program Loop -----------
done = False
while not done:
    #pygame.display.update()
    menuscreen()
    Instructions()
    game()
    pygame.display.flip()
pygame.quit()






