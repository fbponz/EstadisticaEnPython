#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 21:16:40 2021

@author: franciscodeborjaponz
"""


#!pip install pysimplegui

import PySimpleGUI as sg

memA = 0.0
memB = 0.0
resultado = 0.0

layout = [[sg.Text('Calculadora EDEM-PROGRAMACIÓN ESTADÍSTICA CON PYTHON', size=(64, 1), justification='center')],
  [sg.Text(text='Para gastar los valores guardos en memoria MemA, MemB, PrevResult')],
  [sg.Text(text='Valor guardado en MemA '),sg.Text(text=str(memA),size=(15,1), key='LMemA')], 
  [sg.Text(text='Valor guardado en MemB '),sg.Text(text=str(memB),size=(15,1), key='LMemB')],         
  [sg.Text(text='Numero 1:'), sg.InputText(),sg.Button('MemA', key = 'memA')],
  [sg.Text(text='Numero 2:'), sg.InputText(),sg.Button('MemB', key = 'memB')],
  [sg.Text(text='Resultado:'),sg.Text(size=(20,1), key='-RESULTADO-')], 
  [sg.Button('Sumar', key='sumar'), sg.Button('Restar', key = 'restar'), sg.Button('Multiplicar', key = 'multiplicar'), sg.Button('Dividir', key = 'dividir')]
  ]
window = sg.Window('Calculadora FdBPonz', location=(800, 400))
window.Layout(layout).Finalize()
resultado = 0.0

while True:
    event, values = window.Read()

    if('MemA' == values[0]):
        tempA = memA
    elif('MemB' == values[0]):
        tempA = memB
    elif('PrevResult'==values[0]):
        tempA = resultado
    else:
        tempA = values[0]
        
    if('MemA' == values[1]):
        tempB = memA
    elif('MemB' == values[1]):
        tempB = memB
    elif('PrevResult'==values[1]):
        tempB = resultado
    else:
        tempB = values[1]
        
    if event == 'Exit' or event is None:
        break
    if event == 'sumar':
        resultado = (float(tempA) + float(tempB))
        window['-RESULTADO-'].update(str(resultado))
    
    if event == 'restar':
        resultado = (float(tempA) - float(tempB))
        window['-RESULTADO-'].update(str(resultado))
        
    if event == 'multiplicar':
        resultado = (float(tempA) * float(tempB))
        window['-RESULTADO-'].update(str(resultado))
        
    if event == 'dividir':
        resultado = (float(tempA) / float(tempB))
        window['-RESULTADO-'].update(str(resultado))
        
    if event == 'memA':
        memA = float(values[0])
        window['LMemA'].update(str(memA))
        
        
    if event == 'memB':
        memB = float(values[1])
        window['LMemB'].update(str(memB))

        
    if event == sg.WIN_CLOSED:
        break
window.Close()


