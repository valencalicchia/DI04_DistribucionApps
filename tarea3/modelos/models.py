class TipoCocinaModel:
    """
    Representa el modelo de un tipo de cocina.
    Contiene los atributos que definen un tipo de cocina.
    """
    def __init__(self, tipo_cocina_id, nombre):
        """
        Inicializa el objeto TipoCocinaModel con los atributos proporcionados.

        Args:
            tipo_cocina_id (int): El ID único del tipo de cocina.
            nombre (str): El nombre del tipo de cocina.
        """
        self.tipo_cocina_id = tipo_cocina_id  # ID único del tipo de cocina
        self.nombre = nombre  # Nombre del tipo de cocina

    def __repr__(self):
        """
        Representación en forma de cadena del objeto TipoCocinaModel para facilitar su visualización.

        Returns:
            str: Cadena con la representación del objeto.
        """
        return f"TipoCocina(tipo_cocina_id={self.tipo_cocina_id}, nombre='{self.nombre}')"


class SalonModel:
    """
    Representa el modelo de un salón.
    Contiene los atributos que definen un salón en el contexto de las reservas.
    """
    def __init__(self, salon_id, nombre):
        """
        Inicializa el objeto SalonModel con los atributos proporcionados.

        Args:
            salon_id (int): El ID único del salón.
            nombre (str): El nombre del salón.
        """
        self.salon_id = salon_id  # ID único del salón
        self.nombre = nombre  # Nombre del salón

    def __repr__(self):
        """
        Representación en forma de cadena del objeto SalonModel para facilitar su visualización.

        Returns:
            str: Cadena con la representación del objeto.
        """
        return f"Salon(salon_id={self.salon_id}, nombre='{self.nombre}')"


class TipoReservaModel:
    """
    Representa el modelo de un tipo de reserva.
    Contiene los atributos que definen un tipo de reserva.
    """
    def __init__(self, tipo_reserva_id, nombre):
        """
        Inicializa el objeto TipoReservaModel con los atributos proporcionados.

        Args:
            tipo_reserva_id (int): El ID único del tipo de reserva.
            nombre (str): El nombre del tipo de reserva (por ejemplo, si es una reserva para un evento o una comida).
        """
        self.tipo_reserva_id = tipo_reserva_id  # ID único del tipo de reserva
        self.nombre = nombre  # Nombre del tipo de reserva

    def __repr__(self):
        """
        Representación en forma de cadena del objeto TipoReservaModel para facilitar su visualización.

        Returns:
            str: Cadena con la representación del objeto.
        """
        return f"TipoReserva(tipo_reserva_id={self.tipo_reserva_id}, nombre='{self.nombre}')"


class ReservaModel:
    """
    Representa el modelo de una reserva.
    Contiene los atributos que definen una reserva realizada en un salón, con un tipo de cocina y un tipo de reserva.
    """
    def __init__(self, reserva_id, tipo_reserva_id, salon_id, tipo_cocina_id, persona, telefono, fecha, ocupacion, jornadas, habitaciones=0):
        """
        Inicializa el objeto ReservaModel con los atributos proporcionados.

        Args:
            reserva_id (int): El ID único de la reserva.
            tipo_reserva_id (int): El ID del tipo de reserva (relacionado con la clase TipoReservaModel).
            salon_id (int): El ID del salón reservado (relacionado con la clase SalonModel).
            tipo_cocina_id (int): El ID del tipo de cocina (relacionado con la clase TipoCocinaModel).
            persona (str): El nombre de la persona que realizó la reserva.
            telefono (str): El teléfono de la persona que realizó la reserva.
            fecha (str): La fecha y hora de la reserva.
            ocupacion (int): Número de personas que asistirán.
            jornadas (int): Número de jornadas de la reserva (pueden ser varios días si es necesario).
            habitaciones (int): Número de habitaciones (por defecto es 0, si aplica).
        """
        self.reserva_id = reserva_id  # ID único de la reserva
        self.tipo_reserva_id = tipo_reserva_id  # ID del tipo de reserva
        self.salon_id = salon_id  # ID del salón reservado
        self.tipo_cocina_id = tipo_cocina_id  # ID del tipo de cocina asociado
        self.persona = persona  # Nombre de la persona que realizó la reserva
        self.telefono = telefono  # Teléfono de la persona que realizó la reserva
        self.fecha = fecha  # Fecha y hora de la reserva
        self.ocupacion = ocupacion  # Número de personas en la reserva
        self.jornadas = jornadas  # Número de jornadas (días)
        self.habitaciones = habitaciones  # Número de habitaciones (por defecto 0 si no aplica)

    def __repr__(self):
        """
        Representación en forma de cadena del objeto ReservaModel para facilitar su visualización.

        Returns:
            str: Cadena con la representación del objeto.
        """
        return f"Reserva(reserva_id={self.reserva_id}, tipo_reserva_id={self.tipo_reserva_id}, salon_id={self.salon_id}, tipo_cocina_id={self.tipo_cocina_id}, persona='{self.persona}', telefono='{self.telefono}', fecha='{self.fecha}', ocupacion={self.ocupacion}, jornadas={self.jornadas}, habitaciones={self.habitaciones})"
