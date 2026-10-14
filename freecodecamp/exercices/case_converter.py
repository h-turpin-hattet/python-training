def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = [
        # Ternary inside list comprehension:
        # if the character is uppercase → prepend '_' and lowercase it
        # otherwise                    → keep the character as-is
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    # Join all characters into a single string
    # then strip any leading '_' caused by an uppercase first letter
    # e.g. 'IAmPascal' → '_i_am_pascal' → 'i_am_pascal'
    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('IAmAPascalCasedString'))
    # output: 'i_am_a_pascal_cased_string'

main()