# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 19:58:09 2016

@author: pulabio
"""

import math
PI = math.pi

class Calc:
    
    #Asa
    ''' Classe que contem cálculos do avião'''
    def area(c_r, b_r, c_t, b_t):
         return c_r*b_r+(c_r+c_t)*b_t/2
     
    def afilamento(c_t, c_r):
         return c_t/c_r
     
    def alongamento(b, s):
         return b**2/s
     
    def c_MA(c_r,afil):
         return 2/3*c_r*((1+afil+afil**2)/(1+afil))
         
         
    #Asas finitas
    def delta(tr,ar):
        ''' Calcula o delta usado '''
        return # LUT (look up table)
    
    def eficiencia_da_envergadura(delta):
        pass
    
    def coeficiente_angular(a0, e, ar):
        '''Coeficiente angular da curva de uma asa de alto alongamento.
        AR deve ser mair do que 4. Essa relação se assume correta em runtime por questões de performance'''
        return a0/(1+(a0/PI*e*ar))
    
    def razao_perfil_asa_finita(a, a0):
        return a/a0
    
    def cl_asa(cls, dif):
        return [cl * dif for cl in cls ]
    
    #Desempenho em voo
    def v_TrMin(w,ro,s,k,cd0):
        '''retorna a velocidade de mínima tração requerida, também conhecida como velocidade de máximo alcance'''
        return ( (2*w/ro*s) * (k/cd0)**0.5 )**0.5
        
    def v_PrMin(v_TrMin):
        ''' Retorna a velocidade de mínima potência requerida, também conhecidada como velocidade de máxima autom=nomia  '''
        return 0.76 * v_TrMin
        
    #Polar de arrasto
        
        
    #Desempenho de decolagem
    def fator_do_efeito_solo(b,h):
        return 256*h**2/(b**2+256*h**2)
        
    def velocidade_de_estol(w,ro,s,cl):
        return (2 * w/ro * s *cl)**0.5
           
          
    #Coeficiente de proporcionalidade K