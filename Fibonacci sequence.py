sum_even = 0
a, b = 1, 2

while b < 4000000:
    if b % 2 == 0:
        sum_even += b
    a, b = b, a + b

print(sum_even)
