temperatura = float(input("ingrese una temperatura:"))
escala = input("es Fahrenheit (f) o es centígrados (c): ").lower()
if escala == "F" :
    centígrados = temperatura - 32 * 5 / 9
    print(centígrados)
elif escala == "C":
    Fahrenheit = temperatura * 1.8 + 32
    print(Fahrenheit)
else :
    print("escala incorrecta")
    