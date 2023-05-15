def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_prime_numbers(n):
    prime_numbers = []
    for num in range(2, n+1):
        if is_prime(num):
            prime_numbers.append(num)
    print(prime_numbers)


n = 100
print_prime_numbers(n)
