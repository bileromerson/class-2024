
from triangulo1 import figura

perimetro = float(input("calcular perimetro: \n"))
area = float(input("calcular area: \n"))


class triangulo(figura):
    def calcular_perimetro(self, lado):
        perimetro = lado * 3
        return perimetro

    def calcular_area(self, lado, altura):
        area = lado * altura / 2
        return area
    
t = triangulo()
print("----------resultado----------")
print(t.calcular_perimetro(perimetro))
print(t.calcular_area(area))
