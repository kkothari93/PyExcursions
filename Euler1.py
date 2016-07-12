"""
Euler Project: Sum of multiples of 3 & 5 upto 1000
"""

def sumn(n):
    return n*(n+1)/2

def euler1(n, a, b):
    n = n-1
    t1 = (n - (n%a))/a
    t2 = (n - (n%b))/b
    ex = a*b
    t3 = (n - (n%ex))/ex
    return a*sumn(t1) + b*sumn(t2) - ex * sumn(t3)
    
if __name__ == "__main__":
    print(euler1(1000,3,5))
    