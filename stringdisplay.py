class Car:
    def __init__(self): pass
    def __init__(self,brand,regno): self.brand=brand;self.regno=regno

def f(obj,owner,color): 
    return f"{owner}, your car {color} {obj.brand} has registered number {obj.regno}"

t1=Car("Audi","abc123")
print(f(t1,"John","Blue"))