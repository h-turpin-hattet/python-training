# ============================================================
# LOOPS — Key concepts and snippets
# ============================================================


# ── for _ in range() ─────────────────────────────────────────────────────────
# Use _ when the loop counter is not needed in the body
for _ in range(5):
    print('Repeating...')   # counter is irrelevant

# vs standard loop (index is used):
for i in range(5):
    print(f'Step {i}')


# ── while True + break ────────────────────────────────────────────────────────
# Standard pattern for interactive menus and input loops
counter = 0
while True:
    counter += 1
    if counter == 3:
        break   # only exit point
print('Loop ended')

# Menu pattern:
# while True:
#     show_menu()
#     choice = input('Enter your choice: ')
#     if choice == 'exit':
#         break


# ── Modulo for cycling ────────────────────────────────────────────────────────
# Keeps an index within bounds when repeating a sequence
key = 'happy'   # length = 5

for i in range(10):
    print(f'index {i} → key[{i % len(key)}] = {key[i % len(key)]}')
# Cycles: h a p p y h a p p y


# ── map() ─────────────────────────────────────────────────────────────────────
# Applies a function to every element — returns an iterator
expenses = [{'amount': 30}, {'amount': 10}, {'amount': 50}]

amounts = list(map(lambda e: e['amount'], expenses))
print(amounts)   # [30, 10, 50]

# Equivalent list comprehension (preferred in Python):
amounts_lc = [e['amount'] for e in expenses]


# ── filter() ─────────────────────────────────────────────────────────────────
# Keeps only elements where the function returns True — returns an iterator
expenses = [
    {'amount': 30, 'category': 'food'},
    {'amount': 10, 'category': 'transport'},
    {'amount': 50, 'category': 'food'},
]

food = list(filter(lambda e: e['category'] == 'food', expenses))
print(food)   # only food expenses

# Equivalent list comprehension (preferred):
food_lc = [e for e in expenses if e['category'] == 'food']
