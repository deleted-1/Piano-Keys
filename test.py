from datetime import datetime
from pynput.keyboard import Key, Listener
import winsound
import pygame

pygame.init()
keys={
    "q":"C",
    "w":"D",
    "e":"E",
    "r":"F",
    "t":"G",
    "y":"A",
    "u":"B"
}

def game():
    keepGoing = True
    key = -5
    screen = pygame.display.set_mode((1400, 900), pygame.RESIZABLE)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((47, 102, 191))
    
    white_key = pygame.image.load('white_key.png')
    white_key = pygame.transform.scale(white_key,[500,500])
    white_key = white_key.convert()
    

    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.KEYDOWN:
                key = event.unicode
                if key in keys.keys():
                    winsound.PlaySound('piano_{}.wav'.format(keys[str(key).split(' ')[0]]),  winsound.SND_ASYNC)
                
            if event.type == pygame.KEYUP:
                key = -5

        screen.blit(background, (0,0))
        screen.blit(white_key, (100,100))
        pygame.display.flip()
        

game()
    
#


