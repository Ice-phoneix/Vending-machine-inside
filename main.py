# frame work and libraries
import pygame
import random
import time
import datetime
import sys
# framework start
pygame.init()
pygame.font.init()

#Basic parameters
Resolution_X = 1920
Resolution_Y = 1090
Red = (210, 4, 45)
Darker_red = (153, 0, 0) 
Grey = (160,160,160)  
White = (255, 255, 255)
Black = (0, 0, 0)
Background = pygame.image.load('Images/Game background.jpg')
Icon = pygame.image.load('Images/Game icon.jpg')
Lcup_load = pygame.image.load('Images/Lcup.png')
Scup_load = pygame.image.load('Images/Scup.png')
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
FPS = 15
showLcup = False
showScup = False
Lsend = False
Ssend = False 
Lcup_xpos = 700
Scup_xpos = 700
Lcup_ypos = 390
speed = 10
Drink_button_size = 34
my_font = pygame.font.SysFont('arial', 30)

Water_bS = True 
Water_bL = True 
Milk_bS = True 
Milk_bL = True 
Coffe_bS = True 
Coffe_bL = True 
Choco_bS = True 
Choco_bL = True 
Gtea_bS = True 
Gtea_bL = True 
Blacktea_bS = True 
Blacktea_bL = True 
Juice_bS = True 
Juice_bL = True

Water_bS_ON = False  
Water_bL_ON = False 
Milk_bS_ON = False 
Milk_bL_ON = False 
Coffe_bS_ON = False 
Coffe_bL_ON = False 
Choco_bS_ON = False 
Choco_bL_ON = False 
Gtea_bS_ON = False 
Gtea_bL_ON = False
Blacktea_bS_ON = False 
Blacktea_bL_ON = False
Juice_bS_ON = False 
Juice_bL_ON = False 
#Window creation
window = pygame.display.set_mode((Resolution_X, Resolution_Y))
pygame.display.set_caption('Vending machine game')
pygame.display.set_icon(Icon)

#FPS clock
FPSclock = pygame.time.Clock() 

