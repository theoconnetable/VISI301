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
    ancienscore = int(ancienscore)
    if score > int(ancienscore):
        newphrase = nom + ' :' + str(score)
        g = open("highscore.txt","w")
        g.write(newphrase)
        g.close()
        return True
    else:
        return False
    
        ##remplace score
    
