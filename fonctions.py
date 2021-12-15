from random import *
import pygame

def aleatoire(max_width, max_height):
    """Fonction qui permet d'avoir une position aléatoire"""
    
    x = randint(0,max_width)
    y = randint(0,max_height)
    
    return (x,y)



def newhighscore(score,nom):
    '''###########################################################'''
    f = open("highscore.txt")
    phrase = f.readline()
    f.close()
    taille = len(phrase)
    rang = 0
    while phrase[rang] != ":" :
        rang= rang+1
    ancienscore = ''
    for i in range(rang + 1,len(phrase)):
        ancienscore = ancienscore + phrase[i]
    if score > int(ancienscore):
        newphrase = nom + ' :' + str(score)
        g = open("highscore.txt","w")
        g.write(newphrase)
        g.close()
        return str(score)
    else:
        return ancienscore
    
        ##remplace score
