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
#    
#    range_b= (1.5,2.5,0.02)
#    range_c_r = (0.3,0.55,0.05)
#    range_c_t = (0.15,0.30,0.05)
#    range_b_r = (0,1,0.02) # envergadura retangular = 0
#    range_h = (0.05, 0.1, 0.01)
#    
#    intervalos=[range_b,range_c_r,range_c_t,range_b_r,range_h]
#    parametros = gerar_listas_param(intervalos)
#    asas = gerar_listas(Asa, parametros)
##    for asa in asas:
##   #    print(str(asa.b)+" "+ str(asa.c_r) + " "+ str(asa.c_t)+" "+ str(asa.b_r) + " ")
##        print("b:" + str(asa.b)+ "  "+ "s:" + str(asa.s) + "  " + "AR:" + (str(asa.ar)))
##    
    asaA001 = Asa(1.8, 0.3121, 0.1594, 1.8, 0.1)
    a= asaA001