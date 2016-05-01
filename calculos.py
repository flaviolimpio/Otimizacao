# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 19:58:09 2016

@author: pulabio
"""
class Calc:
    ''' Classe que contem cálculos do avião'''
    def area(c_r, b_r, c_t, b_t):
         return c_r*b_t+(c_r+c_t)*b_t/2
     
    def afilamento(c_t, c_r):
         return c_t/c_r
     
    def alongamento(b, s):
         return b**2/s
     
    def c_MA(c_r,afil):
         return 2/3*c_r*((1+afil+afil**2)/(1+afil))
         