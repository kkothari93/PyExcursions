"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
# 1) Any palindrome with even number of digits is divisible by 11
# Since we need to find the largest palindrome <abccba> using product
# of two three digit numbers we will use this to use the greatest numbers
# divisible by 11 < 1000 as one of the factors.
#
# 2) Since we want to find the largest palindrome, we start off by
# assuming a = 9. If that is so, the last digits of the two factors have to be:
# (1, 9), (3, 3), (7, 7)


def ispalindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == "__main__":
    # start off with largest multiple of 11 < 1000 with (2) in mind
    a = 979  # not 990 as that has 0 in the end
    enddigit = {1: 9, 3: 3, 7: 7, 9: 1}
    for m in range(5):
        a = 979 - 22*m
        for i in xrange(99, 80, -1):
            stri = str(i) if i > 9 else '0' + str(i)
            # get b in string form
            try:
                # to remove a multiple of 11 that has 5 or even digit in the
                # end
                strb = stri + str(enddigit[a % 10])
            except:
                break
            b = int(strb)
            if ispalindrome(a*b):
                print("a, b: %d, %d - %d" % (a, b, a*b))
                break
