from sqlite3 import Row
from tkinter import *
from tkinter.tix import Button
from cProfile import label
from cgitb import text
from tkinter import*
from asyncore import read
from random import random
from random import choice
from tkinter import font
from tkinter import filedialog
from unicodedata import name
import json
from sqlite3 import Row

from tkinter.tix import Button



class ImageButton(Button):
        
            def __init__(self, master, image1, image2, *args, **kwargs ):
                self.unclickedImage = PhotoImage(file = image1)
                self.clickedImage = PhotoImage(file = image2)
                
                super().__init__(master, *args, image = self.unclickedImage, **kwargs)
                self.toggleState = 1
                self.bind("<Button-1>", self.clickFunction)
            def clickFunction(self, event = None):
                if self.cget("state") != "disabled": #Ignore click if button is disabled
                    self.toggleState *= -1
                    if self.toggleState == -1:
                        self.config(image = self.clickedImage)
                    else:
                        self.config(image = self.unclickedImage)
def call():

    return

class Example(Frame):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.init_ui()
   

    def init_ui(self):
         for i in range (0,4):
             for j in range (0,7):
                ImageButton(self, "pics\_abba.png", "pics\_abbax.png").grid(row=0, column=1)
                ImageButton(self, "pics\_adele.png", "pics\_adeleX.png").grid(row=0, column=2)
                ImageButton(self, "pics\_aliciacara.png", "pics\_aliciacaraX.png").grid(row=0, column=3)
                ImageButton(self, "pics\_avrilelavigne.png", "pics\_avrilelavigneX.png").grid(row=0, column=4)
                ImageButton(self, "pics\_blacksabbath.png", "pics\_blacksabbathX.png").grid(row=0, column=5)
                ImageButton(self, "pics\_bryanadams.png", "pics\_bryanadamsX.png").grid(row=0, column=6)
                ImageButton(self, "pics\celinedion.png", "pics\celinedionX.png").grid(row=0, column=7) 
                ImageButton(self, "pics\drake.png", "pics\drakeX.png").grid(row=1, column=1) 
                ImageButton(self, "pics\dualipa.png", "pics\dualipaX.png").grid(row=1, column=2)
                ImageButton(self, "pics\edsheeran.png", "pics\edsheeranX.png").grid(row=1, column=3)
                ImageButton(self, "pics\elvispresley.png", "pics\elvispresleyX.png").grid(row=1, column=4) 
                ImageButton(self, "pics\eminem.png", "pics\eminemX.png").grid(row=1, column=5)
                ImageButton(self, "pics\_fleetwoodmac.png", "pics\_fleetwoodmacX.png").grid(row=1, column=6)
                ImageButton(self, "pics\harrystyles.png", "pics\harrystylesX.png").grid(row=1, column=7)
                ImageButton(self, "pics\jamesbrown.png", "pics\jamesbrownX.png").grid(row=2, column=1)
                ImageButton(self, "pics\janisjoplin.png", "pics\janisjoplinX.png").grid(row=2, column=2)
                ImageButton(self, "pics\jimmihendrix.png", "pics\jimmihendrixX.png").grid(row=2, column=3)
                ImageButton(self, "pics\justinbieber.png", "pics\justinbieberX.png").grid(row=2, column=4)
                ImageButton(self, "pics\littlemix.png", "pics\littlemixX.png").grid(row=2, column=5)
                ImageButton(self, "pics\macmiller.png", "pics\macmillerX.png").grid(row=2, column=6)
                ImageButton(self, "pics\_nickiminaj.png", "pics\_nickiminajX.png").grid(row=2, column=7)
                ImageButton(self, "pics\_nirvana.png", "pics\_nirvanaX.png").grid(row=3, column=1)
                ImageButton(self, "pics\onedirection.png", "pics\onedirectionX.png").grid(row=3, column=2)
                ImageButton(self, "pics\philcollins.png", "pics\philcollinsX.png").grid(row=3, column=3)
                ImageButton(self, "pics\queen.png", "pics\queenX.png").grid(row=3, column=4)
                ImageButton(self, "pics\snoopdog.png", "pics\snoopdogX.png").grid(row=3, column=5)
                ImageButton(self, "pics\spicegirls.png", "pics\spicegirlsX.png").grid(row=3, column=6)
                ImageButton(self, "pics\steviewonder.png", "pics\steviewonderX.png").grid(row=3, column=7)
               

                    


def main():

    root=Tk()
    root.configure(bg='black')
    ex =Example(root)
    ex.grid()
    root.title('')
    questions=["1- Est-ce que ton artiste est Americain?",
    "2- Est-ce que ton artiste/groupe est Anglais?",
    "3- Est-ce que c'est un artiste solo?",
    "4- Est-ce que l'artiste/groupe est canadien?",
    "5- Est-ce que l'artiste est femme ?",
    "6- Est-ce que l'artiste est homme?",
    "7- Est-ce que ton artiste/groupe fait partie des artistes des 1000s?",
    "8- Est-ce que ton artiste/groupe fait partie des artistes des 90s?",
    "9- Est-ce que vc'est un groupe?",
    "10- Est-ce que l'artiste est Blanc?",
    "11- Est-ce que l'artiste est noir?",
    "12- Est-ce que l'artiste fait du Rap?",
    "13- Est-ce que l'artiste fait du pop?",
    ]

    vari=StringVar(root)
    vari.set(questions[0])

    questions_menu=OptionMenu(root, vari,*questions)
    questions_menu.grid(row=3, column=1)
    questions_menu["menu"].config(bg="GRAY")
    questions_menu.config(bg = "GRAY")  # Set background color to green


    #answer entry
    answer_entry=Entry(root)
    answer_entry.place(x=795,y=250,width=190,height=25)
    answer_entry.config(bg="GRAY")

    #button submit
    button_submit=Button(root,text="Submit",padx=20,pady=30)
    button_submit.place(x=850,y=290,width=90,height=40)
    root.mainloop()               


    



if __name__ == '__main__':
    main()