productos = []

def crear_producto(codigo, nombre, precio, cantidad):
    producto = {
        'codigo': codigo,
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    productos.append(producto)

crear_producto('12345', 'Casette', 2000, 120)
crear_producto('22222', 'Mouse', 5000, 60)
crear_producto('33333', 'Teclado', 9900, 40)
crear_producto('44444', 'Notebook', 450000, 5)
crear_producto('55555', 'TV Smart LG', 240000, 12)

def leer_productos():
    print("\n===== LISTA DE PRODUCTOS =====")
    for indice, producto in enumerate(productos, start=1):
        print(f"N° { indice }  Codigo: {producto['codigo']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
        
        
def actualizar_producto(codigo, nombre=None, precio=None, cantidad=None):
    for producto in productos:
        if producto['codigo'] == codigo:
            if nombre is not None:
                producto['nombre'] = nombre
            if precio is not None:
                producto['precio'] = precio
            if cantidad is not None:
                producto['cantidad'] = cantidad
            return True
    return False


def eliminar_producto(codigo):
    for producto in productos:
        if producto['codigo'] == codigo:
            productos.remove(producto)
            return True
    return False