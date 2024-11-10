productos = []  
historial_ventas = []  


while True:  
    print("=== Menú Principal ===") 
    print("1. Agregar Producto")
    print("2. Editar Producto")  
    print("3. Eliminar Producto")  
    print("4. Mostrar Productos")  
    print("5. Realizar Venta")  
    print("6. Ver Historial de Ventas")  
    print("7. Salir")  

    opcion = input("Seleccione una opción: ")  

    
    if opcion == '1':  
        nombre = input("Ingrese el nombre del producto: ")  
        precio = float(input("Ingrese el precio del producto: "))  
        cantidad = int(input("Ingrese la cantidad en stock: ")) 
        
        
        producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        
        productos.append(producto)  
        print(f"Producto '{nombre}' agregado exitosamente.")  

    
    elif opcion == '2':  
        if not productos:  
            print("No hay productos disponibles para editar.")  
        else:
            print("=== Lista de Productos ===")  
            for i, producto in enumerate(productos):  
                print(f"{i}. {producto['nombre']} - Precio: ${producto['precio']} - Cantidad: {producto['cantidad']}")
            
            indice = int(input("Seleccione el índice del producto a editar: ")) 
            
            if 0 <= indice < len(productos):  
                
                productos[indice]['nombre'] = input("Nuevo nombre: ")
                productos[indice]['precio'] = float(input("Nuevo precio: "))
                productos[indice]['cantidad'] = int(input("Nueva cantidad: "))
                print("Producto actualizado correctamente.")  
            else:
                print("Índice inválido.")  

   
    elif opcion == '3':  
        if not productos: 
            print("No hay productos disponibles para eliminar.")  
        else:
            print("=== Lista de Productos ===")  
            for i, producto in enumerate(productos): 
                print(f"{i}. {producto['nombre']} - Precio: ${producto['precio']} - Cantidad: {producto['cantidad']}")
            
            indice = int(input("Seleccione el índice del producto a eliminar: "))  
            
            if 0 <= indice < len(productos): 
                producto_eliminado = productos.pop(indice)  
                print(f"Producto '{producto_eliminado['nombre']}' eliminado.")  
            else:
                print("Índice inválido.")  

    
    elif opcion == '4': 
        if not productos:  
            print("No hay productos disponibles.")  
        else:
            print("=== Lista de Productos ===")  
            for i, producto in enumerate(productos): 
                print(f"{i}. {producto['nombre']} - Precio: ${producto['precio']} - Cantidad: {producto['cantidad']}")

   
    elif opcion == '5':  
        if not productos:  
            print("No hay productos disponibles para la venta.")  
        else:
            total = 0  
            venta = []  
            
            while True:  
                for i, producto in enumerate(productos): 
                    print(f"{i}. {producto['nombre']} - Precio: ${producto['precio']} - Cantidad: {producto['cantidad']}")
                
                indice = input("Seleccione el índice del producto (o 'fin' para terminar): ")  
                if indice.lower() == 'fin':  
                    break
                
                if not indice.isdigit() or not (0 <= int(indice) < len(productos)):  
                    print("Índice inválido.")  
                    continue
                
                indice = int(indice)
                producto = productos[indice]  
                cantidad = int(input(f"Ingrese la cantidad de '{producto['nombre']}' a vender: "))  
                
                if cantidad > producto['cantidad']:  
                    print("Cantidad inválida.")  
                    continue
                
                subtotal = producto['precio'] * cantidad  
                productos[indice]['cantidad'] -= cantidad  
                total += subtotal  
                venta.append((producto['nombre'], cantidad, subtotal)) 
            
            print(f"Total de la venta: ${total}")  
            historial_ventas.append({"detalle": venta, "total": total})  
            print("Venta registrada.")  

  
    elif opcion == '6': 
        if not historial_ventas: 
            print("No hay ventas registradas.")  
        else:
            for idx, venta in enumerate(historial_ventas):  
                print(f"Venta #{idx + 1} - Total: ${venta['total']}")  

   
    elif opcion == '7': 
        print("Saliendo del sistema...") 
        break  

    else:
        print("Opción inválida.")  















