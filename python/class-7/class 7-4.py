

def menor(a,b):
    if a <= b:
        return a
    else:
        return b
    
a = float(input("num1 == "))
b = float(input("num2 == "))
print(f"o menor valor entre{a} e {b} e {menor(a,b)}")