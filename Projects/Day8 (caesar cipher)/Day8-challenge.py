
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    return is_prime


number = int(input("What number do you want to check? "))
prime = prime_checker(number)

if prime:
    print("It's a prime number.")
else:
    print("It's not a prime number.")
