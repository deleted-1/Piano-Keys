import pygame

class white_key(pygame.sprite.Sprite):
    def __init__(self,x,screen):
        self.screen = screen
        self.x = x
        self.boolean = False
        pygame.sprite.Sprite.__init__(self)

    def draw(self,boolean):
        self.boolean = boolean
        if self.boolean: self.key = pygame.draw.rect(self.screen, (255,0,0), pygame.Rect(self.x,686,70,214))
        else:   self.key = pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(self.x,686,70,214))

    def isPressed(self):
        return self.boolean

class black_key(pygame.sprite.Sprite):
    def __init__(self,x,screen):
        self.screen = screen
        self.x = x
        pygame.sprite.Sprite.__init__(self)
    
    def isPressed(self,boolean=False):
        if boolean: self.key = pygame.draw.rect(self.screen, (255,0,0), pygame.Rect(self.x,686,70,214))
        else:   self.key = pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(self.x,686,70,214))

class bar_notes(pygame.sprite.Sprite):
    def __init__(self,coloumn,row,size,screen):
        self.size = size
        self.screen = screen
        self.location = [coloumn,row]
        pygame.sprite.Sprite.__init__(self)
    
    def draw(self,speed):   
        self.location[1] += speed
        pygame.draw.rect(self.screen,(0,0,0),pygame.Rect(self.location[0],self.location[1], self.size[0], self.size[1] ) )