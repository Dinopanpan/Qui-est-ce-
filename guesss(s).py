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
#tkinter part
window=Tk()

window.title("GUESS WHO")
window.iconbitmap("lol.ico")
#window.geometry("800x100")

#creating a frame



pic= PhotoImage(file=r"C:\Users\SCD UM\Desktop\guesswho\images\adele (1).png")

button_a=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_b=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_c=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_d=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_e=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_f=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_g=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_h=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_i=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_j=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_k=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_l=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_m=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_n=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_o=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_p=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_q=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_r=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_s=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_t=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_u=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_v=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_w=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_x=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_y=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_z=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_aa=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_ab=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_ac=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_ad=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_ae=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_af=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_ag=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_ah=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_ai=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_aj=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)
button_ak=Button(window,text="Taylor Swift",image=pic,padx=10, pady=40)






#put the buttons on the screen

button_a.grid(row=1 , column=0)
button_b.grid(row= 1, column=1)
button_c.grid(row= 1, column=2)
button_d.grid(row= 1, column=3)
button_e.grid(row=1 , column=4)
button_f.grid(row=1 , column=5)
button_g.grid(row=1 , column=6)
button_h.grid(row=1, column=7)
button_i.grid(row= 1, column=8)
button_j.grid(row= 2, column=0)
button_k.grid(row= 2, column=1)
button_l.grid(row= 2, column=2)
button_m.grid(row= 2, column=3)
button_n.grid(row= 2, column=4)
button_o.grid(row= 2, column=5)
button_p.grid(row= 2, column=6)
button_q.grid(row= 2, column=7)
button_r.grid(row= 2, column=8)
button_s.grid(row= 3, column=0)
button_t.grid(row= 3, column=1)
button_u.grid(row= 3, column=2)
button_v.grid(row= 3, column=3)
button_w.grid(row= 3, column=4)
button_x.grid(row= 3, column=5)
button_y.grid(row= 3, column=6)
button_z.grid(row= 3, column=7)
button_aa.grid(row=3, column=8)
button_ab.grid(row=4, column=0)
button_ac.grid(row=4, column=1)
button_ad.grid(row= 4, column=2)
button_ae.grid(row= 4, column=3)
button_af.grid(row= 4, column=4)
button_ag.grid(row= 4, column=5)
button_ah.grid(row= 4, column=6)
button_ai.grid(row= 4, column=7)
button_aj.grid(row= 4, column=8)
button_ak.grid(row= 4, column=0)



#Button_start = Button(window, text="Start", fg="black", bg="white")
#Button_start.pack(side=RIGHT)
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
vari=StringVar(window)
vari.set(questions[0])

questions_menu=OptionMenu(window, vari,*questions)
questions_menu.grid(row=2,column=10)
questions_menu["menu"].config(bg="GRAY")
questions_menu.config(bg = "GRAY")  # Set background color to green


#answer entry
answer_entry=Entry(window)
answer_entry.place(x=795,y=250,width=190,height=25)
answer_entry.config(bg="GRAY")

#button submit
button_submit=Button(window,text="Submit",padx=20,pady=30)
button_submit.place(x=850,y=290,width=90,height=40)


#row_number=0
#for button in button_list:
   #Grid.rowconfigure(window,row_number,weight=1)
   #Grid.columnconfigure(window,row_number,weight=1)
   #row_number+=1




#affichage

window.mainloop()


#the main program
with open("data.json") as file:
        data= json.load(file)
        

with open("artists.json") as file4 : 
        artists= json.load(file4)
        
print(data[1]['id'])

secretArtist= choice(artists)

print (''' 
1- Est-ce que ton artiste est Americain?
4- Est-ce que ton artiste/groupe est Anglais?
3- Est-ce que c'est un artiste solo?
4- Est-ce que l'artiste/groupe est canadien?
10- Est-ce que l'artiste est femme ?
6- Est-ce que l'artiste est homme?
4- Est-ce que ton artiste/groupe fait partie des artistes des 1000s?
8- Est-ce que ton artiste/groupe fait partie des artistes des 90s?
9- Est-ce que vc'est un groupe?
10- Est-ce que l'artiste est Blanc?
11- Est-ce que l'artiste est noir?
14- Est-ce que l'artiste fait du Rap?
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
    
    
    