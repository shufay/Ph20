import random, sys

def check_prime(n, k=20):
    '''
    Checks if n is prime with accuracy k with the Miller-Rabin primality 
    test.

    Arguments:
        n = number to be checked
        k = parameter that determines accuracy of the test

    Return:
        True if number is prime
        False otherwise

    https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Primality_Testing
    '''
    if n == 2 or n == 3:
        return True

    elif n == 0 or n == 1:
        return False

    s = 0
    d = n-1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(k):
        a = random.randint(2, n-1)
        x = pow(a, d, n)

        if x == 1 or x == n-1:
            continue

        for r in range(s):
            x = pow(x, 2, n)

            if x == 1:
                return False

            elif x == n-1:
                a = 0
                break

        if a:
            return False

    return True

def choose_prime(length):
    '''
    Chooses two prime numbers such that n = p * q has length 'length'.

    Arguments:
        length = length of key n in bits

    Return:
        A tuple (p, q) of prime numbers
    '''
    p, q = 0, 0

    n_min = 1 << (length - 1)   # min value for n given length
    n_max = (1 << length) - 1   # max value for n given length

    p_min = 1 << (length//2 - 1) 
    p_max = 1 << (length//2 + 1)

    while not (check_prime(p) and check_prime(q) and \
        p * q in range(n_min, n_max+1)):
        p = random.randint(p_min, p_max)
        q = random.randint(p_min, p_max)

    return p, q

def coprime(p, q):
    '''
    Checks if numbers p and q are coprime.

    Arguments:
        p, q = numbers to check 

    Return:
        True if p, q are coprime
        False otherwise
    '''
    # computes gcd(p, q)
    while q != 0:
        p, q = q, p % q

    return p == 1

class RSA:
    '''
    A toy RSA cryptosystem. Default key length of n is 16 bits. Only
    encrypts and decrypts integers.
    '''
    def __init__(self, length=8):
        keys = self.make_keys(length)
        self.PublicKeys = {
                            'n': keys[0],
                            'e': keys[1]
                            }
        self.PrivateKey = keys[2]

    def make_keys(self, length):
        '''
        Generates the public and private keys n, d, e.

        Arguments:
            length = length of key n in bits

        Return:
            A tuple (n, e, d) of keys.
        '''
        # choose large prime numbers p, q 
        p, q = choose_prime(length)
        # find key n
        n = p * q                       # public key
        tote = (p-1) * (q-1)

        # find key e
        for i in range(2, tote):
            if coprime(i, tote):
                e = i                   # public key
                break   

        # find key d
        for j in range(2, tote):
            if (e*j % tote == 1):
                d = j                   # private key               
                break       

        return n, e, d

    def encrypt(self, m):
        '''
        Encrypts the message 'm' which is only an integer.

        Arguments:
            m = an integer to be encrypted

        Return:
            The encrypted message
        '''
        return pow(m, self.PublicKeys['e'], self.PublicKeys['n'])

    def decrypt(self, m):
        '''
        Decrypts the message 'sm' which is only an integer.

        Arguments:
            m = an integer to be decrypted

        Return:
            The decrypted message
        '''
        return pow(m, self.PrivateKey, self.PublicKeys['n'])

    def collision(self, c):
        '''
        A brute-force hash collision attack. Finds a message that generates 
        the same ciphertext 'c' as the original message.

        Arguments:
            c = the encrypted message

        Return:
            A message with ciphertext 'c'.

        '''
        test = 0

        while self.encrypt(test) != c:
            test += 1

        return test  

if __name__ == '__main__':
    RSA = RSA(16)
    m = random.randint(1, 1000)
    encrypted = RSA.encrypt(m)
    decrypted = RSA.decrypt(encrypted)
    collide =   RSA.collision(encrypted)

    print('Public Keys')
    print('-----------')
    print('n: ', RSA.PublicKeys['n'])
    print('e: ', RSA.PublicKeys['e'])
    print()

    print('Private Key')
    print('-----------')
    print('d: ', RSA.PrivateKey)
    print()
    
    print('m: ', m)
    print('encrypted: ', encrypted)
    print('decrypted: ', decrypted)
    print()

    print('collision attack: ', collide)
    print(f'encrypt({collide}): ', RSA.encrypt(collide))
















