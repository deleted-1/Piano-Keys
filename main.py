import datetime
import pygame
import mySprites
import json
import time
from tkinter import *


music_sheet = {
    "Mary Had A Little Lamb":{
        "notes":"E D C D E E E D D D E G G E D C D E E E E D D E D C",
        "beats":"1 1 1 1 1 1 2 1 1 2 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 4",
    },
    "Old Mac Donald Had A Farm":{
        "notes":"G G G D E E D B B A A G D G G G D E E D B B A A G",
        "beats":"1 1 1 1 1 1 2 1 1 1 1 2 1 1 1 1 1 1 1 2 1 1 1 1 2"
    }
}

def game(song=None):
    pygame.mixer.pre_init(44100, -16, 50, 512)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.set_num_channels(50)
    keepGoing = True
    screen = pygame.display.set_mode((500, 900), pygame.RESIZABLE)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((47, 102, 191))    
    boolean = False
    white_keys = []
    boolean = []
    
    for i in range(7):
        white_keys.append(mySprites.white_key(72*i,screen)) 
        boolean.append(False)

    keys={
    "q":"C",
    "w":"D",
    "e":"E",
    "r":"F",
    "t":"G",
    "y":"A",
    "u":"B"
    }
    barnote = []
    barsize = []
    iterator = 0
    for beat in music_sheet[song]["beats"].split(" "):
        barsize.append([30*(float(int(beat))),0-135*iterator])
        iterator += 1

    iterator = 0
    for note in music_sheet[song]["notes"].split():
        barnote.append(mySprites.bar_notes( list(keys.values()).index(note)*72 , barsize[iterator][1] , [70,barsize[iterator][0]] , screen ))
        iterator += 1

    score = 0
    past_time = datetime.datetime.utcnow()
    keys_played = []
     
    while keepGoing:
        time.sleep(0.001)
        
        screen.blit(background,(0,0)) 
        present_time = datetime.datetime.utcnow()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                keepGoing = False
                
            if event.type == pygame.KEYDOWN:
                key_to_play = str(event.unicode)
                if key_to_play.lower() in keys.keys():
                    index = list(keys).index(key_to_play)
                    boolean[index] = True
                    
                    for i in range(len(barnote)-1):
                        if barnote[i].location[1] <= 726:
                            if barnote[i].location[1] <= 726 and barnote[i].location[1] >= 646:
                                if boolean[int((barnote[i].location[0]+72)/72-1)]:
                                    score += 10
                            break
                            
    
                    key_to_play = pygame.mixer.Sound('{}.wav'.format(keys[str(key_to_play.lower()).split(' ')[0]]))
                    try:
                        pygame.mixer.find_channel().queue(key_to_play)
                    except AttributeError:   print("Error. Slow down.")
    
            if event.type == pygame.KEYUP:  
                key_realesed = pygame.key.name(event.key)
                
                if key_realesed.lower() in list(keys):
                    index = list(keys).index(key_realesed)
                    boolean[index] = False

        if barnote[len(barnote)-1].location[1] > 726:
            font = pygame.font.Font('freesansbold.ttf',20)
            score = 'YOUR FINAL SCORE IS '+str(score)
            score = font.render(score, True,[255,0,0])
            screen.blit(score, [150,400])
            pygame.display.flip()
            time.sleep(5)
            pygame.quit()
            main()

        for i in range(len(barnote)):
            barnote[i].draw(1.5)
            
        for i in range(7):
            white_keys[i].draw(boolean[i]) 

        pygame.display.flip()



class main:    
    def __init__(self):
        self.window = Tk()
        self.window.title("Welcome!")
        self.window.geometry("600x600+0+0")

        Label(self.window , text="Enter A Song" , font=("Comic Sans MS",35)).place(x=125,y=100)
        self.chosen_song = Entry(self.window , width=70)
        self.chosen_song.pack()
        self.chosen_song.place(x=70,y=180)

        def song_window():
            self.song_window = Tk()
            self.song_window.title("Songs")
            self.song_window.geometry("300x300+600+0")
            iteration = 1
            song_list = open("songs.txt","r")
            for line in song_list:
                Label(self.song_window , text=line.strip() , font=("timesnewroman",12)).place(x=10,y=-5+(25*iteration))
                iteration += 1
        song_window()

        def run():
            chosen_song = str(self.chosen_song.get())
            if chosen_song in list(music_sheet.keys()):
                self.window.destroy()
                self.song_window.destroy()
                game(chosen_song) 

        Button(self.window, text='Quit', width=5, command=self.window.quit).place(x=70,y=200)
        Button(self.window, text='Play', width=5, command=run).place(x=150,y=200)
        """Button(self.window, text="Controls", width=5, command=controls).place(x=230,y=200)
        Button(self.window, text="Leaderboard", width=5, command=controls).place(x=310,y=200)"""


        mainloop()

main()
pygame.quit()