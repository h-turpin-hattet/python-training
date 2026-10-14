# ============================================================
# COMPREHENSIONS — Key concepts and snippets
# ============================================================


# ── Basic list comprehension ──────────────────────────────────────────────────
# [expression for element in iterable]
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print(squares)   # [1, 4, 9, 16, 25]


# ── Filter form ───────────────────────────────────────────────────────────────
# [expression for element in iterable if condition]
# Elements that don't match are EXCLUDED entirely
evens = [n for n in numbers if n % 2 == 0]
print(evens)   # [2, 4]


# ── Ternary (inline if/else) ──────────────────────────────────────────────────
# [value_if_true if condition else value_if_false for element in iterable]
# ALL elements are kept — transformed differently based on condition

labels = ['even' if n % 2 == 0 else 'odd' for n in numbers]
print(labels)   # ['odd', 'even', 'odd', 'even', 'odd']

# Use case: snake_case converter
text = 'CamelCase'
snake_list = [
    '_' + char.lower() if char.isupper()   # uppercase → prepend '_'
    else char                               # lowercase → keep as-is
    for char in text
]
print(''.join(snake_list).strip('_'))   # 'camel_case'


# ── Filter vs Ternary — when to use which ────────────────────────────────────
# Filter form  → use when some elements should be DROPPED
evens_only = [n for n in numbers if n % 2 == 0]      # odds are dropped

# Ternary form → use when ALL elements should be KEPT but transformed
labeled    = ['even' if n % 2 == 0 else 'odd' for n in numbers]  # nothing dropped


# ── sum() with generator expression ──────────────────────────────────────────
# sum() accepts a generator directly — no need to build a list first
total = sum(n ** 2 for n in numbers if n % 2 == 0)
print(total)   # 4 + 16 = 20
