# Import and Initialize
import datetime
import pygame
import mySprites
import time
from tkinter import *
pygame.mixer.pre_init(44100, -16, 50, 512)
pygame.init()
pygame.mixer.init()

music_sheet = {
        "Mary Had A Little Lamb":{
            "notes":"E D C D E E E D D D E G G E D C D E E E E D D E D C",
            "beats":"1 1 1 1 1 1 2 1 1 2 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 4",
        },
        "Old Mac Donald Had A Farm":{
            "notes":"G G G D E E D B B A A G D G G G D E E D B B A A G",
            "beats":"1 1 1 1 1 1 2 1 1 1 1 2 1 1 1 1 1 1 1 2 1 1 1 1 2"
        },
        "Sandbox":{
            "notes":"M",
            "beats":"0"
        }
    }
def game(song=None):
    """
    Takes the song/mode that was inputted
    and prepares the game to play.
    """
    pygame.mixer.set_num_channels(50)
    keepGoing = True
    # Display configuration
    screen = pygame.display.set_mode((500, 900), pygame.RESIZABLE)
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
    "u":"B",
    "2":"C#",
    "3":"D#",
    "5":"F#",
    "6":"G#",
    "7":"A#"
    }
    # Assign values to key variables
    barnote = []
    barsize = []
    iterator = 0
    if song != "Sandbox":
        for beat in music_sheet[song]["beats"].split(" "):
            barsize.append([30*(float(int(beat))),0-135*iterator])
            iterator += 1

        iterator = 0
        for note in music_sheet[song]["notes"].split():
            barnote.append(mySprites.bar_notes( list(keys.values()).index(note)*72 , barsize[iterator][1] , [70,barsize[iterator][0]] , screen ))
            iterator += 1

    past_time = datetime.datetime.utcnow()
    black_keys = []
    font_key = pygame.font.Font('freesansbold.ttf',25) 
    for i in range(7):
        if i == 2: continue
        black_keys.append(mySprites.black_key(72*(i+1)-(20),screen))
        boolean.append(False)

    font = pygame.font.Font('freesansbold.ttf',20) 

    score_board = mySprites.score_board()

    # Entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((47, 102, 191))    
    # Loop
    while keepGoing:
        # Timer to set frame rate
        
        time.sleep(0.001)
        screen.blit(background,(0,0)) 
        present_time = datetime.datetime.utcnow()

        # Event Handling
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                keepGoing = False
                
            if event.type == pygame.KEYDOWN:
                key_to_play = str(event.unicode)
                if key_to_play.lower() in keys.keys():
                    index = list(keys).index(key_to_play.lower())
                    boolean[index] = True
                    
                    if song != 'Sandbox':
                        for i in range(len(barnote)-1):
                            if barnote[i].location[1] <= 736:
                                if barnote[i].location[1] <= 736 and barnote[i].location[1] >= 636:
                                    if boolean[int((barnote[i].location[0]+72)/72-1)]:
                                        score_board.add_score()
                                    else: score_board.add_score(-25)
                                break
                            
    
                    key_to_play = pygame.mixer.Sound('{}.wav'.format(keys[str(key_to_play.lower())]))
                    try:
                        pygame.mixer.find_channel().queue(key_to_play)
                    except AttributeError:   print("Error. Slow down.")
    
            if event.type == pygame.KEYUP:  
                key_realesed = pygame.key.name(event.key)
                
                if key_realesed.lower() in list(keys):
                    index = list(keys).index(key_realesed)
                    boolean[index] = False

        # Refresh Display
        if song != 'Sandbox':
            if barnote[len(barnote)-1].location[1] > 726:
                score_board.end_screen(screen)
                time.sleep(5)
                pygame.quit()
                main()
        elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            main()
        else:
            exit_name = font.render('ESC to exit', True,(255,255,0))
            screen.blit(exit_name, [350,50])

        for i in range(len(barnote)):
            barnote[i].draw(1.5)
            
        for i in range(7):
            white_keys[i].draw(boolean[i]) 
            key_name = font_key.render(list(keys)[i], True,[0,0,0])
            screen.blit(key_name, [30+(72*i),686+117])
  
        for i in range(5):
            black_keys[i].draw(boolean[7+i])
            key_name = font.render(list(keys)[i+7], True,[255,255,255])
            if i >= 2: i += 1
            screen.blit(key_name, [65+(72*i),730])

        score_board.display(screen)
        pygame.display.flip()

class main:
    """
    Creates tkinter window
    the user inputs a song
    in here
    """   
    def __init__(self):
        self.window = Tk()
        self.window.title("Welcome to Piano Keys!")
        self.window.geometry("400x200+0+0")

        self.mainframe = Frame(self.window)
        self.mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
        self.mainframe.columnconfigure(0, weight = 1)
        self.mainframe.rowconfigure(0, weight = 1)
        self.mainframe.pack(pady = 20, padx = 20)
        self.chosen_song = StringVar(self.mainframe)
        
        choices = {'Mary Had A Little Lamb','Old Mac Donald Had A Farm','Sandbox'}
        self.chosen_song.set('Sandbox')

        popupMenu = OptionMenu(self.mainframe,self.chosen_song,*choices)
        Label(self.mainframe, text="Choose a song").grid(row=1,column=1)
        popupMenu.grid(row=2,column=1)

        def run():
            chosen_song = str(self.chosen_song.get())
            if chosen_song in list(music_sheet.keys()) or chosen_song == 'Sandbox':
                self.window.destroy()
                game(chosen_song) 


        Button(self.window, text='Quit', width=5, command=self.window.quit).place(x=200,y=100)
        Button(self.window, text='Play', width=5, command=run).place(x=150,y=100)

        self.window.mainloop()

main()
pygame.quit()