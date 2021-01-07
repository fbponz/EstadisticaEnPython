#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 21:16:40 2021

@author: franciscodeborjaponz
"""


#!pip install pysimplegui

import PySimpleGUI as sg

class calculadora: 
    def __init__(self):
        layout = [[sg.Text('Calculadora EDEM', size=(40, 1), justification='center')],
          [sg.Text(text='Numero 1:'), sg.InputText()],
          [sg.Text(text='Numero 2:'), sg.InputText()],
          [sg.Button('Sumar', key='sumar'), sg.Button('Restar', key = 'restar'), sg.Button('Multiplicar', key = 'multiplicar'), sg.Button('Dividir', key = 'dividir')]
          ]
        self.window = sg.Window('Calculadora FdBPonz', location=(800, 400))
        self.window.Layout(layout).Finalize()
        while True:
            event, values = self.window.Read()
            if event == 'Exit' or event is None:
                sys.exit()
                break
            if event == 'sumar':
                self.sumar(values[0], values[1])
            if event == 'restar':
                self.restar(values[0], values[1])
            if event == 'multiplicar':
                self.multiplicar(values[0], values[1])
            if event == 'dividir':
                self.dividir(values[0], values[1])
    def sumar(self,numero_a, numero_b):
        sg.Popup('resutaldo: '+str((float(numero_a)+float(numero_b))))
    def restar(self,numero_a, numero_b):
        sg.Popup('resutaldo: '+str((float(numero_a)-float(numero_b))))
    def multiplicar(self,numero_a, numero_b):
        sg.Popup('resutaldo: '+str((float(numero_a)*float(numero_b))))
    def dividir(self,numero_a, numero_b):
        sg.Popup('resutaldo: '+str((float(numero_a)/float(numero_b))))
  
interfaz_cal = calculadora()
