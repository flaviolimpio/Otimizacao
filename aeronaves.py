# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 23:48:57 2016

@author: pulabio
"""
from calculos import Calc
from tabelas import Selig1223

class Perfil(object):
    '''Classe dos perfis aerodinâmicos'''
    
    def __init__(self, a0, m0, cls, cds):
        self.a0 = a0
        self.m0 = m0
        self.cls = cls
        self.cds = cds

#cls_perfil=dict()
#cds_perfil=dict()


selig1223= Perfil(1.891259, 0.09741, Selig1223.cl, Selig1223.cd)

selig1223= Perfil(5.891259, 0.09741, Selig1223.cl, Selig1223.cd)

class Aeronave(object):
    '''
    Classe que representa uma Aeronave
    defaults:
        self.asa = None
        self.empenagem = None
        self.trem_de_pouso = None  
    '''
    
    c_fe = 0.0055    
    
    def __init__(self):
        self.asa = None
        self.empenagem = None
        self.trem_de_pouso = None        
        
        
        
class Perfil_aerodinâmico(object):
    pass

class Asa(object):
    
    def __init__(self, b, c_r, c_t, b_r, h):
        
        self.b = b
        self.c_r = c_r
        self.c_t = c_t
        self.b_r = b_r
        self.b_t = b - b_r
        self.h = h

#       self.perfil = perfil
#Para teste
        self.perfil = Perfil(1.891259, 0.09741, selig1223.cls, selig1223.cds)
        
#tr vem de taper ratio e significa afilamento
        self.tr = Calc.afilamento(self)
        self.s = Calc.area(self)
        self.ar = Calc.alongamento(self)
        self.c_MA = Calc.c_MA(self)
        
#Características de asa finita
        self.delta = Calc.delta(self)
        self.e = Calc.eficiencia_da_envergadura(self.delta)
        self.a = Calc.coeficiente_angular_asa(self.perfil.a0, self.e, self.ar)
        self.dif = Calc.razao_perfil_asa_finita(self.a, self.perfil.a0)
        self.cls = Calc.cs_asa(self.perfil.cls, self.dif)      
        self.cds = Calc.cs_asa(self.perfil.cds, self.dif)
        
        self.clmax = max(self.cls)
        
#        self.area_molhada = 
        self.s_wet = Calc.area_molhada(self)
        
        

        
class Empenagem_horizontal(object):
    
    def __init__(self):
        pass

class Empenagem_vertical(object):
    pass
    
class Fuselagem(object):
    pass

class Grupo_motopropulsor(object):
    #__tr
    
    pass

#para testes
class teste(object):
    
    def __init__(self, atributo1, atributo2):
        self.atributo1 = atributo1
        self.atributo2 = atributo2

    #asaA001
asa = Asa(1.8, 0.3121, 0.1594, 1.79999, 0.4)