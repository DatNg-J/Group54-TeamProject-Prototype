import pygame
import pygame.gfxdraw
import sys
import time
import random

from label import *


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()

buttons = pygame.sprite.Group()
class Button(pygame.sprite.Sprite):
    ''' A button treated like a Sprite... and killed too '''
    
    def __init__(self, position, text, size,
        colors="white on blue",
        hover_colors="red on green",
        style="button1",
        borderc=(255,255,255),
        command=lambda: print("No command activated for this button")):


        super().__init__()
        global num

        self.text = text
        self.command = command

        self.colors = colors
        self.original_colors = colors
        self.fg, self.bg = self.colors.split(" on ")

        if hover_colors == "red on green":
            self.hover_colors = f"{self.bg} on {self.fg}"
        else:
            self.hover_colors = hover_colors

        self.style = style
        self.borderc = borderc 

        self.font = pygame.font.SysFont("Arial", size)
        self.render(self.text)
        self.x, self.y, self.w , self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, 500, self.h)
        self.position = position
        self.pressed = 1

        buttons.add(self)

    def render(self, text):

        self.text_render = self.font.render(text, 1, self.fg)

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

        lcolor = (150, 150, 150)
        lcolor2 = (50, 50, 50)
        pygame.draw.line(screen, lcolor, self.position,
            (self.x + self.w , self.y), 5)
        pygame.draw.line(screen, lcolor, (self.x, self.y - 2),
            (self.x, self.y + self.h), 5)

        pygame.draw.line(screen, lcolor2, (self.x, self.y + self.h),
            (self.x + self.w , self.y + self.h), 5)
        pygame.draw.line(screen, lcolor2, (self.x + self.w , self.y + self.h),
            [self.x + self.w , self.y], 5)

        pygame.draw.rect(screen, self.bg, self.rect)  

    def draw_button2(self):
        ''' a linear border '''

        pygame.draw.rect(screen, self.bg, (self.x - 50, self.y, 500 , self.h))
        pygame.gfxdraw.rectangle(screen, (self.x - 50, self.y, 500 , self.h), self.borderc)

    def check_collision(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):

            self.colors = self.hover_colors

        else:
            self.colors = self.original_colors



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
    
    if qnum < len(questions):
        print(qnum, len(questions))
        if answered == "right":
            time.sleep(.1) 
            points += 1

        qnum += 1 
        score.change_text(str(points), color="black")

        title.change_text(questions[qnum-1][0], color="black")

        num_question.change_text(str(qnum))
        show_question(qnum) 
        


    elif qnum == len(questions):
        print(qnum, len(questions))
        if answered == "right":
            kill()
            time.sleep(.1)
            points +=1
        score.change_text("You reached a score of " + str(points), color="black")
    time.sleep(.5)




questions = [
    ["What is 2 + 2", ["4", "8", "6", "7"]],
    ["What is 1 + 5", ["6", "3", "7", "5"]],
    ["What is 7 - 5", ["2", "4", "1", "3"]],
    ["What is 14 - 8", ["6", "7", "2", "5"]],
    ["What is 25 - 17", ["8", "5", "9", "7"]],
    ["What is 7 * 8", ["56", "59", "58", "54"]],
    ["What is 6 * 12", ["72", "76", "78", "74"]],
    ["What is 36 / 12", ["3", "9", "12", "6"]],
    ["What is 14 * 16", ["224", "248", "212", "232"]],
    ["What is 56 / 4", ["14", "18", "12", "16"]],
]




def show_question(qnum):
    ''' put your buttons here '''


    kill()

    

    pos = [100, 150, 200, 250]

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


def kill():
    for _ in buttons:
        _.kill()

qnum = 1
points = 0

num_question = Label(screen, str(qnum), 0, 0)
score = Label(screen, "", 50, 300)
title = Label(screen, questions[qnum-1][0], 10, 10, 55, color="black")



Background=pygame.image.load('Background.png')
Background=pygame.transform.scale(Background,(1024,768))

def loop():
    global game_on

    show_question(qnum)

    while True:
        screen.blit(Background, (0,0))
        for event in pygame.event.get(): 
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
        buttons.update()
        buttons.draw(screen)
        show_labels()
        clock.tick(60)
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    pygame.init()
    game_on = 1
    loop()
