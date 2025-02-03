import mysql.connector
from ..modelos.models import TipoCocinaModel, TipoReservaModel, SalonModel, ReservaModel

class BaseDAO:
    """
    Clase base para manejar la conexión a la base de datos y ejecutar consultas SQL.
    Contiene métodos para ejecutar consultas, realizar commits, y cerrar la conexión.
    """
    def __init__(self):
        """
        Inicializa la conexión a la base de datos MySQL.
        """
        self.conn = mysql.connector.connect(
            user="root",          # Usuario para la conexión
            password="root",      # Contraseña para la conexión
            port="3307",          # Puerto de la base de datos
            host="localhost",     # Dirección del host (servidor)
            database="TAREA3DI",  # Nombre de la base de datos
        )
        self.cursor = self.conn.cursor(dictionary=True)  # Inicializa el cursor para ejecutar consultas y obtener resultados en formato diccionario

    def execute_query(self, query, params=None, fetch_one=False):
        """
        Ejecuta una consulta SQL y devuelve los resultados.

        Args:
            query (str): La consulta SQL a ejecutar.
            params (tuple): Parámetros de la consulta (por defecto es None).
            fetch_one (bool): Si es True, devuelve solo el primer resultado.

        Returns:
            Resultados de la consulta (diccionario o ID de la última fila insertada).
        """
        self.cursor.execute(query, params or ())  # Ejecuta la consulta con los parámetros proporcionados
        if query.strip().upper().startswith("SELECT"):
            # Si la consulta es un SELECT, retorna los resultados.
            return self.cursor.fetchone() if fetch_one else self.cursor.fetchall()
        else:
            # Si la consulta no es un SELECT, hace commit y retorna el ID de la última fila insertada.
            self.conn.commit()
            return self.cursor.lastrowid

    def close(self):
        """
        Cierra el cursor y la conexión a la base de datos.
        """
        self.cursor.close()  # Cierra el cursor
        self.conn.close()    # Cierra la conexión a la base de datos


class TiposCocinaDAO(BaseDAO):
    """
    Clase para manejar operaciones relacionadas con los tipos de cocina en la base de datos.
    Hereda de BaseDAO para reutilizar la conexión y ejecución de consultas.
    """
    def get(self, tipo_cocina_id):
        """
        Obtiene un tipo de cocina por su ID.

        Args:
            tipo_cocina_id (int): El ID del tipo de cocina a obtener.

        Returns:
            TipoCocinaModel: El objeto del tipo de cocina, o None si no existe.
        """
        query = "SELECT * FROM tipos_cocina WHERE tipo_cocina_id = %s"
        row = self.execute_query(query, (tipo_cocina_id,), fetch_one=True)
        if row:
            return TipoCocinaModel(row['tipo_cocina_id'], row['nombre'])  # Devuelve un objeto TipoCocinaModel
        return None

    def get_all(self):
        """
        Obtiene todos los tipos de cocina.

        Returns:
            list: Lista de objetos TipoCocinaModel.
        """
        query = "SELECT * FROM tipos_cocina"
        rows = self.execute_query(query)
        return [TipoCocinaModel(row['tipo_cocina_id'], row['nombre']) for row in rows]  # Devuelve una lista de objetos TipoCocinaModel


class SalonesDAO(BaseDAO):
    """
    Clase para manejar operaciones relacionadas con los salones en la base de datos.
    Hereda de BaseDAO para reutilizar la conexión y ejecución de consultas.
    """
    def get(self, salon_id):
        """
        Obtiene un salón por su ID.

        Args:
            salon_id (int): El ID del salón a obtener.

        Returns:
            SalonModel: El objeto del salón, o None si no existe.
        """
        query = "SELECT * FROM salones WHERE salon_id = %s"
        row = self.execute_query(query, (salon_id,), fetch_one=True)
        if row:
            return SalonModel(row['salon_id'], row['nombre'])  # Devuelve un objeto SalonModel
        return None

    def get_all(self):
        """
        Obtiene todos los salones.

        Returns:
            list: Lista de objetos SalonModel.
        """
        query = "SELECT * FROM salones"
        rows = self.execute_query(query)
        return [SalonModel(row['salon_id'], row['nombre']) for row in rows]  # Devuelve una lista de objetos SalonModel


class TiposReservasDAO(BaseDAO):
    """
    Clase para manejar operaciones relacionadas con los tipos de reserva en la base de datos.
    Hereda de BaseDAO para reutilizar la conexión y ejecución de consultas.
    """
    def get(self, tipo_reserva_id):
        """
        Obtiene un tipo de reserva por su ID.

        Args:
            tipo_reserva_id (int): El ID del tipo de reserva a obtener.

        Returns:
            TipoReservaModel: El objeto del tipo de reserva, o None si no existe.
        """
        query = "SELECT * FROM tipos_reservas WHERE tipo_reserva_id = %s"
        row = self.execute_query(query, (tipo_reserva_id,), fetch_one=True)
        if row:
            return TipoReservaModel(row['tipo_reserva_id'], row['nombre'])  # Devuelve un objeto TipoReservaModel
        return None
    
    def get_all(self):
        """
        Obtiene todos los tipos de reserva.

        Returns:
            list: Lista de objetos TipoReservaModel.
        """
        query = "SELECT * FROM tipos_reservas"
        rows = self.execute_query(query)
        return [TipoReservaModel(row['tipo_reserva_id'], row['nombre']) for row in rows]  # Devuelve una lista de objetos TipoReservaModel


