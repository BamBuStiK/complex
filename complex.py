"""
백동렬:maintainer
허규:addition,subtraction
오현택:multiplication
"""
class Complex:
    def __init__(self, re=0, im=0):
        self.re=re
        self.im=im

    def __str__(self):
        return str(self.re)+"+"+str(self.im)+"i"


    def substraction(self, x):
        c=Complex()
        c.re=self.re - c1.re
        c.im=self.im-c1.im
        return c

    def multiple(self, c1):
        c = Complex()
        c.re = self.re*c1.re-self.im*c1.im
        c.im = self.re*c1.im+self.im*c1.re
        return c