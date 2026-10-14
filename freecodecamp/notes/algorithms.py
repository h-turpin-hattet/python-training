# ============================================================
# ALGORITHMS — Key concepts and snippets
# ============================================================


# ── Bisection method ─────────────────────────────────────────────────────────
# Narrows a search range by half each iteration until close enough to target
# Used here for square root approximation

target = 16
low = 0
high = max(1, target)   # max(1, target) handles targets between 0 and 1
tolerance = 1e-7        # 0.0000001 — acceptable margin of error

for _ in range(100):
    mid = (low + high) / 2
    square_mid = mid ** 2

    if abs(square_mid - target) < tolerance:
        print(f'sqrt({target}) ≈ {mid}')
        break
    elif square_mid < target:
        low = mid    # too small → search upper half
    else:
        high = mid   # too large → search lower half

# Iteration trace:
# low=0, high=16 → mid=8,   8²=64  > 16 → high=8
# low=0, high=8  → mid=4,   4²=16  = 16 ✅ converged


# ── abs() and scientific notation ────────────────────────────────────────────
print(abs(-5))     # 5    — always positive
print(1e-7)        # 1e-07 = 0.0000001
print(1e3)         # 1000.0

# Check proximity:
if abs(15.9999999 - 16) < 1e-7:
    print('Close enough!')


# ── Luhn algorithm ───────────────────────────────────────────────────────────
# Validates card numbers: total of all processed digits must be divisible by 10

card = '4111111145551142'
reversed_card = card[::-1]

# Odd positions (index 0, 2, 4...) — sum as-is
odd_sum = sum(int(d) for d in reversed_card[::2])

# Even positions (index 1, 3, 5...) — double, adjust if >= 10
even_sum = 0
for d in reversed_card[1::2]:
    n = int(d) * 2
    if n >= 10:
        n = (n // 10) + (n % 10)   # split two-digit: 14 → 1+4=5
    even_sum += n

total = odd_sum + even_sum
print(f'Valid: {total % 10 == 0}')   # True = valid card
