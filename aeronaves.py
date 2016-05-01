# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 23:48:57 2016

@author: pulabio
"""
from calculos import Calc

class Aeronave(object):
    '''
    Classe que representa uma Aeronave
    defaults:
        self.asa = None
        self.empenagem = None
        self.trem_de_pouso = None  
    '''
    def __init__(self):
        self.asa = None
        self.empenagem = None
        self.trem_de_pouso = None        
        
class Asa(object):
    
    def __init__(self, b=None, c_r=None, c_t=None, b_r=None):
        self.b = b
        self.c_r = c_r
        self.c_t = c_t
        self.b_r = b_r
        self.b_t = b - b_r
#tr vem de taper ratio e significa afilamento
        self.tr = Calc.afilamento(self.c_t, self.c_r)
        self.s = Calc.area(c_r, b_r, c_t, self.b_t)
        self.ar = Calc.alongamento(b, self.s)
        self.c_MA = Calc.c_MA(c_r, self.tr)

#para testes
class teste(object):
    
    def __init__(self, atributo1, atributo2):
        self.atributo1 = atributo1
        self.atributo2 = atributo2

    #asaA001
asa = Asa(1.8, 0.3121, 0.1594, 0)