class ReservasDAO(BaseDAO):
    """
    Clase para manejar operaciones relacionadas con las reservas en la base de datos.
    Hereda de BaseDAO para reutilizar la conexión y ejecución de consultas.
    """
    def get(self, reserva_id):
        """
        Obtiene una reserva por su ID.

        Args:
            reserva_id (int): El ID de la reserva a obtener.

        Returns:
            ReservaModel: El objeto de la reserva, o None si no existe.
        """
        query = "SELECT * FROM reservas WHERE reserva_id = %s"
        row = self.execute_query(query, (reserva_id,), fetch_one=True)
        if row:
            return ReservaModel(
                row['reserva_id'], row['tipo_reserva_id'], row['salon_id'], row['tipo_cocina_id'],
                row['persona'], row['telefono'], row['fecha'], row['ocupacion'], row['jornadas'], row['habitaciones']
            )  # Devuelve un objeto ReservaModel con los datos de la reserva
        return None
    
    def checkFechaOcupada(self, fecha, salon_id, reserva_id):
        """
        Verifica si una fecha y salón están ocupados por una reserva distinta.

        Args:
            fecha (datetime): La fecha que se desea verificar.
            salon_id (int): El ID del salón que se desea verificar.
            reserva_id (int): El ID de la reserva que se desea verificar.

        Returns:
            bool: True si la fecha y salón están ocupados, False si no.
        """
        query = "SELECT * FROM reservas where fecha = %s and salon_id = %s and reserva_id != %s"
        row = self.execute_query(query, (fecha, salon_id, reserva_id), fetch_one=True)
        if row:
            return True  # Si ya existe una reserva, la fecha está ocupada
        return False  # Si no existe ninguna reserva, la fecha está disponible
    
    def get_by_salon_id(self, salon_id):
        """
        Obtiene todas las reservas de un salón específico.

        Args:
            salon_id (int): El ID del salón del cual obtener las reservas.

        Returns:
            list: Lista de objetos ReservaModel.
        """
        query = "SELECT * FROM reservas WHERE salon_id = %s ORDER BY fecha"
        rows = self.execute_query(query, (salon_id,))
        if rows:
            return [
                ReservaModel(
                    row['reserva_id'], row['tipo_reserva_id'], row['salon_id'], row['tipo_cocina_id'],
                    row['persona'], row['telefono'], row['fecha'], row['ocupacion'], row['jornadas'], row['habitaciones']
                ) for row in rows
            ]  # Devuelve una lista de objetos ReservaModel
        return None

    def get_all(self):
        """
        Obtiene todas las reservas de la base de datos.

        Returns:
            list: Lista de objetos ReservaModel.
        """
        query = "SELECT * FROM reservas"
        rows = self.execute_query(query)
        return [
            ReservaModel(
                row['reserva_id'], row['tipo_reserva_id'], row['salon_id'], row['tipo_cocina_id'],
                row['persona'], row['telefono'], row['fecha'], row['ocupacion'], row['jornadas'], row['habitaciones']
            ) for row in rows
        ]  # Devuelve una lista de objetos ReservaModel

    def create(self, reserva: ReservaModel):
        """
        Crea una nueva reserva en la base de datos.

        Args:
            reserva (ReservaModel): El objeto ReservaModel con los datos de la nueva reserva.

        Returns:
            ReservaModel: El objeto ReservaModel de la reserva creada con su ID asignado.
        """
        query = """
        INSERT INTO reservas (tipo_reserva_id, salon_id, tipo_cocina_id, persona, telefono, fecha, ocupacion, jornadas, habitaciones) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        reserva_id = self.execute_query(query, (
            reserva.tipo_reserva_id, reserva.salon_id, reserva.tipo_cocina_id,
            reserva.persona, reserva.telefono, reserva.fecha,
            reserva.ocupacion, reserva.jornadas, reserva.habitaciones
        ))
        return self.get(reserva_id)  # Devuelve el objeto ReservaModel con los datos de la nueva reserva

    def update(self, reserva: ReservaModel):
        """
        Actualiza una reserva existente en la base de datos.

        Args:
            reserva (ReservaModel): El objeto ReservaModel con los datos actualizados de la reserva.

        Returns:
            ReservaModel: El objeto ReservaModel de la reserva actualizada.
        """
        query = """
        UPDATE reservas 
        SET tipo_reserva_id = %s, salon_id = %s, tipo_cocina_id = %s, persona = %s, telefono = %s, 
            fecha = %s, ocupacion = %s, jornadas = %s, habitaciones = %s 
        WHERE reserva_id = %s
        """
        self.execute_query(query, (
            reserva.tipo_reserva_id, reserva.salon_id, reserva.tipo_cocina_id,
            reserva.persona, reserva.telefono, reserva.fecha,
            reserva.ocupacion, reserva.jornadas, reserva.habitaciones,
            reserva.reserva_id
        ))
        return self.get(reserva.reserva_id)  # Devuelve el objeto ReservaModel de la reserva actualizada