#subprograms
 
    



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
        if 1835 < mpos[0] < 1885 and 892 < mpos[1] < 942:
            showLcup = True
    
    if showLcup:
        window.blit(Lcup_load, (Lcup_xpos, Lcup_ypos))
        
        
        
    if event.type == pygame.MOUSEBUTTONDOWN:
        mpos = pygame.mouse.get_pos()
        if 1715 < mpos[0] < 1765 and 892 < mpos[1] < 942:
            showScup = True
    if showScup:
         window.blit(Scup_load, (Scup_xpos, 525))
        
     #cup sending
    pygame.draw.rect(window, Grey, (1000, 722, 60, 60))
    pygame.draw.line(window, Black, [935, 750], [1000, 750], 10)
    pygame.draw.ellipse(window, Red,(1005,726, 50, 50))
    
    if event.type == pygame.MOUSEBUTTONDOWN and showLcup == True: 
        mpos = pygame.mouse.get_pos()
        if 1000 < mpos[0] < 1060 and 722 < mpos[1] < 782:
            Lsend = True 
    if Lsend == True:
        if (Lcup_xpos + 206) > 0:
            Lcup_xpos -= speed
        if (Lcup_xpos + 206) < 0: 
            showLcup = False
            Lsend = False 
            Lcup_xpos = 700
    if event.type == pygame.MOUSEBUTTONDOWN and showScup == True:
        mpos = pygame.mouse.get_pos()
        if 1000 < mpos[0] < 1060 and 722 < mpos[1] < 782:
            Ssend = True 
    if Ssend == True:
        if (Scup_xpos + 168) > 0:
            Scup_xpos -= speed
        if (Scup_xpos + 168) < 5:
            showScup = False
            Ssend = False
            Scup_xpos = 700
            
    #Drinks making
        #Buttons
    if Water_bS == True:
        pygame.draw.ellipse(window, Red, (15, 75, Drink_button_size, Drink_button_size))
    if Water_bL == True:
        pygame.draw.ellipse(window, Red, (65, 75, Drink_button_size, Drink_button_size))
    if Milk_bS == True:
        pygame.draw.ellipse(window, Red, (122, 75, Drink_button_size, Drink_button_size))
    if Milk_bL == True:
        pygame.draw.ellipse(window, Red, (175, 75, Drink_button_size, Drink_button_size))
    if Coffe_bS == True:
        pygame.draw.ellipse(window, Red, (240, 75, Drink_button_size, Drink_button_size))
    if Coffe_bL == True:
        pygame.draw.ellipse(window, Red, (295, 75, Drink_button_size, Drink_button_size))
    if Choco_bS == True:
        pygame.draw.ellipse(window, Red, (360, 75, Drink_button_size, Drink_button_size))
    if Choco_bL == True:
        pygame.draw.ellipse(window, Red, (415, 75, Drink_button_size, Drink_button_size))
    if Gtea_bS == True:
        pygame.draw.ellipse(window, Red, (484, 75, Drink_button_size, Drink_button_size))
    if Gtea_bL == True:
        pygame.draw.ellipse(window, Red, (540, 75, Drink_button_size, Drink_button_size))
    if Blacktea_bS == True:
        pygame.draw.ellipse(window, Red, (610, 75, Drink_button_size, Drink_button_size))
    if Blacktea_bL == True:
        pygame.draw.ellipse(window, Red, (664, 75, Drink_button_size, Drink_button_size))
    if Juice_bS == True:
        pygame.draw.ellipse(window, Red, (730, 75, Drink_button_size, Drink_button_size))
    if Juice_bL == True:
        pygame.draw.ellipse(window, Red, (785, 75, Drink_button_size, Drink_button_size))
        
        
    if Water_bS_ON == True :
        pygame.draw.ellipse(window, Darker_red, (15, 75, Drink_button_size, Drink_button_size))
    if Water_bL_ON == True:
        pygame.draw.ellipse(window, Darker_red, (65, 75, Drink_button_size, Drink_button_size))
    if Milk_bS_ON == True:
        pygame.draw.ellipse(window, Darker_red, (122, 75, Drink_button_size, Drink_button_size))
    if Milk_bL_ON == True:
        pygame.draw.ellipse(window, Darker_red, (175, 75, Drink_button_size, Drink_button_size))
    if Coffe_bS_ON == True:
        pygame.draw.ellipse(window, Darker_red, (240, 75, Drink_button_size, Drink_button_size))
    if Coffe_bL_ON == True:
        pygame.draw.ellipse(window, Darker_red, (295, 75, Drink_button_size, Drink_button_size))
    if Choco_bS_ON == True:
        pygame.draw.ellipse(window, Darker_red, (360, 75, Drink_button_size, Drink_button_size))
    if Choco_bL_ON == True:
        pygame.draw.ellipse(window, Darker_red, (415, 75, Drink_button_size, Drink_button_size))
    if Gtea_bS_ON == True:
        pygame.draw.ellipse(window, Darker_red, (484, 75, Drink_button_size, Drink_button_size))
    if Gtea_bL_ON == True:
        pygame.draw.ellipse(window, Darker_red, (540, 75, Drink_button_size, Drink_button_size))
    if Blacktea_bS_ON == True:
        pygame.draw.ellipse(window, Darker_red, (610, 75, Drink_button_size, Drink_button_size))
    if Blacktea_bL_ON == True:
        pygame.draw.ellipse(window, Darker_red, (664, 75, Drink_button_size, Drink_button_size))
    if Juice_bS_ON == True:
        pygame.draw.ellipse(window, Darker_red, (730, 75, Drink_button_size, Drink_button_size))
    if Juice_bL_ON == True:
        pygame.draw.ellipse(window, Darker_red, (785, 75, Drink_button_size, Drink_button_size))

    WaterS = my_font.render('S', False, (0, 0, 0))
    window.blit(WaterS, (22,40))    
    MilkS = my_font.render('S', False, (0, 0, 0))
    window.blit(MilkS, (129, 40))  
    CoffeS = my_font.render('S', False, (0, 0, 0))
    window.blit(CoffeS, (247, 40))   
    ChocoS = my_font.render('S', False, (0, 0, 0))
    window.blit(ChocoS, (367, 40))    
    GteaS = my_font.render('S', False, (0, 0, 0))
    window.blit(GteaS, (491, 40))
    BteaS = my_font.render('S', False, (0, 0, 0))
    window.blit(BteaS, (617, 40))
    JuiceS = my_font.render('S', False, (0, 0, 0))
    window.blit(JuiceS, (737, 40))
    WaterL = my_font.render('L', False, (0, 0, 0))
    window.blit(WaterL, (74, 40))
    MilkL = my_font.render('L', False, (0, 0, 0))
    window.blit(MilkL, (185, 40))
    CoffeL = my_font.render('L', False, (0, 0, 0))
    window.blit(CoffeL, (305, 40))
    ChocoL = my_font.render('L', False, (0, 0, 0))
    window.blit(ChocoL, (425, 40))
    GteaL = my_font.render('L', False, (0, 0, 0))
    window.blit(GteaL, (550, 40))
    BteaL = my_font.render('L', False, (0, 0, 0))
    window.blit(BteaL, (673, 40))
    JuiceL = my_font.render('L', False, (0, 0, 0))
    window.blit(JuiceL, (794, 40))
    
    #On / off buttons
    if event.type == pygame.MOUSEBUTTONDOWN:
        mpos = pygame.mouse.get_pos()
        if 15 < mpos[0] < 49 and 75 < mpos[1] < 109:
            Water_bS_ON = True
            Water_bS = False
        if Water_bL_ON == True:
            Water_bL = True
            Water_bL_ON = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        mpos = pygame.mouse.get_pos()
        if 65 < mpos[0] < 99 and 75 < mpos[1] < 109:
            Water_bL_ON = True
            Water_bL = False
        if Water_bS_ON == True:
            Water_bS = True 
            Water_bS_ON = False 
    
        
    
    
    
    
    
    
    
        
        
          
 
            
            
    
    
    
  
            
    






        



        
            
            
            
    #display update
    pygame.display.update()
    
    #FPS limit
    FPSclock.tick(FPS)

