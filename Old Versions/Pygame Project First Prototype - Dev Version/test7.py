#Import Modules
import pygame
import time
import sys
import pygame.gfxdraw
import random

#import class
from labeling import *


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
#size=(1024, 768)
width=1024
height=768


#Loads Game Background Image
Background=pygame.image.load('Main_menu_background.png')
Background=pygame.transform.scale(Background,(1024,768))
Background2=pygame.image.load('Main_menu_background.png')
Background2=pygame.transform.scale(Background2,(1024,768))
Background3=pygame.image.load('Background.png')
Background3=pygame.transform.scale(Background3,(1024,768))

#Pygame Initialisation
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((width,height))

#Clock/Timer
clock = pygame.time.Clock()

#Game buttons classifcation
buttons = pygame.sprite.Group()
class Button(pygame.sprite.Sprite):
    ''' A button treated like a Sprite... and killed too '''
    
    def __init__(self, position, text, size,
        colors="white on blue",
        hover_colors="red on green",
        style="button1",
        borderc=(255,255,255),
        command=lambda: print("No command activated for this button")):

        # the hover_colors attribute needs to be fixed
        super().__init__()
        global num

        self.text = text
        self.command = command
        # --- colors ---
        self.colors = colors
        self.original_colors = colors
        self.fg, self.bg = self.colors.split(" on ")
        # hover_colors
        if hover_colors == "red on green":
            self.hover_colors = f"{self.bg} on {self.fg}"
        else:
            self.hover_colors = hover_colors
        # styles can be button1 or button2 (more simple this one)
        self.style = style
        self.borderc = borderc # for the style2
        # font
        self.font = pygame.font.SysFont("Arial", size)
        self.render(self.text)
        self.x, self.y, self.w , self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, 500, self.h)
        self.position = position
        self.pressed = 1
        # the groups with all the buttons
        buttons.add(self)

    def render(self, text):
        # we have a surface
        self.text_render = self.font.render(text, 1, self.fg)
        # memorize the surface in the image attributes
        self.image = self.text_render

    def update(self):
        self.fg, self.bg = self.colors.split(" on ")
        if self.style == "button1":
            self.draw_button1()
        elif self.style == "button2":
            self.draw_button2()
        if self.command != None:
            self.hover()
            self.click()

    def draw_button1(self):
        ''' draws 4 lines around the button and the background '''
        # horizontal up
        lcolor = (150, 150, 150)
        lcolor2 = (50, 50, 50)
        pygame.draw.line(screen, lcolor, self.position,
            (self.x + self.w , self.y), 5)
        pygame.draw.line(screen, lcolor, (self.x, self.y - 2),
            (self.x, self.y + self.h), 5)
        # horizontal down
        pygame.draw.line(screen, lcolor2, (self.x, self.y + self.h),
            (self.x + self.w , self.y + self.h), 5)
        pygame.draw.line(screen, lcolor2, (self.x + self.w , self.y + self.h),
            [self.x + self.w , self.y], 5)
        # background of the button
        pygame.draw.rect(screen, self.bg, self.rect)  

    def draw_button2(self):
        ''' a linear border '''
        # the width is set to 500 to have the same size not depending on the text size
        pygame.draw.rect(screen, self.bg, (self.x - 50, self.y, 500 , self.h))
        pygame.gfxdraw.rectangle(screen, (self.x - 50, self.y, 500 , self.h), self.borderc)

    def check_collision(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            # you can change the colors when the pointer is on the button if you want
            self.colors = self.hover_colors
            # pygame.mouse.set_cursor(*pygame.cursors.diamond)
        else:
            self.colors = self.original_colors
            # pygame.mouse.set_cursor(*pygame.cursors.arrow)


    def hover(self):
        ''' checks if the mouse is over the button and changes the color if it is true '''

        self.check_collision()

    def click(self):
        ''' checks if you click on the button and makes the call to the action just one time'''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed == 1:
                print("The answer is:'" + self.text + "'")
                self.command()
                self.pressed = 0

            if pygame.mouse.get_pressed() == (0,0,0):
                self.pressed = 1

# ACTION FOR BUTTON CLICK ================
def on_click():
    print("Click on one answer")

def on_right():
    check_score("right")

def on_false():
    ''' if there is no 'right' as arg it means it's false '''
    check_score()

def check_score(answered="wrong"):
    ''' here we check if the answer is right '''
    global qnum, points
    
    # until there are questions (before last)
    hit.play() # click sound
    if qnum < len(questions):
        print(qnum, len(questions))
        if answered == "right":
            time.sleep(.1) # to avoid adding more point when pressing too much
            points += 1
            # Show the score text
        qnum += 1 # counter for next question in the list
        score.change_text(str(points))
        # Change the text of the question
        title.change_text(questions[qnum-1][0], color="cyan")
        # change the question number
        num_question.change_text(str(qnum))
        show_question(qnum) # delete old buttons and show new
        

    # for the last question...
    elif qnum == len(questions):
        print(qnum, len(questions))
        if answered == "right":
            kill()
            time.sleep(.1)
            points +=1
        score.change_text("You reached a score of " + str(points))
    time.sleep(.5)

#game Questions 
questions = [
    ["What is Italy's Capital?", ["Rome", "Paris", "Tokyo", "Madrid"]],
    ["What is France's Capital?", ["Paris", "Rome", "Tokyo", "Madrid"]],
    ["What is England's Capital?", ["London", "Rome", "Tokyo", "Madrid"]],
]

#show question
def show_question(qnum):
    ''' put your buttons here '''

    # Kills the previous buttons/sprites
    kill()

    
    # The 4 position of the buttons
    pos = [100, 150, 200, 250]
    # randomized, so that the right one is not on top
    random.shuffle(pos)

    Button((10, 100), "1. ", 36, "red on yellow",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=None)
    Button((10, 150), "2. ", 36, "red on yellow",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=None)
    Button((10, 200), "3. ", 36, "red on yellow",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=None)
    Button((10, 250), "4. ", 36, "red on yellow",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=None)


    # ============== TEXT: question and answers ====================
    Button((50, pos[0]), questions[qnum-1][1][0], 36, "red on yellow",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=on_right)
    Button((50, pos[1]), questions[qnum-1][1][1], 36, "red on yellow",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=on_false)
    Button((50, pos[2]), questions[qnum-1][1][2], 36, "red on yellow",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=on_false)
    Button((50, pos[3]), questions[qnum-1][1][3], 36, "red on yellow",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=on_false)

#kill buttons
def kill():
    for _ in buttons:
        _.kill()

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

#define varibles
qnum = 1
points = 0

# ================= SOME LABELS ==========================
num_question = Label(screen, str(qnum), 0, 0)
score = Label(screen, "Punteggio", 50, 300)
title = Label(screen, questions[qnum-1][0], 10, 10, 55, color="cyan")
write1 = Label(screen, "PYQUIZ BY GiovanniPython", 50, 350, 20, color="red")

#Define Main Functions of the Game
def menuscreen():
   main=True
   while main:
      screen.blit(Background, (0,0))
      event()
      button(320,360,400,100,intructionsbutton,instructionsbutton2,instruction)
      button(370,180,200,100,startbutton,startbutton2,show_question(qnum))
      pygame.display.update()

def instruction():
    main=True
    while main:
       screen.blit(instructions,(0,0))
       button(750,600,750,600,backbutton,backbutton2,menuscreen)
       event()
       pygame.display.update()

#def game():
    #define colour:
    green = (0,128,0)
    #--------
    #varible:
    countdown = 20
    last_count = pygame.time.get_ticks()
    key = pygame.key.get_pressed()
    startgame = 18
    
    #--------
    #questions:
    Q1="Q1) 2+2 = ?"
    Q2="Q2) 1+5 = ?" 
    Q3="Q3) 3+4 = ?, 6 – A, 7 – B, 5 – C"
    Q4="Q4) 10 + 5 = ?, 12 – A, 17 – B, 15 – C"
    #--------
    #answers:
    #Q1
    Q1ANS1=4
    Q1ANS2=8
    Q1ANS3=7
    #Q2
    Q2ANS1=7
    Q2ANS2=3
    Q2ANS3=6
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
            draw_text('You Failed! Try Better Next Time!', font60, green, int(width / 2 - 450), int(height / 2 + 50))
            button(750,600,750,600,backbutton,backbutton2,menuscreen)
        #----------
        #event() # used this instead since the define doesn't work
        
        Questions(Q1, str(Q1ANS1), str(Q1ANS2), str(Q1ANS3))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            
            if event.type == pygame.KEYDOWN:
                if event.key != pygame.K_1:
                    countdown -= 10
                    Questions(Q2, str(Q2ANS1), str(Q2ANS2), str(Q2ANS3))
                elif event.key == pygame.K_1:
                    countdown += 5
                    Questions(Q2, str(Q2ANS1), str(Q2ANS2), str(Q2ANS3))
            
                

    
        
        
        clock.tick(60)
        pygame.display.update()

#def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#def Questions(Q, A, B, C):
    draw_text(str(Q), font30, green, int(width / 2 - 450), int(150))
    draw_text(("1 - " + str(A)), font30, green, int(width / 2 - 450), int(180))
    draw_text(("2 - " + str(B)), font30, green, int(width / 2 - 450), int(220))
    draw_text(("3 - " + str(C)), font30, green, int(width / 2 - 450), int(260))    

#def event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
#---------------------------------   

def event():
    for event in pygame.event.get(): # ====== quit / exit
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    
def loop():
    global game_on
    event()
    
    while True:
        screen.fill(0)
        menuscreen()
        instruction()
        
        
        buttons.update() #                     update buttons
        buttons.draw(screen)
        show_labels()        #                 update labels
        clock.tick(60)
        pygame.display.update()
    pygame.quit()
    
if __name__ == '__main__':
    pygame.init()
    game_on = 1
    loop()




#done=False
#Program Loop
#while not done:
    #menuscreen()
    #instruction()
    #game()
    #pygame.display.flip()
#pygame.quit()






