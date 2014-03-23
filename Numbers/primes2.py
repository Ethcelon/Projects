def primes_sieve(limit):
    a = [True] * (limit+1)
    a[0] = a[1] = False
    
    for (i, isprime) in enumerate(a):
        if isprime:
            for n in xrange(i*i, limit, i):
                a[n] = False
    return a

def prime():
    n = int(raw_input('Enter the number to find prime factors of:'))
    factors = []
    prime_list = primes_sieve(n)
    for i in range(2, n+1):
        while n%i == 0:
            if prime_list[i] == True:
                factors.append(i)
            n /= i
    factors_ = ' x '.join([str(i) for i in factors])
    print factors_


prime()
