referencia = input("ingrese la rteferencia: ")
articulo = input("ingrese el nombre del articulo: ")
resultado = (input("ingrese el precio: "))
precio = int(resultado)
unidades = input("ingrese las unidades disponibles: ")

subtotal =  19 * precio / 100
preciototal = subtotal + precio

print("este es el precio total con iva incluido", preciototal)