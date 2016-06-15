# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 16:11:39 2016

@author: pulabio
"""
import numpy as np
import itertools
from aeronaves import*

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
    range_b= (1.76,2,0.1)
    range_c_r = (0.3,0.55,0.05)
    range_c_t = (0.15,0.30,0.1)
    range_b_r = (0,1,2) # envergadura retangular = 0
    range_h = (0.05, 0.1, 0.01)
    
    intervalos=[range_b,range_c_r,range_c_t,range_b_r,range_h]
    parametros = gerar_listas_param(intervalos)
    asas = gerar_listas(Asa, parametros)
    for asa in asas:
   #    print(str(asa.b)+" "+ str(asa.c_r) + " "+ str(asa.c_t)+" "+ str(asa.b_r) + " ")
        print("b:" + str(asa.b)+ "  "+ "s:" + str(asa.s) + "  " + "AR:" + (str(asa.ar)))