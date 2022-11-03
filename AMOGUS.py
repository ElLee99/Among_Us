import cv2 
import random
from tkinter import *
import tkinter as tk

def elegir():
    for widgets in frame.winfo_children(): widgets.destroy()
    
    canvas=tk.Canvas(frame,width=800,height=400)
    canvas.pack()
    img=tk.PhotoImage(file="./Imagenes/Elegir.png")
    canvas.background=img
    canvas.create_image(0,0,anchor=tk.NW,image=img)
      
    personaje_op,lugar_op,arma_op=IntVar(),IntVar(),IntVar()
    col1,col2,col3=100,300,500
    fil1,fil2,fil3,fil4,fil5=180,210,240,270,300
    
    tk.Radiobutton(root,text=personajes[1],value=1,variable=personaje_op,fg="yellow",bg="black").place(x=col1,y=fil1)
    tk.Radiobutton(root,text=personajes[2],value=2,variable=personaje_op,fg="yellow",bg="black").place(x=col1,y=fil2)
    tk.Radiobutton(root,text=personajes[3],value=3,variable=personaje_op,fg="yellow",bg="black").place(x=col1,y=fil3)
    tk.Radiobutton(root,text=personajes[4],value=4,variable=personaje_op,fg="yellow",bg="black").place(x=col1,y=fil4)
    tk.Radiobutton(root,text=personajes[5],value=5,variable=personaje_op,fg="yellow",bg="black").place(x=col1,y=fil5)
    tk.Radiobutton(frame,text=lugares[1],value=1,variable=lugar_op,fg="blue",bg="black").place(x=col2,y=fil1)
    tk.Radiobutton(frame,text=lugares[2],value=2,variable=lugar_op,fg="blue",bg="black").place(x=col2,y=fil2)
    tk.Radiobutton(frame,text=lugares[3],value=3,variable=lugar_op,fg="blue",bg="black").place(x=col2,y=fil3)
    tk.Radiobutton(frame,text=lugares[4],value=4,variable=lugar_op,fg="blue",bg="black").place(x=col2,y=fil4)
    tk.Radiobutton(frame,text=lugares[5],value=5,variable=lugar_op,fg="blue",bg="black").place(x=col2,y=fil5)
    tk.Radiobutton(frame,text=armas[1],value=1,variable=arma_op,fg="red",bg="black").place(x=col3,y=fil1)
    tk.Radiobutton(frame,text=armas[2],value=2,variable=arma_op,fg="red",bg="black").place(x=col3,y=fil2)
    tk.Radiobutton(frame,text=armas[3],value=3,variable=arma_op,fg="red",bg="black").place(x=col3,y=fil3)
    tk.Radiobutton(frame,text=armas[4],value=4,variable=arma_op,fg="red",bg="black").place(x=col3,y=fil4)
    tk.Radiobutton(frame,text=armas[5],value=5,variable=arma_op,fg="red",bg="black").place(x=col3,y=fil5)
    quit_button=tk.Button(frame,text="Salir",command=lambda : root.destroy())
    quit_button.place(x=425,y=345)
    quit_button.config(fg="yellow",bg="red",font=('helvetica',15,"bold"))
    
    def checar():
        b_ver.destroy()
        personaje_in,lugar_in,arma_in= personaje_op.get(),lugar_op.get(),arma_op.get()
    
        if pers == personaje_in and lug == lugar_in and arm == arma_in:
            print("Game won.")
            tk.Label(frame,text="Ganaste",fg="green",bg="black",font=('helvetica',15,"bold" )).place(x=300,y=350) 
        else:
            print("Game lost.")
            tk.Label(frame,text="Perdiste",fg="red",bg="black",font=('helvetica',15,"bold")).place(x=300,y=350)
            tk.Label(frame,text=f"{personajes[final]} robó los sueños y aspiraciones de Johan en {lugares[final]} con su {armas[final]}",
                                fg="black",bg="yellow",font=('helvetica',9)).place(x=100,y=150)
            
    b_ver=tk.Button(frame,text="Checar",command=checar)
    b_ver.place(x=300,y=350)
    b_ver.config(fg="white",bg="green",font=('helvetica',12,"bold"))
    return(personaje_op.get(),lugar_op.get(),arma_op.get())

def StoryPlace(place,final):
    cv2.imshow(f"{place}",cv2.imread(f"./Imagenes/{place}{final}.png"))

root=Tk()
root.title("Amogus")
root.resizable(0,0)
frame=Frame()
frame.pack()
frame.config(bg="white",width="800",height="400")
canvas=tk.Canvas(frame,width=800,height=400)
canvas.pack()
img= tk.PhotoImage(file="./Imagenes/Menu.png")
canvas.background=img
bg=canvas.create_image(0,0,anchor=tk.NW,image=img)

personajes={1:"Barack Obama",2:"Vicente Fox",3:"El Power Ranger rojo",4:"Max",5:"Juan Pablo II"}
lugares={1:"Jerusalem",2:"Plaza galerías",3:"El polo norte",4:"Yucatan",5:"Una backroom"}
armas={1:"Excalibur",2:"Un supositorio",3:"Avión de combate f35",4:"Una hoja de papel",5:"Shuriken"}

final=random.randint(1,5)
print(f"Generated ending: {final}")
print(f"{personajes[final]} robó los sueños y aspiraciones de Johan en {lugares[final]} con su {armas[final]}")
pers,arm,lug=final,final,final

alt = 300
b_jerusalen=Button(frame,text="Jerusalem",command=lambda : StoryPlace("Jerusalem",final))
b_jerusalen.place(x=45,y=alt)
b_jerusalen.config(fg="black",bg="white",font=('helvetica',12,"bold"))
b_gale=Button(frame,text="Plaza galerías",command=lambda : StoryPlace("Gale",final))
b_gale.place(x=185,y=alt)
b_gale.config(fg="black",bg="white",font=('helvetica',12,"bold"))
b_polo=Button(frame,text="El polo norte",command=lambda : StoryPlace("Polo",final))
b_polo.place(x=350,y=alt)
b_polo.config(fg="black",bg="white",font=('helvetica',12,"bold"))
b_yuca=Button(frame,text="Yucatan",command=lambda : StoryPlace("Yucatan",final))
b_yuca.place(x=510,y=alt)
b_yuca.config(fg="black",bg="white",font=('helvetica',12,"bold"))
b_backroom=Button(frame,text="Una backroom",command=lambda : StoryPlace("Backroom",final))
b_backroom.place(x=645,y=alt)
b_backroom.config(fg="black",bg="white",font=('helvetica',12,"bold"))
b_continuar=Button(frame,text="Continuar",command=elegir)
b_continuar.place(x=350,y=350)
b_continuar.config(fg="white",bg="red",font=('helvetica',15,"bold" ))

root.mainloop()