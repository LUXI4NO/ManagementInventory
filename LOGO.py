import streamlit as st
import pandas as pd
import altair as alt
import mysql.connector
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="LOGO", page_icon="⭕", layout="wide")

def css_load(css_file):
    with open(css_file) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

css_load("style/main.css")

email_address = "AlvarezLucianoEzequiel@gmail.com"
registros_almacen = []
salidas_registradas = []

# Función para conectar a la base de datos
def conectar_bd():
    conexion = mysql.connector.connect(
        user="root", password="123456789", host="localhost",
        database="Negocio", port="3306"
    )
    return conexion

def mostrar_inicio():
    # Encabezado
    with st.container():
        col1, col2 = st.columns([1, 3])
        # Columna 1: Imagen
        with col1:
            image = Image.open("imagenes/LogoTipo2.png")
            st.image(image, use_column_width=True, width=50)
        with col2:
            st.write("##")
            st.write("##")
            st.title("Bienvenido a LOGO: Tu Solución Integral de Gestión de Inventarios")
            st.subheader("Optimiza el control de tus productos y pedidos de forma efectiva")

            st.write(
                "LOGO es la plataforma perfecta para gestionar tu inventario y Productos de manera eficiente y sin complicaciones. "
                "Con nuestras herramientas automatizadas, puedes llevar un registro preciso de tus productos, realizar un seguimiento y generar informes detallados para tomar decisiones informadas. "
                "Simplifica tus procesos de negocio y ahorra tiempo y recursos con LOGO."
            )
    # Sección 1: Nuestros servicios
    # Encabezado de la sección
    st.write("---")
    st.subheader("Los servicios que ofrecemos: ")
    st.write("##")
    
    with st.container():
        col1, col2, col3 = st.columns([2, 2, 2])
        
        # Columna 1: Imagen
        with col1:
            image = Image.open("imagenes/LogoTipo3.png")
            st.image(image, use_column_width=True)
            st.subheader("Simplifica tu gestión")
            st.write(
                "En nuestro Inventario, ofrecemos herramientas avanzadas para simplificar la gestión de tus inventarios. Olvídate de los procesos manuales tediosos y lleva un control eficiente de tus productos y pedidos."
            )
            st.write(
                "- Gestiona fácilmente tu inventario de productos.\n"
                "- Realiza seguimiento de entrada y salida de productos.\n"
                "- Obtén análisis detallados de tus datos para tomar decisiones informadas.\n\n"
                "Simplifica tu negocio con nuestro Inventario."
            )
        
        # Columna 2: Texto descriptivo
        with col2:
            image = Image.open("imagenes/LogoTipo3.png")
            st.image(image, use_column_width=True)
            st.subheader("Automatización de procesos")
            st.write(
                "Automatiza tareas repetitivas y ahorra tiempo. Con Mi Negocio, puedes automatizar la gestión de pedidos, controlar el stock de productos y generar informes automáticamente. Dedica más tiempo a hacer crecer tu negocio."
            )
            st.write(
                "- Registro y seguimiento de pedidos de manera eficiente.\n"
                "- Notificaciones automáticas para mantenerte informado.\n"
                "- Integración con proveedores para una gestión sin problemas.\n\n"
                "Simplifica tus procesos con Mi Negocio."
            )

        with col3:
            image = Image.open("imagenes/LogoTipo3.png")
            st.image(image, use_column_width=True)
            st.subheader("Visualización de datos")
            st.write(
                "Obtén una visión clara de tu negocio. Con Mi Negocio, puedes visualizar datos en tiempo real, realizar un seguimiento detallado de tus productos y pedidos, y tomar decisiones informadas para el crecimiento de tu empresa."
            )
            st.write(
                "- Gráficos interactivos para analizar tendencias.\n"
                "- Informes personalizados para cada aspecto de tu negocio.\n"
                "- Acceso rápido y fácil a tus datos desde cualquier lugar.\n\n"
                "Visualiza tus datos con Mi Negocio."
            )

        with st.container():
            st.write("----")
            st.header("Contactame! 📩")
            st.write("##")
            contact_from =f"""
        <form action="https://formsubmit.co/{email_address}" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Tu nombre" required>
                <input type="email" name="email" placeholder="Tu email" required>
                <textarea name="message" placeholder="Tu mensaje aquí" required></textarea>
                <button type="submit">Enviar</button>
            </form>
            """

            left_column, righ_column = st.columns([3, 1])
            with left_column:
                st.markdown(contact_from, unsafe_allow_html= True)
            with righ_column:
                image = Image.open("imagenes/LogoTipo2.png")
                st.image(image, use_column_width=True, width=50)
            
