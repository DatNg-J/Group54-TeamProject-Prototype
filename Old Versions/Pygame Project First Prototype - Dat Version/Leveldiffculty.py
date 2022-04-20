#import pygame
import pygame

#game initialization
pygame.init()

#set display window value
display = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Main Menu")

#Set Data
main_font = pygame.font.SysFont("cambria", 50)
background = pygame.image.load("Pygame Project - Dat Version/Main_menu_background.png")

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

#Format of buttons
button_surface = pygame.image.load("Pygame Project - Dat Version/buttonspng/easybutton.png")
button_surface = pygame.transform.scale(button_surface, (400, 150))
button = Button(button_surface, 256, 300, "Easy")

button_surface2 = pygame.image.load("Pygame Project - Dat Version/buttonspng/mediumbutton.png")
button_surface2 = pygame.transform.scale(button_surface2, (400, 150))
button2 = Button(button_surface2, 768, 300, "Medium")

button_surface3 = pygame.image.load("Pygame Project - Dat Version/buttonspng/hardbutton.png")
button_surface3 = pygame.transform.scale(button_surface3, (400, 150))
button3 = Button(button_surface3, 256, 500, "Hard")

button_surface4 = pygame.image.load("Pygame Project - Dat Version/buttonspng/extremebutton.png")
button_surface4 = pygame.transform.scale(button_surface4, (400, 150))
button4 = Button(button_surface4, 768, 500, "Extreme")

#Format of Menu Background
bg=pygame.transform.scale(background,(1024,768))


#keep the game window open until event user manual end
open1 = True
while open1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open1 = False
    display.fill("white")
    display.blit(bg, (0, 0))
    
    button.update()
    button.changeColor(pygame.mouse.get_pos())
    
    button2.update()
    button2.changeColor(pygame.mouse.get_pos())
    
    button3.update()
    button3.changeColor(pygame.mouse.get_pos())
    
    button4.update()
    button4.changeColor(pygame.mouse.get_pos())
    
    pygame.display.update()

#end entire script
pygame.quit()
quit()

