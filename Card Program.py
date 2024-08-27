from creditCardValidator import cardValidation
from generateCard import cardGenerator

while True:
    card_mode = input("Select card mode <===> (A) --> Card Validation (B) --> Card Generator (press key n to exit): ").lower()
    if card_mode == "a" or card_mode == 'b' or card_mode == 'n':
        if card_mode == "a":
            print("A")
            cardValidation()

        if card_mode == "b":
            print("A")
            cardGenerator()

        if card_mode == 'n':
            break
    else:
        print("Invalid Input")



