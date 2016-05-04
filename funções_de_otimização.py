# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 16:11:39 2016

@author: pulabio
"""
import numpy as np
import itertools

def gerar_listas(classe, parametros):
    lista = []
    
    for parametro in parametros:
        lista.append(classe(*parametro))
    return lista
    
def gerar_listas_param(intervalos):
    lista = []
    lista_param = []
    
    for param in intervalos:
        lista_param.append(np.arange(*param))
                       
    lista = list(itertools.product(*lista_param))
    return lista

def lista_de_teste(*argv):
    l = []
    for arg in argv:
        l.append(arg)
    return l

def otimização(função_objetiva, condição, argumentos):
    pass
    
if __name__== '__main__':
    intervalos=[(1,3,0.1),(1,3,.1),(1,3.,1),(0,1,2)]
    parametros = gerar_listas_param(intervalos)
    asas = gerar_listas(Asa, parametros)
    for asa in asas:
   #    print(str(asa.b)+" "+ str(asa.c_r) + " "+ str(asa.c_t)+" "+ str(asa.b_r) + " ")
        print(str(asa.b)+ "  "+ str(asa.s) + "  " +(str(asa.ar)))