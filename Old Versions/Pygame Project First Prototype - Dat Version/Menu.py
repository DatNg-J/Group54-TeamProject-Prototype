#import pygame
import pygame
import time
import random
import sys

#game initialization 
pygame.init()

#set display window value
display = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Main Menu")

#Set Data
main_font = pygame.font.SysFont("cambria", 50)
gamebackground = pygame.image.load("Pygame Project - Dat Version/Main_menu_background.png")
gamebackground=pygame.transform.scale(gamebackground,(1024,768))   
clock = pygame.time.Clock()

#button Class
class Button():
	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		display.blit(self.image, self.rect)
		display.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			print("Button Press!")

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.text_input, True, "green")
		else:
			self.text = main_font.render(self.text_input, True, "white")

#Format of button
button_surface = pygame.image.load("Pygame Project - Dat Version/buttonspng/startbutton.png")
button_surface = pygame.transform.scale(button_surface, (400, 150))

fpsClock = pygame.time.Clock

#Defining
def mainmenu():
   main=True
   while main:
    	display.blit(gamebackground, (0,0))
    	event()
    	button = Button(button_surface, 512, 300, "START")
    	button.update()
    	button.changeColor(pygame.mouse.get_pos())
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
    pygame.display.flip()
pygame.quit()