# Función para la página de productos
def mostrar_productos():
    st.title("Ingreso de Proveedores y Productos")
    st.subheader("Aquí puedes registrar la información de Proveedores y Productos.")

    # Sección para ingresar proveedores
    with st.container():
        st.write("---")
        st.header("Ingreso de Proveedores:")
        st.write("##")
        
        # Recopilación de datos del usuario
        col1, col2 = st.columns((1, 2))
        with col1:
            NombreProveedor = st.text_input("Nombre del Proveedor")
            Telefono = st.text_input("Teléfono del Proveedor")
            Notas = st.text_area("Notas del Proveedor")
        with col2:
            Email = st.text_input("Email del Proveedor")
            Ubicacion = st.text_input("Ingrese la Ubicacion del Proveedor")


        if st.button("Registrar Proveedor", key="registrar_proveedor"):
            # Validar campos obligatorios
            if not NombreProveedor or not Ubicacion:
                st.error("Por favor, ingrese el nombre del proveedor")
            else:
                conexion = conectar_bd()
                cursor = conexion.cursor()

                consulta = "INSERT INTO Proveedores (NombreProveedor, Ubicacion, Telefono, Email, Notas) VALUES (%s, %s, %s, %s, %s)"
                datos = (NombreProveedor, Ubicacion, Telefono, Email, Notas)

                try:
                    cursor.execute(consulta, datos)
                    conexion.commit()
                    st.success("Los datos del proveedor se han registrado exitosamente.")
                except mysql.connector.Error as e:
                    st.error("Error al registrar el proveedor.")
                finally:
                    cursor.close()
                    conexion.close()

    # Sección para mostrar los proveedores en una tabla
    with st.container():
        st.write("##")
        st.header("Historial de Proveedores")
        st.subheader("Lista de Proveedores del almacen. Aquí puedes ver los Proveedores.")

        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = "SELECT Proveedor_ID, NombreProveedor, Ubicacion, Telefono, Email, Notas FROM Proveedores"
        cursor.execute(query)
        Proveedores = cursor.fetchall()
        df = pd.DataFrame(Proveedores, columns=["ID", "Nombre Proveedor", "Ubicación", "Teléfono", "Email", "Notas"])

        st.dataframe(df, width=1250)

    # Eliminar última fila de proveedores
    if st.button("Eliminar Última Fila de Proveedores", key="eliminar_ultima_fila_proveedores"):
        if not df.empty:
            ultimo_id = int(df.iloc[-1]["ID"])

            conexion = conectar_bd()
            cursor = conexion.cursor()

            try:
                delete_productos_query = "DELETE FROM Productos WHERE Proveedor_ID = %s"
                cursor.execute(delete_productos_query, (ultimo_id,))
                
                delete_proveedores_query = "DELETE FROM Proveedores WHERE Proveedor_ID = %s"
                cursor.execute(delete_proveedores_query, (ultimo_id,))
                
                conexion.commit()
                st.success("La última fila de proveedores y las filas relacionadas en productos han sido eliminadas.")
            except mysql.connector.Error as e:
                st.error("Error al eliminar el proveedor y sus productos relacionados.")
            finally:
                cursor.close()
                conexion.close()
        else:
            st.warning("La tabla de Proveedores ya está vacía.")

    # Sección para agregar productos
    with st.container():
        st.write("---")
        st.header("Registra tus Productos:")
        st.write("##")

        conexion = conectar_bd()
        cursor = conexion.cursor()
        query_proveedores = "SELECT Proveedor_ID, NombreProveedor FROM Proveedores"
        cursor.execute(query_proveedores)
        proveedores = cursor.fetchall()
        proveedores_dict = {str(proveedor[0]): proveedor[1] for proveedor in proveedores}

        Proveedor_ID = st.selectbox("Selecciona un Proveedor:", options=list(proveedores_dict.keys()))

        # Recopilación de datos del usuario
        column1, column2 = st.columns((1, 2))
        with column1:
            Nombre = st.text_input("Nombre del Producto:")
            Descripcion = st.text_input("Descripción del Producto:")
            Categoria = st.text_input("Categoría del Producto:")
        with column2:
            PrecioCompra = st.number_input("Precio de Compra del Producto:", min_value=0, max_value=10000000)
            PrecioVenta = st.number_input("Precio de Venta del Producto:", min_value=0, max_value=10000000)
            Stock = st.number_input("Cantidad en Stock:", min_value=0, max_value=10000000)

        if st.button("Registrar Producto", key="registrar_producto"):
            if not Proveedor_ID or not Nombre or not PrecioCompra or not PrecioVenta or not Stock:
                st.error("Por favor, complete todos los campos obligatorios.")
            else:
                with conectar_bd() as conexion:
                    cursor = conexion.cursor()

                    consulta = "INSERT INTO Productos (Proveedor_ID, Nombre, Descripcion, Categoria, PrecioCompra, PrecioVenta, Stock) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    datos = (Proveedor_ID, Nombre, Descripcion, Categoria, PrecioCompra, PrecioVenta, Stock)

                    try:
                        cursor.execute(consulta, datos)
                        conexion.commit()
                        st.success("Los datos se han registrado exitosamente.")
                    except mysql.connector.Error as e:
                        st.error("Error al registrar el producto.")
                    finally:
                        cursor.close()

    # Sección para mostrar los productos en una tabla
    with st.container():
        st.write("##")
        st.header("Nuestros Productos")
        st.subheader("Lista de Productos del negocio. Aquí puedes ver los Productos.")

        conexion = conectar_bd()
        cursor = conexion.cursor()
        
        query = """
        SELECT p.ID_Productos, pr.NombreProveedor, p.Nombre, p.Descripcion, p.Categoria,
            p.PrecioCompra, p.PrecioVenta, p.Stock
        FROM Productos p
        INNER JOIN Proveedores pr ON p.Proveedor_ID = pr.Proveedor_ID
        """
        
        cursor.execute(query)
        productos = cursor.fetchall()
        df = pd.DataFrame(productos, columns=["ID", "Proveedor", "Nombre", "Descripción", "Categoría",
                                            "Precio Compra", "Precio Venta", "Stock"])
        
        st.dataframe(df, width=1250)

        if st.button("Eliminar Última Fila de Productos", key="eliminar_ultima_fila_productos"):
            if not df.empty:
                ultimo_id = int(df.iloc[-1]["ID"])

                conexion = conectar_bd()
                cursor = conexion.cursor()

                try:
                    delete_existencias_query = "DELETE FROM Existencias WHERE ID_Productos = %s"
                    cursor.execute(delete_existencias_query, (ultimo_id,))

                    delete_productos_query = "DELETE FROM Productos WHERE ID_Productos = %s"
                    cursor.execute(delete_productos_query, (ultimo_id,))

                    conexion.commit()
                    cursor.close()
                    conexion.close()

                    df = df.iloc[:-1]
                    st.success("La última fila de productos ha sido eliminada.")
                except mysql.connector.Error as e:
                    st.error("Error al eliminar el producto y sus existencias relacionadas.")
                finally:
                    cursor.close()
                    conexion.close()
            else:
                st.warning("La tabla de productos ya está vacía.")

    # Sección para agregar productos al almacén
    with st.container():
        st.write("---")
        st.header("Gestión de Almacenamiento")
        st.subheader("Bienvenido al Almacén. Aquí puedes gestionar tus productos y pedidos.")

        with st.container():
            conexion = conectar_bd()
            cursor = conexion.cursor()

            query_Productos = "SELECT ID_Productos, Nombre FROM Productos"
            cursor.execute(query_Productos)
            Productos = cursor.fetchall()
            Productos_dict = {str(producto[0]): producto[1] for producto in Productos}

            ID_Productos = st.selectbox("Selecciona un Producto:", options=list(Productos_dict.keys()))
            st.subheader("Ingresa donde desees almacenar tus productos.")

            UbicacionAlmacen = st.text_input("Nombre de la Almacén:")
            
            column1, column2 = st.columns((1, 2))
            with column1:
                FechaEntrada = st.date_input("Fecha de Entrada del Producto:")
            with column2:
                FechaCaducidad = st.date_input("Fecha de Caducidad del Producto:")

            if st.button("Registrar Almacén", key="registrar_Almacen"):
                conexion = conectar_bd()
                cursor = conexion.cursor()

                consulta = "INSERT INTO Existencias (ID_Productos, UbicacionAlmacen, FechaEntrada, FechaCaducidad) VALUES (%s, %s, %s, %s)"
                datos = (ID_Productos, UbicacionAlmacen, FechaEntrada, FechaCaducidad)

                try:
                    cursor.execute(consulta, datos)
                    conexion.commit()
                    st.success("Los datos del almacén se han registrado exitosamente.")
                except mysql.connector.Error as e:
                    st.error("Error al registrar el almacén.")
                finally:
                    cursor.close()
                    conexion.close()   
