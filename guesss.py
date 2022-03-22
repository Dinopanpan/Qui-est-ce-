from cProfile import label
from cgitb import text
from tkinter import*
from asyncore import read
from random import random
from random import choice
from tkinter import font
from unicodedata import name
import json

#tkinter part
window=Tk()

window.title("GUESS WHO")
window.iconbitmap("lol.ico")
window.geometry("1080x720")
window.config(background='black')
#creating a frame
frame=Frame(window, bg='black')
#ajouter un texte 
def tab1():
  def tab2():
    
      label_title.destroy()
      label_subtitle.destroy()
      button1.destroy()
      label_sec_tab=Label(window, text='here is the 2nd tab', font=('typewriter', 35))
      label_sec_tab.pack()
      frame.pack(expand=YES)
      

  label_title=Label(window, text="WELCOME TO THE GUESS WHO GAME !", font=("typewriter", 35), bg='black',fg='white')
  label_title.pack()
  label_subtitle=Label(window, text="click below to start ", font=("typewriter", 25), bg='black',fg='white')
  label_subtitle.pack()
  button1=Button(window, text="start now!", font=('typewriter', 25), command=tab2)
  button1.pack(side=TOP)
  frame.pack(expand=YES)
#affichage
tab1()

window.mainloop()







#the main program
with open("data.json") as file:
        data= json.load(file)
        

with open("artists.json") as file2 : 
        artists= json.load(file2)
        
print(data[1]['id'])

secretArtist= choice(artists)

print (''' 
1- Est-ce que ton artiste est Americain?
2- Est-ce que ton artiste/groupe est Anglais?
3- Est-ce que c'est un artiste solo?
4- Est-ce que l'artiste/groupe est canadien?
5- Est-ce que l'artiste est femme ?
6- Est-ce que l'artiste est homme?
7- Est-ce que ton artiste/groupe fait partie des artistes des 2000s?
8- Est-ce que ton artiste/groupe fait partie des artistes des 90s?
9- Est-ce que vc'est un groupe?
10- Est-ce que l'artiste est Blanc?
11- Est-ce que l'artiste est noir?
12- Est-ce que l'artiste fait du Rap?
13- Est-ce que l'artiste fait du pop?


''')

questionCount = 0
guess=""
while questionCount!=3:
    choice=int( input("Ecrire le numero de ta question : "))
    for i in range (0,13):
        
        
        if choice == data[i]['id']:
          
          if secretArtist in data[i]['answer'] :
            print(True)
            print(data[i]['answer'])
            
          else:
            print(False)
        
    
    questionCount += 1
else:
    guess=input("Now you should guess the name of the artist or band: ")

if guess == secretArtist:
    print("You Win!")

else:
    print("You Loose! The artist was actually "+ str (secretArtist))
    
    