# frame work and libraries
import pygame
import random
# framework start
pygame.init()

#Basic parameters
Resolution_X = 1280
Resolution_Y = 720


#Window creation
window = pygame.display.set_mode((Resolution_X, Resolution_Y))
pygame.display.set_caption('Vending machine game')

#window loop
while True:
    #Turning off the app
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           #framework shutdown
            pygame.quit()
            #app shutdown
            sys.exit()

