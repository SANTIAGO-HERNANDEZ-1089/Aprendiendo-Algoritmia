precioH = int(input("ingrese el precio de la hora trabajada:"))
htrabM = int(input("ingrese las horas extras trabajadas en el mes:"))

neto = precioH * htrabM 
recargo = neto * 0.35
total = recargo + neto

print("liquidacion total de extras:", total)