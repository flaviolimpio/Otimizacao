# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 16:11:39 2016

@author: pulabio
"""
import numpy as np
import itertools
t1=[1,2]
t2=(3,4)
t3=[5,6,7]

combinacoes = list(itertools.product(t1,t2,t3))

#def função_objetiva:
def gerar_listas(classe, intervalo):
    lista = []
    
    for valores in np.arange(intervalo[0],intervalo[1],intervalo[2]):
        lista.append(classe(valores))
    return lista
    
def gerar_listas(classe, intervalos):
    lista = []
    lista_param = []
    
    for param in intervalos:
        lista_param.append(float(param[0]))
    
    for i in range(len(intervalos)):
        for lista_param[i] in np.arange(*intervalos[i]):
            lista.append(classe(*lista_param))
        
    return lista

def lista_de_teste(*argv):
    l = []
    for arg in argv:
        l.append(arg)
    return l

def otimização(função_objetiva, condição, argumentos):
    pass
    
if __name__== '__main__':
    intervalos=[(0,2,1),(0,2,1),(0,2,1),(0,2,1)]
    asas = gerar_listas(lista_de_teste, intervalos)
    for asa in asas:
#        print(str(asa.b)+" "+ str(asa.c_r) + " "+ str(asa.c_t)+" "+ str(asa.b_r) + " ")
        print(asa)
    
    
#def gerar_listas(variaveis, intervalos):
#    ''' recebe lista de variaveis e intervalos '''        
#    
#    [(1.8, 0.1, 20),(0.312, 0.420, 20), (0.1594, 0.1, 5), (0,0,0)] 