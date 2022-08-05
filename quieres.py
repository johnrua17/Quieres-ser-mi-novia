import tkinter as tk
from tkinter import BOTH, W, Toplevel, ttk
from tkinter.messagebox import NO
from tkinter import *
import random
import random as rnd



class Mensaje:
    def __init__(self, win):
        self.ventana = win
        self.ventana.geometry("800x600")
        self.ventana.resizable(width=False, height=False)
        self.ventana.title("Declaracion")
        self.ventana = self.centra(self.ventana,800,600)
        self.frame_label= tk.Frame(self.ventana, width= 800,height=600, borderwidth=0, relief="sunken")
        self.frame_label.place(x=1, y= 1)
        self.frame_label.config(bg="purple")
        # Nombre

        self.label_xd=tk.Label(self.frame_label, text='¿Puedo ser tu novio?', font='Courier 45')
        self.label_xd.config(fg="white")
        self.label_xd.config(bg="purple")
        self.label_xd.place(x=40, y=50)
        self.label_xd1=tk.Label(self.frame_label, text="❤️", font='Courier 255')
        self.label_xd1.place(x=220, y=150)
        self.label_xd1.config(fg="red")
        self.label_xd1.config(bg="purple")


        self.button_si=tk.Button(self.frame_label, text='Si',font= "Courier 15" , width=20, command= self.siclick)
        self.button_si.place(x=60, y=400)
        self.button_si.config(fg="black")
        self.button_si.config(bg="white")
        self.button_no=tk.Button(self.frame_label, text='No',font= "Courier 15" ,width=20, command= self.clicked)
        self.button_no.place(x=500 , y=400)
        self.button_no.config(fg="black")
        self.button_no.config(bg="white")
        return
        
       
    def centra(self,win,ancho,alto): 
        """ centra las ventanas en la pantalla """ 
        x = win.winfo_screenwidth() // 2 - ancho // 2 
        y = win.winfo_screenheight() // 2 - alto // 2 
        win.geometry(f'{ancho}x{alto}+{x}+{y}') 
    
    def clicked(self):
        self.num = int(rnd.random()*400)+1
        self.num1 = int(rnd.random()*700)+1
        self.button_no.place(x= self.num1, y=self.num )

    def siclick(self):
        self.label_xd2=tk.Label(self.frame_label, text='Sabia que dirias\n"Si" mi Amor' , font='Courier 45')
        self.label_xd2.config(fg="white")
        self.label_xd2.config(bg="purple")
        self.label_xd2.place(x=120, y=50)
        self.label_xd3=tk.Label(self.frame_label, text="❤️", font='Courier 255')
        self.label_xd3.place(x=220, y=200)
        self.label_xd3.config(fg="red")
        self.label_xd3.config(bg="purple")
        self.label_xd.destroy()
        self.button_si.place(x=1000, y=1100)
        self.button_no.place(x=1000, y=1100)





  
  

if __name__ == '__main__':
    ventana = Tk()
    application = Mensaje(ventana)
    ventana.mainloop()