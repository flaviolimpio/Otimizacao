# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 19:58:09 2016

@author: pulabio
"""


import math
PI = math.pi

class Calc:

    ''' Classe que contem cálculos do avião'''
    
    #Asa
    def area(asa):
         return asa.c_r*asa.b_r+(asa.c_r+asa.c_t)*asa.b_t/2
     
    def afilamento(asa):
         return asa.c_t/asa.c_r
     
    def alongamento(asa):
         return asa.b**2/asa.s
     
    def c_MA(asa):
         return 2/3*asa.c_r*((1+asa.tr+asa.tr**2)/(1+asa.tr))
         
    def area_molhada_asa(asa):
        return asa.s * 2
         
    #Asas finitas
    def delta(asa):
        
#####################################################################################
#####################################################################################
#####################################################################################        
        
        ''' Calcula o delta usado '''
        #Depende de tr e ar
        return 0.03# deve ser substituido por LUT (look up table)
        
        
        
#####################################################################################
#####################################################################################
##################################################################################### 
   
    def eficiencia_da_envergadura(delta):
        ''' Fator de eficiencia de envergadura (e) '''
        return 1/(1+delta)
    
    def coeficiente_angular_asa(a0, e, ar):
        '''Coeficiente angular da curva de uma asa de alto alongamento.
        AR deve ser mair do que 4. Essa relação se assume correta em runtime por questões de performance'''
        return a0/(1+(a0/PI*e*ar))
    
    def razao_perfil_asa_finita(a, a0):
        '''Dif'''
        return a/a0
    
    def cs_asa(cls, dif):
        return [cl * dif for cl in cls ]
    
    
    
    #Desempenho em voo
    def v_TrMin(w,ro,s,k,cd0):
        '''retorna a velocidade de mínima tração requerida, também conhecida como velocidade de máximo alcance'''
        return ( (2*w/ro*s) * (k/cd0)**0.5 )**0.5
        
    def v_PrMin(v_TrMin):
        ''' Retorna a velocidade de mínima potência requerida, também conhecidada como velocidade de máxima autonomia  '''
        return 0.76 * v_TrMin
        
    #Polar de arrasto
        
    def area_molhada(aeronave):
        return aeronave.asa.s_wet + aeronave.empenagem.s_wet + aeronave.trem_de_pouso.s_wet
        
    def eficiencia_de_Oswald(e):
        ''' Fator de eficiência de Oswald (e0) '''
        return e * 0.75
        
    def coeficiente_de_proporcionalidade(e0,AR):
        ''' Coeficiente de proporcionalidade K '''
        return 1/(PI*e0*AR)
        
    def coeficiente_de_atrito():
        ''' Coeficiente de atrito C_F '''
        #Coeficiente de atrito equivalente C_F calculado
        pass
        
    def coeficiente_de_arrasto_parasita(S_wet, C_F, S):
        '''Coeficiente de arrasto parasita C_D0'''
        return S_wet * C_F / S
        
    #Desempenho de decolagem
    def fator_do_efeito_solo(b, h):
        return 256*h**2/(b**2+256*h**2)
        
    #Calculo da empenagem
    
    # velocidade de estol
    def velocidade_de_estol(w, ro, s, cl):
        return (2 * w/ro * s *cl)**0.5
           
    def area_da_empenagem_vertical(v):
        pass
    
#    def area_molhada_asa(c_t, c_p, s):
#        ''' Área molhada, também conhecida como S_wet '''
#        return 2 * (1+ 0.2* c_t, c_p)
        
    def pressao_dinamica(ro, v):
        return ( ro * v**2 )/ 2
    
    def sustentacao(q, s, cl_asa_finita):
        return q * s * cl_asa_finita
        
    def arrasto(q, s, cd_asa_finita):
        return q * s * cd_asa_finita

    #Coeficiente de proporcionalidade K