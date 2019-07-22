class calcy():
    """addition
           substraction
           multiplication
           division"""
    def add(a,b):
        return(a+b)
    def substraction(a,b):
        return(a-b)
    def multiplication(a,b):
        return(a*b)
    def division(a,b):
        return(a/b)
        
a=int(input("a="))
b=int(input("b="))
print(calcy.add(a,b))
print(calcy.substraction(a,b))
print(calcy.multiplication(a,b))
print(calcy.division(a,b))




