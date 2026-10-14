def verify_card_number(card_number):
    
    # Step 1: reverse the card number for easier position-based processing ──
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]

    # Extract digits at odd positions (index 0, 2, 4... after reversal)
    odd_digits = card_number_reversed[::2]

    # Sum odd-position digits as-is (no transformation needed)
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # Step 2: process even-position digits (index 1, 3, 5... after reversal) ──
    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]

    for digit in even_digits:
        number = int(digit) * 2   # double each even-position digit

        # If doubling produces a two-digit number, sum its digits
        # e.g. 7 * 2 = 14 → 1 + 4 = 5
        if number >= 10:
            number = (number // 10) + (number % 10)

        sum_of_even_digits += number

    # Step 3: validate — total must be divisible by 10 ──
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0   # True = valid card, False = invalid


def main():
    card_number = '4111-1111-4555-1142'

    # Remove dashes and spaces before processing
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()