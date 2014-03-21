# Computing PI till n digits
from __future__ import division
from math import *
def gauss_legendre(precision):
    a = 1
    b = 1/sqrt(2)
    t = 1/4
    p = 1
    counter = 2
    while True:
        a_n = (a+b)/2
        b_n = sqrt((a*b))
        t_n = t - p*(pow(a_n,2)-pow(b_n,2))
        p_n = 2*p
        a, b, t, p = a_n, b_n, t_n, p_n
        pi = (pow((a_n+b_n),2))/(4*t_n)
        
        if precision < counter:
            return pi
        else:
            counter *= 2

def main():
    digits = int(raw_input("Enter number of decimals:"))
    pi = gauss_legendre(digits)
    print "3." + str(pi)[2:digits+2]

if __name__ == '__main__':
    main()
