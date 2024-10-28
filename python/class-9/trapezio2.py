
from trapezio1 import figura

class trapezio(figura):
    def calcular_perimetro(self, ladoMaior):
        perimetro = ladoMaior
        return perimetro
    
    def calcular_area(self, ladoMaior, altura):
        ladoMenor = ladoMaior - altura
        return ladoMenor

t = trapezio()

print(t.calcular_area(10))