'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")
class date:

    def __init__(self, value):
        self.value=value         
        self.max=31
        self.min=1
        
    def setup(self):
        if self.value>self.max: 
            self.value=self.min 
        elif self.value<self.min: 
            self.value=self.max
        return self.value
        
    
    def increase(self):
        self.value+=1
        self.setup()
        return self.value
        
    def decrease(self):
        self.value+=-1
        self.setup()
        return self.value
d1=date(1);
d2=date(1)
print("d1.increase= ",d1.increase())
print("d2.decrease= ", d2.decrease())


class month(date):
    def __init__(self,value):
        super().__init__(value)
        self.max=12
        
m1=month(12)
m2=month(1)
print("m1.increase= ",m1.increase())
print("m2.decrease= ",m2.decrease())

class year(date):
    def __init__(self,value):
        super().__init__(value)
        
    def setup(self):
        if self.value<1900: self.value=1900
        
y1=year(2000)
y2=year(1800)
print("y1.increase= ",y1.increase())
print("y2.decrease= ",y2.decrease())


        
    

    