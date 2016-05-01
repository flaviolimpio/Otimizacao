# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 22:41:58 2016

@author: Flavio de Lima
"""

#import math
import numpy as np

from aeronaves import *
from funções_de_otimização import *


DENSIDADE = 1.225
V_VOO = 16.782
VISCOSIDADE_DINAMICA = 1.789*10**-5

if __name__ == "__main__":
    lista_de_asas = list()
    
#    for i in np.arange(0,1,0.05):
#        b = 2.8; c_r = 0.41; c_t = 0.25 ; b_r = 1.8
#        c_r = c_r + i
#        lista_de_asas.append(Asa(b, c_r, c_t, b_r)) 
    
    b = 2.8; c_r = 0.41; c_t = 0.25 ; b_r = 1.8

    for valor in np.arange(0.41,0.81,0.05):

        c_r = valor
        lista_de_asas.append(Asa(b, c_r, c_t, b_r))         
        
    for i in range(len(lista_de_asas)):
        print(" c_r  " + str(lista_de_asas[i].c_r)+ "  tr  "+ str(lista_de_asas[i].tr))
    print("\n")
    
    asaA001 = Asa(1.8, 0.3121, 0.1594, 0)
    a= asaA001