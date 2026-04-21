import os
os.system("cls")
flag = True
pedido = False
nombre =""
rut =""
while flag:
    print("1.Agregar pedido")
    print("2.Ver resumen")
    print("3.Descargar boleta")
    print("4.Salir")
    try:
        opcion = int(input("Ingres una opción\n"))
        if opcion == 1:
            nombre = ""
            rut = ""
            opc_pedido = 0
            cantidad = 0
            print("1.Agregar pedido\n")
            os.system("cls")
            while len(nombre) <= 3 or len(nombre) >=20:
                nombre = input("Agregar nombre (3-20 carácteres)")
                print("Nombre válido")
            while len(rut) <8:
                rut = input("Ingrese su RUT (sin dígito verificador)")
                print("1. Hamburguesa $5000")
                print("2. Pizza $8000")
                print("3. Ensalada $4000")
                while opc_pedido <= 0 or opc_pedido >3:
                    opc_pedido = int(input("Ingrese opción de producto"))
                while cantidad <=0:
                    cantidad = int(input("Ingresar cantidad del producto"))
                if opc_pedido == 1:
                    monto_producto = 5000
                    producto = "Hamburguesa"
                elif opc_pedido == 2:
                    monto_producto = 8000
                    producto = "Pizza"
                else:
                    monto_producto = 4000
                    producto = "Ensalada"
                total = monto_producto * cantidad
                pedido = True
        elif opcion == 2:
            print("2.Ver resumen")
            os.system("cls")
        elif opcion == 3:
            print("3.Descargar boleta")
            os.system("cls")
    except:
        print(".............")