# ...

# Dentro de la función para mostrar el inventario
# Dentro de la función para mostrar el inventario
def mostrar_inventario():
    # Título y descripción
    st.title("Inventario de Productos")
    st.subheader("Bienvenido al sistema de inventario. Aquí puedes visualizar tus productos.")
    st.write("---")

    # Conectar a la base de datos y recuperar los datos del inventario
    conexion = conectar_bd()
    cursor = conexion.cursor()
    query_inventario = """
    SELECT p.Nombre AS Nombre_Producto, p.Stock, p.PrecioCompra, p.PrecioVenta, p.Categoria, e.UbicacionAlmacen, e.FechaEntrada, e.FechaCaducidad
    FROM Existencias e
    INNER JOIN Productos p ON e.ID_Productos = p.ID_Productos
    WHERE p.Stock > 0  # Solo seleccionar productos con stock mayor que cero
    """

    cursor.execute(query_inventario)
    datos_inventario = cursor.fetchall()
    cursor.close()
    conexion.close()

    # Inicializar tabla_inventario como None
    tabla_inventario = None

    # Crear tabla_inventario si hay datos en datos_inventario
    if datos_inventario:
        tabla_inventario = pd.DataFrame(datos_inventario, columns=["Producto", "Stock", "Precio Unitario", "Precio de Venta", "Categoría", "Ubicación en Almacén", "Fecha de Entrada", "Fecha de Caducidad"])

    # Mostrar los datos del inventario en una tabla
    if tabla_inventario is not None:
        valor_total = (tabla_inventario['Stock'] * tabla_inventario['Precio Unitario']).sum()

        # Agregar filtros para búsqueda y ordenamiento
        with st.sidebar:
            st.subheader("Filtros")
            nombre_producto = st.text_input("Buscar por nombre de producto:")
            ubicacion_almacen = st.selectbox("Filtrar por almacén:", ["Todos"] + tabla_inventario["Ubicación en Almacén"].unique().tolist())
            if ubicacion_almacen != "Todos":
                tabla_inventario = tabla_inventario[tabla_inventario["Ubicación en Almacén"] == ubicacion_almacen]
            if nombre_producto:
                tabla_inventario = tabla_inventario[tabla_inventario["Producto"].str.contains(nombre_producto, case=False)]

            st.subheader("Ordenar por")
            ordenar_por = st.selectbox("Seleccione una columna:", tabla_inventario.columns)
            ascendente = st.checkbox("Ordenar ascendente")
            if ascendente:
                tabla_inventario = tabla_inventario.sort_values(by=ordenar_por, ascending=True)
            else:
                tabla_inventario = tabla_inventario.sort_values(by=ordenar_por, ascending=False)

        st.table(tabla_inventario)
        st.info(f"Valor total del inventario: ${valor_total:.2f}")
    else:
        st.warning("No se encontraron registros en el inventario.")

    # Calcular el stock total
    if tabla_inventario is not None:
        with st.container():
            st.write("---")
            st.header("Análisis de los Productos")

            # Gráfico de barras para la cantidad de productos por categoría
            chart1 = alt.Chart(tabla_inventario).mark_bar().encode(
                x=alt.X('Categoría:N', title='Categoría'),
                y=alt.Y('count():Q', title='Cantidad de Productos'),
                color=alt.Color('Categoría:N', title='Categoría')
            ).properties(
                title='Cantidad de Productos por Categoría'
            )

            st.altair_chart(chart1, use_container_width=True)

            st.write("---")

            # Gráfico de barras para la distribución de stock por ubicación en el almacén
            ubicacion_stock = tabla_inventario.groupby('Ubicación en Almacén')['Stock'].sum().reset_index()

            chart2 = alt.Chart(ubicacion_stock).mark_bar(color='lightblue').encode(
                x=alt.X('Ubicación en Almacén:N', title='Ubicación en el Almacén'),
                y=alt.Y('Stock:Q', title='Cantidad de Stock'),
                tooltip=['Ubicación en Almacén:N', 'Stock:Q']
            ).properties(
                width=1250,
                title='Distribución de Stock por Ubicación en el Almacén'
            )

            maximo_stock = ubicacion_stock['Stock'].max()
            maximo_line = alt.Chart(pd.DataFrame({'y': [maximo_stock]})).mark_rule(color='lightgray', strokeWidth=2).encode(y='y:Q')

            final_chart = chart2 + maximo_line

            st.altair_chart(final_chart)
        
