# Autor : Robert Groom

ciclo = True

productos = ["Pikachu Roll", "Otaku Roll", "Pulpo Venenoso Roll", "Anguila Eléctrica Roll"]
precios = [4500, 5000, 5200, 4800]
cantidades = [0, 0, 0, 0]

while ciclo == True:
    try:
        opc = int(input(f"\nArme su pedido. Presione '0' para salir\n1){productos[0]}:\t\t\t${precios[0]}\n2){productos[1]}:\t\t\t${precios[1]}\n3){productos[2]}:\t\t${precios[2]}\n4){productos[3]}:\t${precios[3]}\n\n"))
    except ValueError:
        print("Error de tipeo, el programa no admite carácteres.")
    else:
        if opc == 0:
            pass
        elif opc == 1:
            cantidades[0] += 1
        elif opc == 2:
            cantidades[1] += 1
        elif opc == 3:
            cantidades[2] += 1
        elif opc == 4:
            cantidades[3] += 1
        else:
            print("Opción inválida. Intente nuevamente.")
        total = cantidades[0]*precios[0] + cantidades[1]*precios[1] + cantidades[2]*precios[2] + cantidades[3]*precios[3]
        print("\nCarro:")
        print(f"{cantidades[0]}x {productos[0]}\n{cantidades[1]}x {productos[1]}\n{cantidades[2]}x {productos[2]}\n{cantidades[3]}x {productos[3]}")
        print(f"Total: ${total}")
        while opc == 0:
            cod = input("\nIngrese un código de descuento.\nPresione 'x' para volver al menú de pedidos.\nPresione '0' para terminar la compra:\n").lower()
            if cod == "soyotaku":
                ciclo = False
                break
            elif cod == "x":
                break
            elif cod == "0":
                ciclo = False
                break
            else:
                print("Código no válido.")
descuento = round(total*0.1)
total_prod = cantidades[0] + cantidades[1] + cantidades[2] + cantidades[3]
print(f"******************************\nTOTAL PRODUCTOS: {total_prod}\n******************************")
print(f"{productos[0]} : {cantidades[0]}\n{productos[1]} : {cantidades[1]}\n{productos[2]} : {cantidades[2]}\n{productos[3]} : {cantidades[3]}\n")
print("******************************")
if cod == "soyotaku":
    print(f"Subtotal por pagar: ${total}\nDescuento por codigo: ${descuento}\nTOTAL: ${total-descuento}")
else:
    print(f"TOTAL: ${total}")