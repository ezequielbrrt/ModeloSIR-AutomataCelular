#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Moduló de la interfaz gráfica que manda a llamar a los demás
archivos  
"""

from Tkinter import *
import tkMessageBox
import subprocess

#tkMessageBox.showerror("Error", "Selecciona una opción \n de automata")
		
def graficarPoblacion():
	poblacion.configure(state='disabled')
	programa = subprocess.Popen([sys.executable, 'grafica.py'])
	 
def iniciar():
	poblacion.configure(state='normal')
	datosResistencia = resistencia.get()
	datosVelocidad = velocidad.get()
	datosPersonas = personas.get()
	mapa = subprocess.Popen([sys.executable, 'mapa.py'])
	datos = open("Datos.txt","w")
	datos.write(str(datosResistencia)+","
		+str(datosVelocidad)+","+str(datosPersonas))
	datos.close()

#configuraciones de la ventana principal
root = Tk()
root.geometry("300x400")
root.resizable(width=False, height=False)

variable = StringVar(root)
variableTiempo = StringVar(root)
variableSimulacion = StringVar(root)
var  = IntVar()
v = StringVar()
varAtractor = IntVar()

#Label principal
Label(root, text="Propagación del Dengue en México").grid(row=0,column=1)
Label(root, text="           ").grid(row=0,column=0)


#labels

Label(root, text="").grid(row=2,column=0)
Label(root, text="Nivel de Resistencia").grid(row=3,column=1)
Label(root, text="Velocidad de Simulación").grid(row=5,column=1)
Label(root, text="Porcentaje de Personas Infectadas").grid(row=7,column=1)

#scrollbar's
resistencia = Scale(root, from_=0, to=100, orient=HORIZONTAL)
resistencia.grid(row=4,column=1)
velocidad = Scale(root, from_=1, to=10, orient=HORIZONTAL)
velocidad.grid(row=6,column=1)
personas = Scale(root, from_=1, to=10, orient=HORIZONTAL)
personas.grid(row=8,column=1)

#Botones para simular y graficar
Label(root, text="").grid(row=9,column=0)
Label(root, text="").grid(row=10,column=0)

iniciar = Button(root, text="Iniciar Simulación",command=iniciar, relief=GROOVE)
Label(root, text="").grid(row=12,column=0)
poblacion = Button(root, text="Graficar Población", command=graficarPoblacion,state='disabled',relief=GROOVE)
Label(root, text="").grid(row=14,column=0)
Label(root, text="Barreto Aviles Ezequiel Adrian").grid(row=15,column=1)


iniciar.grid(row=11,column=1)
poblacion.grid(row=13,column=1)
mainloop()