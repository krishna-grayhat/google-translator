from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


def change(text="type",src="english",dest="Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text


def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = sor_txt.get(1.0,END)
    textget = change(text=masg,src=s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)






root = Tk()
root.title("Translator")
root.geometry("500x600")
root.config(bg='red')

lab_txt=Label(root,text="Translator", font=("Time New Roman",40,"bold"),bg="white")
lab_txt.place(x=53,y=40,height=60,width=400)

frame = Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="Source Text", font=("Time New Roman",20,"bold"),fg="black")
lab_txt.place(x=100,y=130,height=25,width=300)

sor_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
sor_txt.place(x=10,y=170,height=100,width=480)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=285,height=40,width=150)
comb_sor.set("english")

button_change = Button(frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=170,y=285,height=40,width=160)

comb_dest = ttk.Combobox(frame,value=list_text)
comb_dest.place(x=340,y=285,height=40,width=150)
comb_dest.set("english")

lab_txt=Label(root,text="Result", font=("Time New Roman",20,"bold"),fg="black")
lab_txt.place(x=100,y=340,height=25,width=300)

dest_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=380,height=100,width=480)

root.mainloop()