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
        return str(self.re)+"+"+str(self.im)+"im"
    
    
    def multiplication(self):
        print(str(self.re) +"x"+ str(self.im) +"="+str(self.re*self.im))
        
c1=Complex(1,2)
print(c1)
c1.multiplication()