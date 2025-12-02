def largest_prime_factor(n):
    factor = 2
    last_factor = 1

    while factor * factor <= n:
        if n % factor == 0:
            last_factor = factor
            n //= factor
        else:
            factor += 1

    # If n > 1 here, n itself is a prime factor (the largest one)
    return max(last_factor, n)

num = 600851475143
print(largest_prime_factor(num))
