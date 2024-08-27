# **Credit/Debit Card Validator**

# The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers, most notably credit card numbers. It’s designed to detect accidental errors in digits, such as mistyped numbers. Here's how it works:
#
# 1. Remove any '-' or ' '|
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit(even places) from right to left.
# (If result is a two-digit number,
# add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is valid

import re


def cardValidation():
    while True:
        card_number = input("Card Number: ").replace(" ", "").replace("-", "")[::-1]

        no_letter = bool(re.findall(r'[A-Za-z]', card_number))

        if not no_letter:
            break
        else:
            print("Your card is INVALID")

        # card_number = '23023765544321'
    print(card_number)

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
        print("Your card is VALID")
    else:
        print("Your card is INVALID")