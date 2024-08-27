# The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers, most notably credit card numbers. It’s designed to detect accidental errors in digits, such as mistyped numbers. Here's how it works:
#
# 1. Remove any '-' or ' '|
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit(even places) from right to left.
# (If result is a two-digit number,
# add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is valid

import random
import time

def cardGenerator():
    while True:
        try:
            card_mode = int(input("Select card length from 13-19: "))
            if 13 <= card_mode <= 19:
                print("Generating card...")
                time.sleep(3)
                break
            else:
                print("Number out of range")
        except ValueError:
            print("Invalid Input")

    card_number = ""

    while True:
        for i in range(card_mode):
            # print(random.randint(0,9), end="")
            card_number += str(random.randint(0, 9))
        card_number = card_number[::-1]

        odd_digit = 0
        even_digit = 0

        # odd_digit
        for i in card_number[::2]:
            odd_digit += int(i)

        # even_digit
        for i in card_number[1::2]:
            number = int(i) * 2
            if number > 9:
                number -= 9
            even_digit += number

        total = odd_digit + even_digit

        if total % 10 == 0:
            print(f"Card Number: {card_number[::-1]}")
            break
        else:
            card_number = ""
