from datetime import datetime
import pygame as pg
import asyncio
import string
from msvcrt import getch
playable = {'a'}

pg.init()
pg.mixer.init()

def game():
    keepGoing = True
    
    while keepGoing:
        key = getch()
        for event in pg.event.get():
            if event == pg.QUIT():  keepGoing = False
    
        if key in string.ascii_lowercase and key in playable:   sound = pg.mixer.Sound('piano_{}.wav'.format(key.toUpperCase()))
            
        
   
                    
                    
                    

def play_sound():
    pass

