from bd import obtener_conexion

#INSERTAR UN REGISTRO
def insertar_venta(id_tipo_comprobante, fecha, nombre_cliente, direccion, id_juego, cantidad):
    conexion = obtener_conexion()
    sql = "INSERT INTO Ventas(id_tipo_comprobante, fecha, nombre_cliente, direccion, id_juego, cantidad) VALUES (%s, %s, %s, %s, %s, %s)"
    conexion.cursor().execute(sql,(id_tipo_comprobante, fecha, nombre_cliente, direccion, id_juego, cantidad));
    conexion.commit()
    conexion.close()


def obtener_ventas():
    conexion = obtener_conexion()
    ventas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT ventas.id, tipo_comprobante.descripcion, fecha, nombre_cliente, direccion, juegos.nombre, cantidad FROM ventas inner join juegos on ventas.id_juego =juegos.id inner join tipo_comprobante on ventas.id_tipo_comprobante = tipo_comprobante.id;")
        #cursor.execute("SELECT id, id_tipo_comprobante, fecha, nombre_cliente, direccion, id_juego, cantidad FROM ventas")
        ventas = cursor.fetchall()
    conexion.close()
    return ventas


def eliminar_venta(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM ventas WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_venta_por_id(id):
    conexion = obtener_conexion()
    venta = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, id_tipo_comprobante, fecha, nombre_cliente, direccion, id_juego, cantidad FROM ventas WHERE id = %s", (id,))
        venta = cursor.fetchone()
    conexion.close()
    return venta

def obtener_tipos_de_comprobante():
    conexion = obtener_conexion()
    tipos_de_comprobante = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, descripcion FROM tipo_comprobante")
        
        tipos_de_comprobante = cursor.fetchall()
    conexion.close()
    return tipos_de_comprobante