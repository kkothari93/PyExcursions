"""
Problem 8
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Ans: This problem does not need code.

It is easy to show that to be a Pythagorean triplet one of a, b has to be
odd and the other even which makes c an odd number.
(Note: Although all can be even dividing by common 2^p divisor should get 
us back to this argument albeit. Hence, in some sense, we are interested in 
only primitive triplets, i.e. gcd of a, b, c = 1. If a multiple of a primitive 
triplet is the answer, we will find that too with this approach.)

Let, a = 2m, b = 2n + 1, c = 2r + 1
Now,
a^2  = c^2 - b^2
4m^2 = (c-b)(c+b)
Now since c, b are odd, c+b, c-b would be even
Let, c - b = 2s, c + b = 2t, then
m^2 = st 
if (s, t) are relative prime, then
s = p^2, t = q^2

Therefore, a = 2pq, b = p^2 - q^2, c = p^2 + q^2
Substituting in the  sum, we have:

2pq + 2p^2 = 1000
p(p + q) = 500 = 2^2 * 5^3
p(p + q) = 20 * 25
Giving p = 20, q = 5

Therefore, a, b, c = 200, 375, 425
Which gives the answer = a*b*c = 31875000

Note:
This is definitely not a irreducible triplet,
the most primitive form of this triplet is a, b, c = 8, 15, 17
Further note that 8 + 15 + 17 = 40 divides 1000 as it should.
"""