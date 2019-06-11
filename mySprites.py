import pygame

class white_key(pygame.sprite.Sprite):
    def __init__(self,x,screen):
        self.screen = screen
        self.x = x
        pygame.sprite.Sprite.__init__(self)

    def draw(self,boolean):
        if boolean: self.key = pygame.draw.rect(self.screen, (255,0,0), pygame.Rect(self.x,686,70,214))
        else:   self.key = pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(self.x,686,70,214))

class bar_notes(pygame.sprite.Sprite):
    def __init__(self,coloumn,row,size,screen):
        self.size = size
        self.screen = screen
        self.location = [coloumn,row]
        pygame.sprite.Sprite.__init__(self)
    
    def draw(self,speed):   
        self.location[1] += speed
        pygame.draw.rect(self.screen,(0,0,0),pygame.Rect(self.location[0],self.location[1], self.size[0], self.size[1] ) )

class black_key(pygame.sprite.Sprite):
    def __init__(self,x,screen):
        self.screen = screen
        self.x = x
        pygame.sprite.Sprite.__init__(self)

    def draw(self,boolean):
        if boolean: self.key = pygame.draw.rect(self.screen, (255,0,0), pygame.Rect(self.x,686,40,107))
        else:   self.key = pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(self.x,686,40,107))

class score_board(pygame.sprite.Sprite):
    def __init__(self):
        self.score = 0
    
    def add_score(self,score=10):
        self.score += score

    def display(self,screen):
        font = pygame.font.Font('freesansbold.ttf',20) 
        current_score = font.render(str(self.score), True,[255,0,0])
        screen.blit(current_score, [450,850])

    def end_screen(self,screen):
        file = open('highscore.txt','r')
        high_score = int(file.read())
        file.close()
        print(high_score)
        font = pygame.font.Font('freesansbold.ttf',20) 
        if high_score < self.score:
            file = open('highscore.txt','w')
            file.write(str(self.score))
            file.close()

        high_score = 'HIGHSCORE: {}'.format(high_score)
        high_score = font.render(high_score, True,[255,0,0])
        self.score = 'YOUR FINAL SCORE IS '+str(self.score)
        self.score = font.render(self.score, True,[255,0,0])
        screen.blit(self.score, [100,400])
        screen.blit(high_score, [100,450])
        pygame.display.flip()


        