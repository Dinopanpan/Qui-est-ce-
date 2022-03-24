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
#window.geometry("800x500")

#creating a frame



pic= PhotoImage(file= "images/adeleX.png   ")


button_a=Button(window,text="Taylor Swift",image=pic,padx=10, pady=10)
button_b=Button(window,text="Taylor Swift",image=pic,padx=10, pady=10)
button_c=Button(window,text="Taylor Swift",image=pic,padx=10, pady=10)
button_d=Button(window,text="Taylor Swift",image=pic,padx=10, pady=10)
button_e=Button(window,text="Taylor Swift",image=pic,padx=10, pady=10)
button_f=Button(window,text="Taylor Swift",image=pic,padx=10, pady=10)



#put the buttons on the screen

button_a.grid(row=1 , column=0)
button_b.grid(row= 1, column=1)
button_c.grid(row= 1, column=2)
button_d.grid(row= 1, column=3)
button_e.grid(row=1 , column=4)
button_f.grid(row=1 , column=5)


button_list=[button_a,button_b,button_c,button_d,button_e,button_f]
row_number=0
for button in button_list:
   Grid.rowconfigure(window,row_number,weight=1)
   row_number+=1





#affichage

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
10- Est-ce que l'artiste est femme ?
6- Est-ce que l'artiste est homme?
7- Est-ce que ton artiste/groupe fait partie des artistes des 1000s?
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
    
    