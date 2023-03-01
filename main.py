# frame work and libraries
import pygame
import random
import time
import datetime
import sys
# framework start
pygame.init()

#Basic parameters
Resolution_X = 1920
Resolution_Y = 1090
Red = (210, 4, 45)
Grey = (160,160,160)  
White = (255, 255, 255)
Background = pygame.image.load('Images/Game background.jpg')
Icon = pygame.image.load('Images/Game icon.jpg')
Flashlight_size = 25
Flashlight_off_colour = (0, 102, 0)
Flashlight_on_colour = (0, 255, 0)
GButton_size = 50
Rbutton_size = 37
Sbutton_middlex = 1740
Sbutton_middley = 917 
Lbutton_middlex = 1860
Lbutton_middley = 917
Cbuttonr = 25
FPS = 1
#Window creation
window = pygame.display.set_mode((Resolution_X, Resolution_Y))
pygame.display.set_caption('Vending machine game')
pygame.display.set_icon(Icon)

#FPS clock
FPSclock = pygame.time.Clock() 


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
            Flashing_light3 = pygame.draw.ellipse(window, Flashlight_on_colour , (1719, 355, Flashlight_size, Flashlight_size))
    if drink == 4:
            Flashing_light4 = pygame.draw.ellipse(window, Flashlight_on_colour , (1831, 355, Flashlight_size, Flashlight_size))
    if drink == 5:
            Flashing_light5 = pygame.draw.ellipse(window, Flashlight_on_colour , (1719, 445, Flashlight_size, Flashlight_size))
    if drink == 6:
            Flashing_light6 = pygame.draw.ellipse(window, Flashlight_on_colour , (1831, 445, Flashlight_size, Flashlight_size))
    if drink == 7:
            Flashing_light7 = pygame.draw.ellipse(window, Flashlight_on_colour , (1719, 537, Flashlight_size, Flashlight_size))
    if drink == 8:
            Flashing_light8 = pygame.draw.ellipse(window, Flashlight_on_colour , (1831, 537, Flashlight_size, Flashlight_size))
    if drink == 9:
            Flashing_light9 = pygame.draw.ellipse(window, Flashlight_on_colour , (1719, 626, Flashlight_size, Flashlight_size))
    if drink == 10:
            Flashing_light10 = pygame.draw.ellipse(window, Flashlight_on_colour , (1831, 626, Flashlight_size, Flashlight_size))
    if drink == 11:
            Flashing_light11 = pygame.draw.ellipse(window, Flashlight_on_colour , (1719, 719, Flashlight_size, Flashlight_size))
    if drink == 12:
            Flashing_light12 = pygame.draw.ellipse(window, Flashlight_on_colour , (1831, 719, Flashlight_size, Flashlight_size))
      
      
      #Cup selection
    S_cup_outerb = pygame.draw.ellipse(window, Grey ,(1715, 892, GButton_size, GButton_size))
    S_cup_innerb = pygame.draw.ellipse(window, Red ,( 1722, 898, Rbutton_size, Rbutton_size)) 
    L_cup_outerb = pygame.draw.ellipse(window, Grey, (1835, 892, GButton_size, GButton_size))                                   
    L_cup_innerb = pygame.draw.ellipse(window, Red , (1842, 898, Rbutton_size, Rbutton_size))
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        mpos = pygame.mouse.get_pos()
        if 1715 < mpos[0] < 1765 and 892 < mpos[1] < 942:
            
    






        



        
            
            
            
    #display update
    pygame.display.update()
    
    #FPS limit
    FPSclock.tick(FPS)

