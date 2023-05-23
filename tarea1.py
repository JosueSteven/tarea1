class Producto:
    def __init__(self, nombre, tipo, cantidad_actual, cantidad_minima, precio_base):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad_actual = cantidad_actual
        self.cantidad_minima = cantidad_minima
        self.precio_base = precio_base
    
    def calcular_precio_final(self):
        impuestos = {
            "papelería": 0.16,
            "supermercado": 0.04,
            "droguería": 0.12
        }
        impuesto = impuestos.get(self.tipo, 0)
        return self.precio_base * (1 + impuesto)


class Tienda:
    def __init__(self):
        self.productos = []
        self.caja = 0
    
    def agregar_producto(self, producto):
        nombres_existentes = [p.nombre for p in self.productos]
        if producto.nombre not in nombres_existentes:
            self.productos.append(producto)
            print("Producto agregado correctamente.")
        else:
            print("Ya existe un producto con ese nombre.")
    
    def visualizar_productos(self):
        if len(self.productos) == 0:
            print("No hay productos en la tienda.")
        else:
            print("Productos en la tienda:")
            for producto in self.productos:
                print(f"Nombre: {producto.nombre}")
                print(f"Tipo: {producto.tipo}")
                print(f"Cantidad actual: {producto.cantidad_actual}")
                print(f"Cantidad mínima para abastecimiento: {producto.cantidad_minima}")
                print(f"Precio base de venta por unidad: {producto.precio_base}")
                print("------------------------------")
    
    def vender_producto(self, nombre, cantidad):
        producto_encontrado = None
        for producto in self.productos:
            if producto.nombre == nombre:
                producto_encontrado = producto
                break
        if producto_encontrado is not None:
            if cantidad <= producto_encontrado.cantidad_actual:
                precio_final = producto_encontrado.calcular_precio_final()
                total_venta = precio_final * cantidad
                producto_encontrado.cantidad_actual -= cantidad
                self.caja += total_venta
                print(f"Se vendieron {cantidad} unidades de {producto_encontrado.nombre}.")
                print(f"Total de venta: ${total_venta}")
            else:
                print("No hay suficiente cantidad de ese producto en la tienda.")
        else:
            print("No se encontró el producto en la tienda.")
    
    def abastecer_producto(self, nombre, cantidad):
        producto_encontrado = None
        for producto in self.productos:
            if producto.nombre == nombre:
                producto_encontrado = producto
                break
        if producto_encontrado is not None:
            producto_encontrado.cantidad_actual += cantidad
            print(f"Se abastecieron {cantidad} unidades de {producto_encontrado.nombre}.")
        else:
            print("No se encontró el producto en la tienda.")
    
    def cambiar_producto(self, nombre, nuevo_nombre, nuevo_tipo, nueva_cantidad_minima, nuevo_precio_base):
        producto_encontrado = None
        for producto in self.productos:
            if producto.nombre == nombre:
                producto_encontrado = producto
                break
        if producto_encontrado is not None:
            producto_encontrado.nombre = nuevo_nombre
            producto_encontrado.tipo = nuevo_tipo
            producto_encontrado.cantidad_minima = nueva_cantidad_minima
            producto_encontrado.precio_base = nuevo_precio_base
            print("Producto cambiado correctamente.")
        else:
            print("No se encontró el producto en la tienda.")
    
    def estadisticas_ventas(self):
        if len(self.productos) == 0:
            print("No hay productos en la tienda.")
        else:
            productos_vendidos = []
            ventas_totales = 0
            for producto in self.productos:
                cantidad_vendida = producto.cantidad_actual - producto.cantidad_minima
                productos_vendidos.append((producto.nombre, cantidad_vendida))
                precio_final = producto.calcular_precio_final()
                ventas_totales += precio_final * cantidad_vendida
            
            productos_vendidos.sort(key=lambda x: x[1])
            producto_mas_vendido = productos_vendidos[-1][0]
            producto_menos_vendido = productos_vendidos[0][0]
            cantidad_dinero_promedio = ventas_totales / sum(p[1] for p in productos_vendidos)
            
            print(f"Producto más vendido: {producto_mas_vendido}")
            print(f"Producto menos vendido: {producto_menos_vendido}")
            print(f"Dinero total obtenido por ventas: ${ventas_totales}")
            print(f"Dinero promedio por unidad vendida: ${cantidad_dinero_promedio}")


tienda = Tienda()

producto1 = Producto("Lápiz", "papelería", 50, 10, 10)
producto2 = Producto("Cuaderno", "papelería", 30, 5, 50)
producto3 = Producto("Arroz", "supermercado", 100, 20, 25)
producto4 = Producto("Nixon pa las emorroides", "droguería", 40, 8, 15)

tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)
tienda.agregar_producto(producto4)

tienda.visualizar_productos()

tienda.vender_producto("Lápiz", 20)
tienda.vender_producto("Cuaderno", 10)

tienda.abastecer_producto("Arroz", 50)

tienda.cambiar_producto("Lápiz", "Lápiz HB", "papelería", 15, 12)

tienda.estadisticas_ventas()