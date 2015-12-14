#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Moduló de la interfaz gráfica que manda a llamar a los demás
archivos  
"""

from Tkinter import *
import tkMessageBox
import subprocess


def simularAutomata():
	if var.get() == 1 or var.get() == 2:
		poblacion.configure(state='normal')
		atractor.configure(state='normal')
		reinicio.configure(state='normal')
		simulacion.configure(state='disabled')
		datoPoblacion = variable.get()
		datoDensidad = open("DatoDensidad.txt","w")
		datoDensidad.write(str(datoPoblacion)+","
			+str(var.get())+","
			+str(variableTiempo.get())+","
			+(variableSimulacion.get())+","
			+v.get()+","
			+str(varAtractor.get()))
		datoDensidad.close()
		programaAutomata = subprocess.Popen([sys.executable, 'automata.py'])
	else:
		tkMessageBox.showerror("Error", "Selecciona una opción \n de automata")
		
def graficarPoblacion():
	poblacion.configure(state='disabled')
	programa = subprocess.Popen([sys.executable, 'grafica.py'])
	 
def iniciar():
	poblacion.configure(state='normal')
	pass


root = Tk()
variable = StringVar(root)
variableTiempo = StringVar(root)
variableSimulacion = StringVar(root)
var  = IntVar()
v = StringVar()
varAtractor = IntVar()

#Label principal
Label(root, text="Propagación del Dengue en México").grid(row=0,column=1)

#labels
Label(root, text="Nivel de Resistencia").grid(row=1,column=0)
Label(root, text="Velocidad de Simulación").grid(row=1,column=2)
Label(root, text="Porcentaje de Personas Infectadas").grid(row=1,column=1)

#scrollbar's
resistencia = Scale(root, from_=0, to=100, orient=HORIZONTAL)
resistencia.grid(row=2,column=0)
velocidad = Scale(root, from_=1, to=10, orient=HORIZONTAL)
velocidad.grid(row=2,column=2)
personas = Scale(root, from_=1, to=10, orient=HORIZONTAL)
personas.grid(row=2,column=1)

#Botones para simular y graficar
iniciar = Button(root, text="Iniciar Simulación",command=iniciar, relief=GROOVE)
poblacion = Button(root, text="Graficar Población", command=graficarPoblacion,state='disabled',relief=GROOVE)

iniciar.grid(row=11,column=1)
poblacion.grid(row=12,column=1)
mainloop()