# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 21:19:45 2020

@author: Nicole
"""

def funcionPablo(lista):
    #esta funcion retorna la suma de elementos de una lista
    assert type(lista)==list
    salida = 0
    for i in lista:
        salida += i
    return salida


def funcionNicole(palabra):
    #esta funcion retorna la palabra invertida
    assert type(palabra)==str
    return palabra[::-1]


def funcion(lista):
    
    return max(lista)

