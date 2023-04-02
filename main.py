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
Malfuction_image = pygame.image.load('Images/Malfuction.png') 
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
nbutton = False
Off_button = 15
Make_BY = 350
Makerspeed = 5
Maker_Down_S = False
Maker_Down_L = False 
Miliseconds_S = 1000
Maker_UP = pygame.USEREVENT + 1
MAKER_UPP = False 
Money = 999
Malfuction_message = 'Something'
Malfuction_show = True 
#Window creation
window = pygame.display.set_mode((Resolution_X, Resolution_Y))
pygame.display.set_caption('Vending machine game')
pygame.display.set_icon(Icon)

#FPS clock
FPSclock = pygame.time.Clock() 

#subprograms
 
def Malfuction():
    Malfuction_show = True
    if Malfuction_show == True:
        window.blit(Malfuction_image, (1050, 350))
        pygame.draw.rect(window, Red,(1177, 532, 301, 99))
        Repair_message = my_font.render('Repair', False, (0, 0, 0))
        window.blit(Repair_message, (1275,550))
        Repair_cost = my_font.render('(10Kč)', False, (0, 0, 0))
        window.blit(Repair_cost, (1275, 580))
    if event.type == pygame.MOUSEBUTTONDOWN and Malfuction_show == True:
        mpos = pygame.mouse.get_pos()
        if 1177 < mpos[0] < 1478 and 532 < mpos[1] < 631:
            if Money > 10:
                Malfuction_show = False
                Money - 10 

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
    
    
    #Next button
    Next_button = pygame.draw.ellipse(window, Red, (1788, 810, 35 , 35))
    if event.type == pygame.MOUSEBUTTONDOWN:
        Malfuction_Chance = random.randint(1,100)
        if Malfuction_Chance == 69:
            Malfuction()
        mpos = pygame.mouse.get_pos()
        if 1788 < mpos[0] < 1823 and 810 < mpos[1] < 845:
            nbutton = True 
            drink = random.randint(1,12)


    if nbutton == True:
        
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
        Malfuction_Chance = random.randint(1,100)
        if Malfuction_Chance == 69:
            Malfuction()
        mpos = pygame.mouse.get_pos()
        if 1835 < mpos[0] < 1885 and 892 < mpos[1] < 942:
            showLcup = True
    
    if showLcup:
        window.blit(Lcup_load, (Lcup_xpos, Lcup_ypos))
        
        
        
    if event.type == pygame.MOUSEBUTTONDOWN:
        Malfuction_Chance = random.randint(1,100)
        if Malfuction_Chance == 69:
            Malfuction()
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
        Malfuction_Chance = random.randint(1,2)
        if Malfuction_Chance == 69:
            Malfuction()
        mpos = pygame.mouse.get_pos()
        if 1000 < mpos[0] < 1060 and 722 < mpos[1] < 782:
            Lsend = True 
    if Lsend == True:
        if (Lcup_xpos + 206) > 0:
            Lcup_xpos -= speed
        if (Lcup_xpos + 206) < 0: 
            showLcup = False
            Lsend = False
            nbutton = False 
            Lcup_xpos = 700
    if event.type == pygame.MOUSEBUTTONDOWN and showScup == True:
        Malfuction_Chance = random.randint(1,100)
        if Malfuction_Chance == 69:
            Malfuction()
        mpos = pygame.mouse.get_pos()
        if 1000 < mpos[0] < 1060 and 722 < mpos[1] < 782:
            Ssend = True 
    if Ssend == True:
        if (Scup_xpos + 168) > 0:
            Scup_xpos -= speed
        if (Scup_xpos + 168) < 5:
            showScup = False
            Ssend = False
            nbutton = False 
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
        Malfuction_Chance = random.randint(1,100)
        if Malfuction_Chance == 69:
            Malfuction()
        if 15 < mpos[0] < 49 and 75 < mpos[1] < 109:
            Water_bS_ON = True
            Water_bS = False
            Water_bL = True
            Water_bL_ON = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        Malfuction_Chance = random.randint(1,100)
        if Malfuction_Chance == 69:
            Malfuction()
        mpos = pygame.mouse.get_pos()
        if 65 < mpos[0] < 99 and 75 < mpos[1] < 109:
            Water_bL_ON = True
            Water_bL = False
            Water_bS = True 
            Water_bS_ON = False
            
    if event.type == pygame.MOUSEBUTTONDOWN:
        Malfuction_Chance = random.randint(1,100)
        if Malfuction_Chance == 69:
            Malfuction()
        mpos = pygame.mouse.get_pos()
        if 122 < mpos[0] < 156 and 75 < mpos[1] < 109:
            Milk_bS_ON = True
            Milk_bS = False
            Milk_bL = True
            Milk_bL_ON = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        Malfuction_Chance = random.randint(1,100)
        if Malfuction_Chance == 69:
            Malfuction()
        mpos = pygame.mouse.get_pos()
        if 175 < mpos[0] < 209 and 75 < mpos[1] < 109:
            Milk_bL_ON = True
            Milk_bL = False
            Milk_bS = True
            Milk_bS_ON = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        Malfuction_Chance = random.randint(1,100)
        if Malfuction_Chance == 69:
            Malfuction()
        mpos = pygame.mouse.get_pos()
        if 240 < mpos[0] < 274 and 75 < mpos[1] < 109:
            Coffe_bS_ON = True
            Coffe_bS = False
            Coffe_bL = True
            Coffe_bL_ON = False
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        Malfuction_Chance = random.randint(1,100)
        if Malfuction_Chance == 69:
            Malfuction()
        mpos = pygame.mouse.get_pos()
        if 295 < mpos[0] < 329 and 75 < mpos[1] < 109:
            Coffe_bL_ON = True
            Coffe_bL = False
            Coffe_bS = True
            Coffe_bS_ON = False
            
    if event.type == pygame.MOUSEBUTTONDOWN:
        Malfuction_Chance = random.randint(1,100)
        if Malfuction_Chance == 69:
            Malfuction()
        mpos = pygame.mouse.get_pos()
        if 360 < mpos[0] < 394 and 75 < mpos[1] < 109:
            Choco_bS_ON = True
            Choco_bS = False
            Choco_bL = True
            Choco_bL_ON = False
            
    if event.type == pygame.MOUSEBUTTONDOWN:
        Malfuction_Chance = random.randint(1,100)
        if Malfuction_Chance == 69:
            Malfuction()
        mpos = pygame.mouse.get_pos()
        if 415 < mpos[0] < 449 and 75 < mpos[1] < 109:
            Choco_bL_ON = True
            Choco_bL = False
            Choco_bS = True
            Choco_bS_ON = False
            
    if event.type == pygame.MOUSEBUTTONDOWN:
        Malfuction_Chance = random.randint(1,100)
        if Malfuction_Chance == 69:
            Malfuction()
        mpos = pygame.mouse.get_pos()
        if 484 < mpos[0] < 518 and 75 < mpos[1] < 109:
            Gtea_bS_ON = True
            Gtea_bS = False
            Gtea_bL = True
            Gtea_bL_ON = False
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        Malfuction_Chance = random.randint(1,100)
        if Malfuction_Chance == 69:
            Malfuction()
        mpos = pygame.mouse.get_pos()
        if 540 < mpos[0] < 574 and 75 < mpos[1] < 109:
            Gtea_bL_ON = True
            Gtea_bL = False
            Gtea_bS = True
            Gtea_bS_ON = False
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        Malfuction_Chance = random.randint(1,100)
        if Malfuction_Chance == 69:
            Malfuction()
        mpos = pygame.mouse.get_pos()
        if 610 < mpos[0] < 644 and 75 < mpos[1] < 109:
            Blacktea_bS_ON = True
            Blacktea_bS = False
            Blacktea_bL = True
            Blacktea_bL_ON = False
            
    if event.type == pygame.MOUSEBUTTONDOWN:
        Malfuction_Chance = random.randint(1,100)
        if Malfuction_Chance == 69:
            Malfuction()
        mpos = pygame.mouse.get_pos()
        if 664 < mpos[0] < 698 and 75 < mpos[1] < 109:
            Blacktea_bL_ON = True
            Blacktea_bL = False
            Blacktea_bS = True
            Blacktea_bS_ON = False
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        Malfuction_Chance = random.randint(1,100)
        if Malfuction_Chance == 69:
            Malfuction()
        mpos = pygame.mouse.get_pos()
        if 730 < mpos[0] < 764 and 75 < mpos[1] < 109:
            Juice_bS_ON = True
            Juice_bS = False
            Juice_bL = True
            Juice_bL_ON = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        Malfuction_Chance = random.randint(1,100)
        if Malfuction_Chance == 69:
            Malfuction()
        mpos = pygame.mouse.get_pos()
        if 785 < mpos[0] < 819 and 75 < mpos[1] < 109:
            Juice_bL_ON = True
            Juice_bL = False
            Juice_bS = True
            Juice_bS_ON = False
    
    #Turn off button for drink maker
    pygame.draw.ellipse(window, Red, (49.5, 100, Off_button, Off_button))
    pygame.draw.ellipse(window, Red, (158, 100, Off_button, Off_button))
    pygame.draw.ellipse(window, Red, (277, 100, Off_button, Off_button))
    pygame.draw.ellipse(window, Red, (397, 100, Off_button, Off_button))
    pygame.draw.ellipse(window, Red, (521.5, 100, Off_button, Off_button))
    pygame.draw.ellipse(window, Red, (646.5, 100, Off_button, Off_button))
    pygame.draw.ellipse(window, Red, (767, 100, Off_button, Off_button))
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        mpos = pygame.mouse.get_pos()
        if 49.5 < mpos[0] < 64.5 and 100 < mpos[1] < 115:
            Water_bL = True
            Water_bL_ON = False
            Water_bS = True
            Water_bS_ON = False
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        mpos = pygame.mouse.get_pos()
        if 158 < mpos[0] < 173 and 100 < mpos[1] < 115:
            Milk_bL = True
            Milk_bL_ON = False
            Milk_bS = True
            Milk_bS_ON = False
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        mpos = pygame.mouse.get_pos()
        if 277 < mpos[0] < 292 and 100 < mpos[1] < 115:
            Coffe_bL = True
            Coffe_bL_ON = False
            Coffe_bS = True
            Coffe_bS_ON = False
            
    if event.type == pygame.MOUSEBUTTONDOWN:
        mpos = pygame.mouse.get_pos()
        if 397 < mpos[0] < 412 and 100 < mpos[1] < 115:
            Choco_bL = True
            Choco_bL_ON = False
            Choco_bS = True
            Choco_bS_ON = False
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        mpos = pygame.mouse.get_pos()
        if 521.5 < mpos[0] < 536.5 and 100 < mpos[1] < 115:
            Gtea_bL = True
            Gtea_bL_ON = False
            Gtea_bS = True
            Gtea_bS_ON = False
            
    if event.type == pygame.MOUSEBUTTONDOWN:
        mpos = pygame.mouse.get_pos()
        if 646.5 < mpos[0] < 661.5 and 100 < mpos[1] < 115:
            Blacktea_bL = True
            Blacktea_bL_ON = False
            Blacktea_bS = True
            Blacktea_bS_ON = False
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        mpos = pygame.mouse.get_pos()
        if 767 < mpos[0] < 782 and 100 < mpos[1] < 115:
            Juice_bL = True
            Juice_bL_ON = False
            Juice_bS = True
            Juice_bS_ON = False 

            
    #Make
    pygame.draw.rect(window, Grey, (925, 250, 75, 75))
    pygame.draw.ellipse(window, Red, (933, 257, 60,60))
    Make_B = my_font.render('Make', False, (0, 0, 0))
    window.blit(Make_B, (925, 320))
    pygame.draw.line(window, Black, [825, 290], [925, 290], 7)
    pygame.draw.line(window, Black, [813.5, 290], [813.5, Make_BY], 30)
    
    
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        Malfuction_Chance = random.randint(1,100)
        if Malfuction_Chance == 69:
            Malfuction()
        mpos = pygame.mouse.get_pos()
        if 933 < mpos[0] < 993 and 257 < mpos[1] < 317:
            if Water_bS_ON == True and Coffe_bS_ON == True and Milk_bS_ON == True:
                if showScup == True:
                    Maker_Down_S = True
            elif  Water_bS_ON == True and Gtea_bS_ON == True:
                if showScup == True:
                    Maker_Down_S = True
            elif Water_bS_ON == True  and Choco_bS_ON == True:
                if showScup == True:
                    Maker_Down_S = True
            elif  Juice_bS_ON == True:
                if showScup == True:
                    Maker_Down_S = True
            elif  Water_bS_ON == True  and Blacktea_bS_ON == True:
                if showScup == True:
                    Maker_Down_S = True
            elif  Water_bS_ON == True and Coffe_bS_ON == True:
                if showScup == True:
                    Maker_Down_S = True
                    
            elif Water_bL_ON == True and Coffe_bL_ON == True and Milk_bL_ON == True:
                if showLcup == True:
                    Maker_Down_L = True
            elif Water_bL == True and Gtea_bL_ON == True:
                if showLcup == True:
                    Maker_Down_L = True 
            elif Water_bL_ON == True and Choco_bL_ON == True:
                if showLcup == True:
                    Maker_Down_L = True
            elif Juice_bL_ON == True:
                if showLcup == True:
                    Maker_Down_L = True
            elif Water_bL_ON == True and Blacktea_bL_ON == True:
                if showLcup == True:
                    Maker_Down_L = True
            elif Water_bL_ON == True and Coffe_bL_ON == True:
                if showLcup == True:
                    Maker_Down_L = True
                    
            
                    
    
    if Maker_Down_S == True:
        if Make_BY <= 537:
            Make_BY += Makerspeed
            if Make_BY <= 535:
                pygame.time.set_timer(Maker_UP, 10000)
    
    if event.type == Maker_UP:
        Maker_Down_S = False
        Maker_Down_L = False
        MAKER_UPP = True
    if MAKER_UPP == True:
        if Make_BY >= 300:
            Make_BY -= Makerspeed
            if Make_BY <= 300:
                MAKER_UPP = False 
                
               
    if Maker_Down_L == True:
        if Make_BY <= 412:
            Make_BY += Makerspeed
            if Make_BY <= 410:
                pygame.time.set_timer(Maker_UP, 15000) 
            
            
    if event.type == Maker_UP:
        Maker_Down_S = False
        Maker_Down_L = False
        MAKER_UPP = True
    if MAKER_UPP == True:
        if Make_BY >= 300:
            Make_BY -= Makerspeed
            if Make_BY <= 300:
                MAKER_UPP = False
                
                
                
                
    
    
         
    
    
        
    
    
    
    
    
    
    
        
        
          
 
            
            
    
    
    
  
            
    






        



        
            
            
            
    #display update
    pygame.display.update()
    
    #FPS limit
    FPSclock.tick(FPS)

