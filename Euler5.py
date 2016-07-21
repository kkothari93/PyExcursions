"""
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

This does not need any code. Any smallest evenly divisible number should have the primes and account for multiplicity if any in the range.
2520 = 2*3*5*7 (all primes till 10) * 2*2 (8 has 3 2s in its factorization) * 3 (9 has 2 3s in its factorization)

therefore our answer is:
2*3*5*7*11*13*17*19 (all primes till 20) * 2*2*2 (16 has 4 2s) * 3 (9 has 2 3s)

This gives us:
232792560

"""