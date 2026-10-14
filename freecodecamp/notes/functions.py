# ============================================================
# FUNCTIONS — Key concepts and snippets
# ============================================================


# ── Default parameters ────────────────────────────────────────────────────────
# Default values used when the caller doesn't provide an argument
def greet(name, greeting='Hello'):
    print(f'{greeting}, {name}!')

greet('Hippolyte')               # Hello, Hippolyte!
greet('Hippolyte', 'Bonjour')   # Bonjour, Hippolyte!

# Rule: parameters with defaults must come AFTER those without
# def invalid(optional='x', required): ← SyntaxError


# ── Returning a boolean expression directly ───────────────────────────────────
# Any comparison operator returns True/False — no need for if/else

# Verbose:
def is_valid_v1(total):
    if total % 10 == 0:
        return True
    else:
        return False

# Concise:
def is_valid_v2(total):
    return total % 10 == 0   # ✅ expression already evaluates to bool

print(is_valid_v2(30))   # True
print(is_valid_v2(31))   # False


# ── Direction parameter ───────────────────────────────────────────────────────
# One function handles two opposite operations via a direction multiplier

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def shift_char(char, offset, direction=1):
    index = alphabet.index(char)
    new_index = (index + offset * direction) % 26
    return alphabet[new_index]

print(shift_char('a', 7))        # 'h'  (encrypt, direction=1)
print(shift_char('h', 7, -1))    # 'a'  (decrypt, direction=-1)


# ── Lambda functions ──────────────────────────────────────────────────────────
# Anonymous single-line functions — useful with map(), filter(), sorted()

double = lambda x: x * 2
print(double(5))   # 10

# Most common use: pass directly to another function
expenses = [{'amount': 30}, {'amount': 10}, {'amount': 50}]
sorted_expenses = sorted(expenses, key=lambda e: e['amount'])
print(sorted_expenses)   # sorted by amount ascending
