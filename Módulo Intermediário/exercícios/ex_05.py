a, b, c = map(float, input().split())

triangulo = (a * c)/2
circulo = (c**2 )* 3.14159
trapezio = ((a + b ) * c)/2
quadrado = b*b
retangulo = a * b 

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')