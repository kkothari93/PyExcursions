"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# TODO:
# Implement the Sieve of Eratosthenes


def largest_prime(n):
    """
    Gives out the largest prime factor for n
    n - should be a positive integer below OFL of hardware
    """
    lpf = n
    p = 3
    while n % 2 == 0:
        lpf = 2
        n = n / 2

    while n != 1:
        while n % p == 0:
            lpf = p
            n = n / p
        # very inefficient next step
        # Probably the sieve should help
        # Issues with memory if complete sieve generated
        # Try implementing a sieve based iterator object
        p += 2

    return lpf

if __name__ == "__main__":
    print("Solution is: %d" % largest_prime(600851475143))
