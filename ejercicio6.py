nombre = input("ingrese su nombre: ")
cargo = input("ingrese su cargo: ")
sueldo = int (input("ingrese su sueldo basico mensual: "))

salud = sueldo * 4 / 100
pension = sueldo * 3.375 / 100
neto = sueldo - (salud + pension)

print(nombre)
print(cargo)
print("aporte a salud:", salud)
print("aporte a pension", pension)
print("neto a pagar:", neto)