def mostrar_salida():
    # Título y descripción
    st.title("Salida de Productos")
    st.subheader("Bienvenido al sistema de Salida. Aquí puedes registrar y visualizar la salida de tus productos.")
    st.write("---")

    # Crear dos columnas para el diseño de la página
    column1, column2 = st.columns((1, 2))

    with column1:
        # Conectar a la base de datos
        conexion = conectar_bd()
        cursor = conexion.cursor()

        # Recuperar la lista de productos disponibles con el Nombre como etiqueta de opción
        query_productos = "SELECT ID_Productos, Nombre FROM Productos"
        cursor.execute(query_productos)
        productos = cursor.fetchall()
        producto_dict = {str(producto[0]): producto[1] for producto in productos}

        # Mostrar un selectbox para que el usuario elija un producto con el Nombre como etiqueta
        selected_product_id = st.selectbox("Selecciona un Producto:", options=list(producto_dict.keys()))

        # Obtener el nombre del producto seleccionado
        selected_product_name = producto_dict.get(selected_product_id, None)

        if selected_product_id is not None:
            # Consulta para obtener la cantidad disponible del producto seleccionado
            query_cantidad_disponible = "SELECT Stock FROM Productos WHERE ID_Productos = %s"
            cursor.execute(query_cantidad_disponible, (int(selected_product_id),))
            cantidad_disponible = cursor.fetchone()[0]
        else:
            cantidad_disponible = None  # Establece cantidad_disponible en None si no hay producto seleccionado

        # Tipos de movimiento de salida
        movimiento = {
            "Salida por venta": "Venta"
        }

        tipo_movimiento = st.selectbox("Seleccione el Tipo de Movimiento:", list(movimiento.keys()))
        fecha_movimiento = st.date_input("Fecha de Movimiento del Producto:")

    with column2:
        # Permitir al usuario especificar la cantidad de salida solo si hay un producto seleccionado
        if cantidad_disponible is not None and cantidad_disponible >= 1 and tipo_movimiento == "Salida por venta":
            # Establecer el valor máximo como cantidad_disponible para evitar errores
            cantidad = st.number_input("Cantidad de Salida:", min_value=1, max_value=cantidad_disponible)
            # Capturar la razón del movimiento de salida
            razon_movimiento = st.text_input("Razón de la Salida:")
        else:
            cantidad = None
            # Capturar la razón del movimiento de salida
            razon_movimiento = st.text_input("Razón de la Salida:")

    if st.button("Registrar Salida", key="registrar_salida"):
        # Conectar a la base de datos
        conexion = conectar_bd()
        cursor = conexion.cursor()

        # Consulta SQL para insertar datos en la tabla de MovimientosInventario
        consulta = "INSERT INTO MovimientosInventario (ID_Productos, TipoMovimiento, Cantidad, FechaMovimiento, RazonMovimiento) VALUES (%s, %s, %s, %s, %s)"

        # Los datos deben ser proporcionados en el mismo orden que aparecen en la consulta
        datos = (int(selected_product_id), "Salida", cantidad, fecha_movimiento, razon_movimiento)

        try:
            cursor.execute(consulta, datos)

            if tipo_movimiento == "Salida por venta":
                # Calcular la nueva cantidad de stock correctamente
                nueva_cantidad = cantidad_disponible - cantidad

                # Actualizar el stock en la base de datos
                query_actualizar_stock = "UPDATE Productos SET Stock = %s WHERE ID_Productos = %s"
                cursor.execute(query_actualizar_stock, (nueva_cantidad, int(selected_product_id)))

            conexion.commit()
            st.success("Los datos de la salida se han registrado exitosamente.")
        except mysql.connector.Error as e:
            st.error("Hubo un error al registrar la salida.")
        finally:
            cursor.close()
            conexion.close()

    # Sección para mostrar el registro de salidas
    with st.container():
        st.write("##")
        st.header("Registro de Salida de Productos")
        # Línea divisoria

        # Conectar a la base de datos
        conexion = conectar_bd()
        cursor = conexion.cursor()

        # Consulta para obtener datos del registro de salida de productos
        query_salida = """
        SELECT m.ID_Movimiento, p.Nombre AS Nombre_Producto, e.UbicacionAlmacen AS Ubicacion_Producto, m.Cantidad, m.TipoMovimiento, m.FechaMovimiento, m.RazonMovimiento, p.PrecioVenta
        FROM MovimientosInventario m
        INNER JOIN Productos p ON m.ID_Productos = p.ID_Productos
        INNER JOIN Existencias e ON m.ID_Productos = e.ID_Productos
        WHERE m.TipoMovimiento = 'Salida'
        ORDER BY m.FechaMovimiento DESC
        """

        cursor.execute(query_salida)
        salida_data = cursor.fetchall()
        cursor.close()
        conexion.close()

        # Mostrar datos del registro de salida de productos en una tabla
        if salida_data:
            df_salida = pd.DataFrame(salida_data, columns=["ID Movimiento", "Nombre Producto", "Ubicación Producto", "Cantidad", "Tipo de Movimiento", "Fecha de Movimiento", "Razón de Movimiento", "Precio de Venta"])
            
            valor_total = (df_salida['Cantidad'] * df_salida['Precio de Venta']).sum()
            # Filtros y ordenamiento
            st.sidebar.subheader("Filtros")
            nombre_producto = st.sidebar.text_input("Buscar por nombre de producto:")
            tipo_movimiento = st.sidebar.selectbox("Filtrar por tipo de movimiento:", ["Todos"] + df_salida["Tipo de Movimiento"].unique().tolist())
            if tipo_movimiento != "Todos":
                df_salida = df_salida[df_salida["Tipo de Movimiento"] == tipo_movimiento]
            if nombre_producto:
                df_salida = df_salida[df_salida["Nombre Producto"].str.contains(nombre_producto, case=False)]

            st.sidebar.subheader("Ordenar por")
            sort_by = st.sidebar.selectbox("Seleccione una columna:", df_salida.columns)
            ascending = st.sidebar.checkbox("Ordenar ascendente")
            if ascending:
                df_salida = df_salida.sort_values(by=sort_by, ascending=True)
            else:
                df_salida = df_salida.sort_values(by=sort_by, ascending=False)

            st.table(df_salida)

            st.info(f"Valor recaudado de venta del inventario: ${valor_total:.2f}")

        else:
            st.warning("No se encontraron registros de salida de productos.")

    # Información adicional: Gráfico de ventas por producto
    with st.container():
        st.write("---")
        st.header("Gráficos de Productos Vendidos")
        st.write("##")
        if salida_data:
            # Crear un DataFrame con la columna de fecha de movimiento
            df_fecha = df_salida.copy()
            df_fecha['Fecha de Movimiento'] = pd.to_datetime(df_salida['Fecha de Movimiento'])

            # Agrupar por fecha y contar la cantidad de cada producto vendido
            df_ventas_productos = df_fecha.groupby(['Fecha de Movimiento', 'Nombre Producto'])['Cantidad'].sum().reset_index()

            # Crear un gráfico de barras apiladas con Altair
            chart = alt.Chart(df_ventas_productos).mark_bar(strokeWidth=10).encode(
                x=alt.X('Cantidad:Q', title='Cantidad Vendida'),
                y=alt.Y('Fecha de Movimiento:T', title='Fecha de Movimiento'),
                color=alt.Color('Nombre Producto:N', legend=alt.Legend(title='Producto'))
            ).properties(
                width=700
            ).configure_axis(
                labelAngle=10
            ).configure_legend(
                orient='right'
            )

            # Mostrar el gráfico en Streamlit
            st.altair_chart(chart, use_container_width=True)
  

st.sidebar.title("Menú de Navegación")
# Opiones del menú
opciones = ["Inicio", "Ingreso de Productos", "Almacen", "Salida de Productos"]
# Crear botones para las opciones
opcion_seleccionada = st.sidebar.radio("Seleccione una opción", opciones)
if opcion_seleccionada == "Inicio":
    mostrar_inicio()
elif opcion_seleccionada == "Ingreso de Productos":
    mostrar_productos()
elif opcion_seleccionada == "Almacen":
    mostrar_inventario()
elif opcion_seleccionada == "Salida de Productos":
    mostrar_salida()