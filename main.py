# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamadas a la función con diferentes casos
monto1 = 100
descuento1 = calcular_descuento(monto1)  # Usa el porcentaje por defecto (10%)
monto_final1 = monto1 - descuento1

monto2 = 200
porcentaje2 = 15
descuento2 = calcular_descuento(monto2, porcentaje2)  # Usa un porcentaje personalizado (15%)
monto_final2 = monto2 - descuento2

# Mostrar resultados del primer monto
print(f"Monto total de la compra: ${monto1}")
print(f"Descuento aplicado: ${descuento1}")
print(f"Monto final a pagar: ${monto_final1}\n")

# Mostrar resultados del segundo monto
print(f"Monto total de la compra: ${monto2}")
print(f"Descuento aplicado: ${descuento2}")
print(f"Monto final a pagar: ${monto_final2}")

