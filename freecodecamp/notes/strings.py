# ============================================================
# STRINGS — Key concepts and snippets
# ============================================================


# ── strip() ──────────────────────────────────────────────────────────────────
# Default: removes whitespace from both ends
print('  hello  '.strip())    # 'hello'

# With argument: removes specific characters
print('_hello_'.strip('_'))   # 'hello'
print('___hello'.strip('_'))  # 'hello'
print('_hello_'.lstrip('_'))  # 'hello_'  ← left only
print('_hello_'.rstrip('_'))  # '_hello'  ← right only

# Use case: snake_case converter removes leading '_' from uppercase first letter
# 'IAmPascal' → '_i_am_pascal' → .strip('_') → 'i_am_pascal'


# ── maketrans() + translate() ─────────────────────────────────────────────────
# Clean a string by replacing/removing multiple characters at once
card = '4111-1111-4555-1142'
table = str.maketrans({'-': '', ' ': ''})
print(card.translate(table))   # '4111111145551142'

# vs chained replace (fine for 1-2 chars, messy beyond that)
print(card.replace('-', '').replace(' ', ''))   # same result


# ── Slicing ───────────────────────────────────────────────────────────────────
# sequence[start:stop:step]
s = 'hello'
print(s[::-1])    # 'olleh'   — reverse
print(s[::2])     # 'hlo'     — every 2 chars
print(s[1::2])    # 'el'      — every 2 chars starting at index 1
print(s[1:-1])    # 'ell'     — exclude first and last

# Use case in Luhn: extract odd/even position digits after reversing
card = '4111111145551142'
reversed_card = card[::-1]
odd_digits  = reversed_card[::2]   # index 0, 2, 4...
even_digits = reversed_card[1::2]  # index 1, 3, 5...


# ── alphabet indexing ─────────────────────────────────────────────────────────
# Use a string as a reference alphabet for cipher operations
alphabet = 'abcdefghijklmnopqrstuvwxyz'

print(alphabet.index('h'))   # 7  — position of a character
print(alphabet[7])           # 'h' — character at a position

# Shift a character forward
char = 'm'
offset = 7
new_index = (alphabet.index(char) + offset) % 26
print(alphabet[new_index])   # 't'

# Shift backward (decryption)
new_index = (alphabet.index('t') - offset) % 26
print(alphabet[new_index])   # 'm'
