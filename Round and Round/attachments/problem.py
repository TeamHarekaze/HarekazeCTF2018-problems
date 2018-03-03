from Crypto.Util.number import *
from Crypto.Random.random import randint

import gmpy
import key
import binascii

flag = key.FLAG
FLAG = binascii.hexlify(flag)
FLAG = int(FLAG.decode('utf-8'), 16)

def gen_n(bits=1024):
  p = getStrongPrime(bits)
  q = getStrongPrime(bits)
  return p*q, p, q

def main():
    n, p, q = gen_n()
    e = (1<<16)+1
    enc = pow(FLAG, e, n)
    p1 = (sum([pow(p-1, i, p) for i in range(q)]))
    q1 = (sum([pow(q-1, i, q) for i in range(p)]))

    print("enc =",enc)
    print("p1 =",p1)
    print("q1 =",q1)

if __name__ == "__main__":
    main()
