a=int(input("Dati a (prima fractie a/b) = "))
b=int(input("Dati b (prima fractie a/b) = "))
c=int(input("Dati c (prima fractie c/d) = "))
d=int(input("Dati d (prima fractie c/d) = "))

from fractions import Fraction


def adunarefractii():
    s=Fraction(a,b) + Fraction(c,d)
    return s

def produsfractii():
    p=Fraction(a,b) * Fraction(c,d)
    return p

print(f"Suma= {adunarefractii()}, produsul = {produsfractii()}")