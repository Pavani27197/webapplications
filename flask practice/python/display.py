class calcy():
    def __init__(self,A,B):
        self.n1=A
        self.n2=B
    def display(self):
        print(self.n1,self.n2)
    def add(self,c):
        return(self.n1+self.n2+c)
    def substraction(self):
      return(self.n1-self.n2)
    def multiplication(self):
       return(self.n1*self.n2)
    def division(self):
        return(self.n1/self.n2)
a=int(input())
b=int(input())
c=int(input())
obj=calcy(a,b)
obj.display()
print(obj.add(c))
print(obj.substraction())
print(obj.multiplication())
print(obj.division())
