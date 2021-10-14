# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 17:19:22 2021

@author: emili
"""

from random import *

def aleatoire(max_width, max_height):
    """Fonction qui permet d'avoir une position aléatoire"""
    
    x = randint(0,max_width)
    y = randint(0,max_height)
    
    return (x,y)
    