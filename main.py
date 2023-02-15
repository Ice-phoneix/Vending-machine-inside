# frame work and libraries
import pygame
import random
# framework start
pygame.init()

#Basic parameters
Resolution_X = 1920
Resolution_Y = 1090
White = (255, 255, 255)
Background = pygame.image.load('Images/Game background.jpg')
Flashlight_size = 25
Flashlight_off_colour = (0, 102, 0)
Flashlight_on_colour = (0, 255, 0)




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
    #alt+f4 shutdown
    Keyboard = pygame.key.get_pressed()
    F4 = Keyboard[pygame.K_F4]
    if F4 == True:
        pygame.QUIT
    
    #Background
    window.blit(Background, (0, 0))
    
    #Selected drink indicator
    Flashing_light1 = pygame.draw.ellipse(window, Flashlight_off_colour , (1719, 268, Flashlight_size, Flashlight_size))
    Flashing_light2 = pygame.draw.ellipse(window, Flashlight_off_colour , (1831, 268, Flashlight_size, Flashlight_size))
    Flashing_light3 = pygame.draw.ellipse(window, Flashlight_off_colour , (1719, 355, Flashlight_size, Flashlight_size))
    Flashing_light4 = pygame.draw.ellipse(window, Flashlight_off_colour , (1831, 355, Flashlight_size, Flashlight_size))
    Flashing_light5 = pygame.draw.ellipse(window, Flashlight_off_colour , (1719, 445, Flashlight_size, Flashlight_size))
    Flashing_light6 = pygame.draw.ellipse(window, Flashlight_off_colour , (1831, 445, Flashlight_size, Flashlight_size))
    Flashing_light7 = pygame.draw.ellipse(window, Flashlight_off_colour , (1719, 537, Flashlight_size, Flashlight_size))
    Flashing_light8 = pygame.draw.ellipse(window, Flashlight_off_colour , (1831, 537, Flashlight_size, Flashlight_size))
    Flashing_light9 = pygame.draw.ellipse(window, Flashlight_off_colour , (1719, 626, Flashlight_size, Flashlight_size))
    Flashing_light10 = pygame.draw.ellipse(window, Flashlight_off_colour , (1831, 626, Flashlight_size, Flashlight_size))
    Flashing_light11 = pygame.draw.ellipse(window, Flashlight_off_colour , (1719, 719, Flashlight_size, Flashlight_size))
    Flashing_light12 = pygame.draw.ellipse(window, Flashlight_off_colour , (1831, 719, Flashlight_size, Flashlight_size))
    
    drink = (random.randint(1,12))
    if drink == 1:
        Flashing_light1 = pygame.draw.ellipse(window, Flashlight_on_colour , (1719, 268, Flashlight_size, Flashlight_size))
    if drink == 2:
            Flashing_light2 = pygame.draw.ellipse(window, Flashlight_on_colour , (1831, 268, Flashlight_size, Flashlight_size))
    if drink == 3:

        
            
            
            
    #display update
    pygame.display.update()

