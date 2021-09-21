import random
import time
start = 1 

origin_field = start

while True:
    eyes = random.randint(1,6)
    new_field = origin_field + eyes
    origin_field = new_field

    if new_field == 44:
        print("Eyes: ", eyes, "Origin Field: ", origin_field, "New Field: ", new_field)    
        print("Nun bei D angekommen!")

        break
    elif  new_field <= 44:
        print("Eyes: ", eyes, "Origin Field: ", origin_field, "New Field: ", new_field)    
        continue
    elif new_field >= 44:
        origin_field = new_field - eyes
        continue
    
        
    




