def area(lado):
    area = lado * lado
    return area

def perimetro(lado):
    perimetro = lado *4
    return perimetro


i = True

while i:
    try:
        lado = float(input("Introduce el lado del cuadrado en cm.: "))
    except ValueError:
        print("Debes introducir un número: ")
    else:
        i = False

print(f"El área de un cuadrado de lado {lado} cm. es:  {area(lado)}")
print(f"El perímetro de un cuadrado de lado {lado} cm. es:  {perimetro(lado)}")
