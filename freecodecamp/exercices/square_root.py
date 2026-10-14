def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    # tolerance: how close mid² must be to target to accept the result
    # max_iterations: safety cap — avoids infinite loops

    # Edge cases handled before the main algorithm
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        low = 0
        high = max(1, square_target)  # max(1, target) handles targets between 0 and 1
        root = None                   # will be set if the algorithm converges

        # _ signals the loop counter is not used — we only care about the limit
        for _ in range(max_iterations):
            mid = (low + high) / 2    # midpoint of current search range
            square_mid = mid ** 2     # test value

            # Check if mid² is close enough to target (within tolerance)
            if abs(square_mid - square_target) < tolerance:
                root = mid
                break   # converged — exit the loop early

            elif square_mid < square_target:
                low = mid    # mid is too small → narrow to upper half
            else:
                high = mid   # mid is too large → narrow to lower half

        if root is None:
            # Loop exhausted without converging
            print(f"Failed to converge within {max_iterations} iterations.")
        else:
            print(f'The square root of {square_target} is approximately {root}')

    return root

N = 16
square_root_bisection(N)