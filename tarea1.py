import datetime

inventory = [
    {
        "name": 'abv',
        "qty": 4,
        "price": 5.5,
        "p_type": 'hdfjk',
        "size": 'sdufy',
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": '435iu4h',
        "qty": 23,
        "price": 10,
        "p_type": 'dfsg',
        "size": 'kjhg',
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": '54h',
        "qty": 12,
        "price": 1,
        "p_type": 'hljkkf',
        "size": 'chcio',
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": 'Chicle',
        "qty": 132,
        "price": 2,
        "p_type": 'Trident',
        "size": 'grande',
        "updated_at": datetime.datetime.now(),
    },
]


def addItem():
    print("Creacion de producto")
    name = input("Ingrese un nombre: ")
    qty = float(input("Cantidad: "))
    price = float(input("Precio: "))
    p_type = input("Tipo: ")
    size = input("Tamaño: ")
    item = {
        "name": name,
        "qty": qty,
        "price": price,
        "p_type": p_type,
        "size": size,
        "updated_at": datetime.datetime.now(),
    }
    inventory.append(item)


def edit():
    def itemSelection():
        print("Seccione un producto:")
        for idx, item in enumerate(inventory):
            print(f"{idx+1}) {item['name']} \t\t Cantidad: \t {item['qty']}")
        sel_num = int(input("Ingrese el identificar del producto:"))
        sel_item = inventory[sel_num-1]
        return sel_num, sel_item


    sel_num, sel_item = itemSelection()
    print(f"Selecciono {sel_item['name']}, con {sel_item['qty']} existencias")
    new_qty = float(input("Ingrese nuevo valor: "))
    sel_item["qty"] = new_qty
    sel_item["updated_at"] = datetime.datetime.now()
    inventory[sel_num - 1] = sel_item
    print("Actualizado correctamente")

    


def view():
    def showViewMenu():
        print("Seleccione una vista para ver el inventario")
        print("1) Ver por orden de Ingreso")
        print("2) Ver por nombre ascendente")
        print("3) Ver por nombre descendente")
        print("4) Ver por cantidad ascendente")
        print("5) Ver por cantidad descendente")
        print("6) Ver por precio ascendente")
        print("7) Ver por precio descendente")
        print("0) Regresar")
        return int(input("Seleccione una opcion: "))

    def showInventory(sortInventory):
        print('--------------------------------------------------------------------------------------------------------------------------')
        for item in sortInventory:
            print(
                f"{item['name']}\t{item['qty']} Unidades\t ${item['price']}\t de tipo {item['p_type']}\t de tamaño {item['size']}\t Actualizacion {item['updated_at']}\t"
            )
        print('--------------------------------------------------------------------------------------------------------------------------')

    validSorts = {
        1: lambda: showInventory(inventory),
        2: lambda: showInventory(sorted(inventory, key=lambda i: i["name"])),
        3: lambda: showInventory(
            sorted(inventory, key=lambda i: i["name"], reverse=True)
        ),
        4: lambda: showInventory(sorted(inventory, key=lambda i: i["qty"])),
        5: lambda: showInventory(
            sorted(inventory, key=lambda i: i["qty"], reverse=True)
        ),
        6: lambda: showInventory(sorted(inventory, key=lambda i: i["price"])),
        7: lambda: showInventory(
            sorted(inventory, key=lambda i: i["price"], reverse=True)
        ),
        0: lambda: print('Regresando...')
    }
    view_option = 1
    while view_option != 0:
        view_option = showViewMenu()
        validSorts.get(view_option, invalidOption)()


def report():
    def showInventory(sortInventory):
        for item in sortInventory:
            print(
                f"{item['name']}\t{item['qty']} Unidades\t ${item['price']}\t de tipo {item['p_type']}\t de tamaño {item['size']}\t Actualizacion {item['updated_at']}\t"
            )

    def showReportMenu():
        print("Seleccione una opcion")
        print("1) Calcular valor total del inventario")
        print("2) Mostrar inventario por ultima actualizacion")
        print("3) Mostrar productos con bajas existencias")
        print("0) Regresar")
        return int(input("Seleccione una opcion: "))
    
    def lowInventory():
        limit = float(input("Ingrese un limite buscar: "))
        low = [item for item in inventory if item['qty'] <= limit]
        print(f"Inventario por en o por debajo de {limit}")
        showInventory(low)
    
    
    validReports = {
        1: lambda: print(sum(i['price'] * i['qty'] for i in inventory)),
        2: lambda: showInventory(sorted(inventory, key=lambda i: i["updated_at"], reverse=True)),
        3: lambda: lowInventory(),
        0: lambda: print('Regresando...')
    }
    
    report_option = 1
    while report_option != 0:
        report_option = showReportMenu()
        validReports.get(report_option, invalidOption)()
    


validOptions = {
    0: exit,
    1: view,
    2: addItem,
    3: edit,
    4: report,
}


def showMenu():
    print("Inventario App")
    print("Seleccione una opcion:")
    print("(1) Ver Inventario")
    print("(2) Agregar Producto")
    print("(3) Editar Cantidades")
    print("(4) Reportes")
    print("(0) Salir")


def exit():
    print("Terminando app...")


def invalidOption():
    print("¡¡¡Opcion Invalida!!!")


def main():
    option = 1
    while option != 0:
        showMenu()
        option = int(input("Seleccione una opcion: "))
        func = validOptions.get(option, invalidOption)
        func()


main()
