import random

capital = 0
piece = ['pile','face']

def piece_proba(pile,face):
    global proba
    proba = [pile,face]

def comptage():
    global capital
    capital += lance.count('pile')
    capital -= lance.count('face')

#_______ jeu  __________

for nb_games in range(1000000):
    # Si pile : jeu A , Si face : jeu B
    piece_proba(0.5,0.5)
    lance = random.choices(piece,proba,k=1)


    if lance[0] == 'pile':
        #_______ jeu A __________

        piece_proba(0.49,0.51)
        lance = random.choices(piece,proba,k=1)
        comptage()


    else:
        #_______ jeu B __________

        #si mon capital est un multiplicateur de 3 : proba 0.09, 0.91
        if capital%3 == 0:

            piece_proba(0.09,0.91)
            lance = random.choices(piece,proba,k=1)
            comptage()
            
        #sinon : proba 0.74, 0.26
        else:
            piece_proba(0.74,0.26)
            lance = random.choices(piece,proba,k=1)
            comptage()
            
print("Votre capital est de : " ,capital)