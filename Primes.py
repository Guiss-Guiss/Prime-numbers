from time import sleep

def generate_primes():
    num = 2  # Starting from the first prime number
    while True:
        # Check if the current number is prime
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
        num += 1
        sleep(0.001)

# This function will keep running and generating prime numbers until it's interrupted with Ctrl-C
generate_primes()
