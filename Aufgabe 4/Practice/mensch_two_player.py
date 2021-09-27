import random
import time

#Setze Start-Werte für alle Figuren auf '0'.
g1_og = 0, g1 = 0
g2_og = 0, g2 = 0
g3_og = 0, g3 = 0
g4_og = 0, g4 = 0

b1_og = 0, b1 = 0
b2_og = 0, b2 = 0
b3_og = 0, b3 = 0
b4_og = 0, b4 = 0


#WUERFELWURF [Funktion]
def wuerfelwurf():
    eyes = random.randint(1,6)
    if turn == green:
        if g1_og > g2_og and g1_og > g3_og and g1_og > g4_og and g1_og != 0 and g2_og != 0 and g3_og != 0 and g4_og != 0 and g1_og != 1 and g2_og != 1 and g3_og != 1 and g4_og != 1:
            g1 = g1_og + eyes
            g1_og = g1
        elif g2_og > g1_og and g2_og > g3_og and g2_og > g4_og and g1_og != 0 and g2_og != 0 and g3_og != 0 and g4_og != 0 and g1_og != 1 and g2_og != 1 and g3_og != 1 and g4_og != 1:
            g2 = g2_og + eyes
            g2_og = g2
        elif g3_og > g1_og and g3_og > g2_og and g3_og > g4_og and g1_og != 0 and g2_og != 0 and g3_og != 0 and g4_og != 0 and g1_og != 1 and g2_og != 1 and g3_og != 1 and g4_og != 1:
            g3 = g3_og + eyes
            g3_og = g3
        elif g4_og > g1_og and g4_og > g2_og and g4_og > g3_og and g1_og != 0 and g2_og != 0 and g3_og != 0 and g4_og != 0 and g1_og != 1 and g2_og != 1 and g3_og != 1 and g4_og != 1:
            g4 = g4_og + eyes
            g4_og = g4
    elif turn == blue:
        if b1_og > b2_og and b1_og > b3_og and b1_og > b4_og:
            b1 = b1_og + eyes
            b1_og = b1
        elif b2_og > b1_og and b2_og > b3_og and b2_og > b4_og:
            b2 = b2_og + eyes
            b2_og = b2
        elif b3_og > b1_og and b3_og > b2_og and b3_og > b4_og:
            b3 = b3_og + eyes
            b3_og = b3
        elif b4_og > b1_og and b4_og > b2_og and b4_og > b3_og:
            b4 = b4_og + eyes
            b4_og = b4
    return eyes, g1, g2, g3, g4, b1, b2, b3, b4, g1_og, g2_og, g3_og, g4_og, b1_og, b2_og, b3_og, b4_og

#Figuren SCHLAGEN [Funktion]
def figuren_schlagen():
    if g1 == b1 or g1 == b2 or g1 == b3 or g1 == b4:
        #Fuer g1:
        if g1 == b1 - 20 or b1 == g1 - 20 and b1 != 41 and b1 != 42 and b1 != 43 and b1 != 44:
            b1 = 0
        elif g1 == b2 - 20 or b2 == g1 - 20 and b2 != 41 and b2 != 42 and b2 != 43 and b2 != 44:
            b2 = 0
        elif g1 == b3 - 20 or b3 == g1 - 20 and b3 != 41 and b3 != 42 and b3 != 43 and b3 != 44:
            b3 = 0
        elif g1 == b4 - 20 or b4 == g1 - 20 and b4 != 41 and b4 != 42 and b4 != 43 and b4 != 44:
            b4 = 0
        #Fuer g2:
        if g2 == b1 - 20 or b1 == g2 - 20 and b1 != 41 and b1 != 42 and b1 != 43 and b1 != 44:
            b1 = 0
        elif g2 == b2 - 20 or b2 == g2 - 20 and b2 != 41 and b2 != 42 and b2 != 43 and b2 != 44:
            b2 = 0
        elif g2 == b3 - 20 or b3 == g2 - 20 and b3 != 41 and b3 != 42 and b3 != 43 and b3 != 44:
            b3 = 0
        elif g2 == b4 - 20 or b4 == g2 - 20 and b4 != 41 and b4 != 42 and b4 != 43 and b4 != 44:
            b4 = 0
        #Fuer g3:
        if g3 == b1 - 20 or b1 == g3 - 20 and b1 != 41 and b1 != 42 and b1 != 43 and b1 != 44:
            b1 = 0
        elif g3 == b2 - 20 or b2 == g3 - 20 and b2 != 41 and b2 != 42 and b2 != 43 and b2 != 44:
            b2 = 0
        elif g3 == b3 - 20 or b3 == g3 - 20 and b3 != 41 and b3 != 42 and b3 != 43 and b3 != 44:
            b3 = 0
        elif g3 == b4 - 20 or b4 == g3 - 20 and b4 != 41 and b4 != 42 and b4 != 43 and b4 != 44:
            b4 = 0
        #Fuer g4:
        if g4 == b1 - 20 or b1 == g4 - 20 and b1 != 41 and b1 != 42 and b1 != 43 and b1 != 44:
            b1 = 0
        elif g4 == b2 - 20 or b2 == g4 - 20 and b2 != 41 and b2 != 42 and b2 != 43 and b2 != 44:
            b2 = 0
        elif g4 == b3 - 20 or b3 == g4 - 20 and b3 != 41 and b3 != 42 and b3 != 43 and b3 != 44:
            b3 = 0
        elif g4 == b4 - 20 or b4 == g4 - 20 and b4 != 41 and b4 != 42 and b4 != 43 and b4 != 44:
            b4 = 0
    return g1, g2, g3, g4, b1, b2, b3, b4 


#Abfolge bei Zug
while GameOver == False:
    
    #g an der Reihe:
    eyes = 0
    wuerfelwurf()
    figuren_schlagen()
    while eyes == 6:
        wuerfelwurf()
        figuren_schlagen()
    print('g1: ', g1, 'g2:', g2, 'g3:', g3, 'g4:', g4)