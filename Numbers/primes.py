"""Getting prime factors.This can be done much easily, but I was reading
generators and thought I could use them here."""

def primes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False

def generate_prime_list(limit):
    prime_gen = primes_sieve(limit)
    primes_list = []
    while True:
        a = next(prime_gen, None)
        if a == None:
            return primes_list
        primes_list.append(a)

def prime():
    n = int(raw_input('Enter the number to find prime factors of:'))
    factors = []
    prime_list = generate_prime_list(n)
    for i in range(2, n+1):
        while n%i == 0:
            if i in prime_list:
                factors.append(i)
            n /= i
    factors_ = ' x '.join([str(i) for i in factors])
    print factors_
prime()


