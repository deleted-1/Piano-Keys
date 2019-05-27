import pygame as pg 
from tkinter import *
song_list = open("songs.txt","r")
pg.init()
pg.font.init()

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
            for line in song_list:
                Label(self.song_window , text=line.strip() , font=("timesnewroman",12)).place(x=10,y=-5+(25*iteration))
                iteration += 1
        song_window()

        def run():
            if str(chosen_song.get()) !== "Mary Had A Little Lamb": return;
            game()

        Button(self.window, text='Quit', width=5, command=self.window.quit).place(x=70,y=200)
        Button(self.window, text='Play', width=5, command=run).place(x=150,y=200)

        mainloop()

    def game():
        screen = pg.display.set_mode((1000,900), pg.RESIZABLE)
        pg.display.set_caption("Piano Keys")

        

main()


        
        

 