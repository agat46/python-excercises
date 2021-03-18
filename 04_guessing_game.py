# GRA 1 RAZ #


import random

random_number = random.randint(1,10)
num = None

while num != random_number:
    guess = input("Podaj prosze liczbę od 1 do 10: ")
    num = int(guess)
    if num > random_number:
        print("To za duzo.")
    elif num < random_number:
        print("To za mało.")
    else:
        print("Wygrałes!")
        
print(f"Mialem na mysli liczbe {random_number}")


# GRA WIELE RAZY #    


import random

random_number = random.randint(1,10)

while True:
    guess = input("Podaj prosze liczbę od 1 do 10: ")
    num = int(guess)
    if num > random_number:
        print("To za duzo.")
    elif num < random_number:
        print("To za mało.")
    else:
        print("Wygrałes!")
        play_again = input("Chcesz grac dalej? (y/n) ")
        if play_again == "y":
            random_number = random.randint(1,10)
            num = None
        else: 
            print("Dzięki za gre!")
            break
            
        
