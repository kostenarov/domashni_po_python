class Triangle: 
 
    def __init__(self,a,b,c): 
        self.a = int(a) 
        self.b = int(b) 
        self.c = int(c) 
 
    def area(self): 
        s=(self.a + self.b + self.c) 
        return(s) 
 
a=input("Enter the value of a = ") 
b=input("Enter the value of b = ") 
c=input("Enter the value of c = ") 
t = Triangle(a, b, c) 
print("area : {}".format(t.area())) 