from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QDate

from ..vistas.create_edit_reserva_ui import Ui_Reservar

from ..modelos.datos import ReservasDAO, SalonesDAO, TiposCocinaDAO, TiposReservasDAO, BaseDAO
from ..modelos.models import ReservaModel

from ..utilidades.message_box import MessageBox


class ReversaController(QDialog):
    """
    Controlador que gestiona la creación y modificación de reservas en la interfaz de usuario.
    Hereda de QDialog para mostrar un cuadro de diálogo modal.
    """

    def __init__(self, reserva_id, salon_id):
        """
        Constructor de la clase ReversaController.

        Args:
            reserva_id (int): Identificador de la reserva a modificar. Si es 0, se creará una nueva.
            salon_id (int): Identificador del salón donde se realizará la reserva.
        """
        try:
            super().__init__()  # Inicializa la clase QDialog
            self.ui = Ui_Reservar()  # Crea una instancia de la UI del formulario de reserva
            self.ui.setupUi(self)  # Configura la interfaz en el cuadro de diálogo

            self.init_daos()  # Inicializa los DAOs para manejar datos
            self.config_events()  # Configura los eventos (conexión de botones, etc.)

            self.salon_id = salon_id  # Asigna el ID del salón
            if reserva_id:  # Si hay un ID de reserva, significa que es una edición
                self.reserva_id = reserva_id
                self.reserva_modificacion = self.dao_reserva.get(self.reserva_id)  # Obtiene la reserva a editar
                self.es_editar = True  # Marca como edición
            else:  # Si no hay ID de reserva, es una nueva reserva
                self.reserva_id = 0
                self.es_editar = False
                self.reserva_modificacion = ReservaModel("","","","","","","","","")  # Reserva vacía para nueva

            self.init_ui()  # Inicializa la interfaz de usuario con los valores predeterminados

        except Exception as e:
            # Si ocurre un error, se muestra un mensaje de error
            MessageBox("Error al cargar el formulario de reservas", "error", str(e)).show()

    def config_events(self):
        """
        Configura los eventos para los botones y otras interacciones de la interfaz.
        """
        self.ui.vcbtnReservar.clicked.connect(self.confirm_reserva)  # Conecta el botón de reservar
        self.ui.vccboBoxTipoRes.currentTextChanged.connect(self.tipo_res_changed)  # Cambiar tipo de reserva

    def tipo_res_changed(self):
        """
        Maneja el cambio de tipo de reserva, mostrando u ocultando elementos relacionados con congresos.
        """
        self.tipo_reserva = self.ui.vccboBoxTipoRes.currentText()  # Obtiene el tipo de reserva seleccionado
        self.ui.vcchkBoxHabitaciones.setVisible(self.bCongreso())  # Muestra u oculta el checkbox de habitaciones si es Congreso
        self.ui.vcchkBoxHabitaciones.setChecked(False)  # Desmarca el checkbox por defecto

        self.ui.vcSpinBoxJornadas.setVisible(self.bCongreso())  # Muestra u oculta el spinbox de jornadas si es Congreso
        self.ui.vcSpinBoxJornadas.setValue(0)  # Restablece el valor por defecto a 0

        self.ui.vcLblJornadas.setVisible(self.bCongreso())  # Muestra u oculta la etiqueta de jornadas

    def bCongreso(self):
        """
        Devuelve True si el tipo de reserva es 'Congreso', de lo contrario False.
        """
        return self.tipo_reserva == "Congreso"

    def init_ui(self):
        """
        Inicializa la interfaz de usuario con los datos de los combo boxes y la fecha.
        Si es una edición, rellena los campos con los datos de la reserva seleccionada.
        """
        try:
            self.fill_cbobox_cocina()  # Llena el combo box de tipos de cocina
            self.fill_cbobox_tipo_reserva()  # Llena el combo box de tipos de reserva
            self.set_fecha()  # Establece la fecha actual o la de la reserva

            if self.es_editar:
                self.rellenar_datos()  # Si es una edición, rellena los campos con los datos de la reserva

        except Exception as e:
            # Si ocurre un error al inicializar la UI, muestra un mensaje de error
            MessageBox("Error al inicializar la UI", "error", str(e)).show()

    def init_daos(self):
        """
        Inicializa los objetos de acceso a datos (DAOs) necesarios para manejar la información de reservas,
        salones, tipos de cocina y tipos de reserva.
        """
        try:
            self.dao_salon = SalonesDAO()  # DAO para obtener los salones
            self.dao_reserva = ReservasDAO()  # DAO para obtener y manejar reservas
            self.dao_tipo_cocina = TiposCocinaDAO()  # DAO para obtener los tipos de cocina
            self.dao_tipo_reserva = TiposReservasDAO()  # DAO para obtener los tipos de reserva
        except Exception as e:
            # Si ocurre un error al inicializar los DAOs, muestra un mensaje de error
            MessageBox("Error al inicializar los DAOS", "error", str(e)).show()

    def rellenar_datos(self):
        """
        Rellena los campos de la interfaz con los datos de la reserva que se está editando.
        """
        tipo_reserva = self.dao_tipo_reserva.get(self.reserva_modificacion.tipo_reserva_id)
        tipo_cocina = self.dao_tipo_cocina.get(self.reserva_modificacion.tipo_cocina_id)
        if tipo_cocina:
            self.ui.vccboBoxTipoCocina.setCurrentText(tipo_cocina.nombre)  # Establece el tipo de cocina
        if tipo_reserva:
            self.ui.vccboBoxTipoRes.setCurrentText(tipo_reserva.nombre)  # Establece el tipo de reserva

        # Rellena los demás campos del formulario con los datos de la reserva
        self.ui.vcTxtNombre.setText(self.reserva_modificacion.persona)
        self.ui.vcTxtTelefono.setText(self.reserva_modificacion.telefono)
        self.ui.vcSpinBoxNAsist.setValue(self.reserva_modificacion.ocupacion)
        self.ui.vcchkBoxHabitaciones.setChecked(self.reserva_modificacion.habitaciones == 1)
        self.ui.vcSpinBoxJornadas.setValue(self.reserva_modificacion.jornadas)

    def fill_cbobox_cocina(self):
        """
        Llena el combo box de tipos de cocina con los datos obtenidos desde el DAO.
        """
        self.ui.vccboBoxTipoCocina.clear()  # Limpia el combo box antes de llenarlo
        cocinas = self.dao_tipo_cocina.get_all()  # Obtiene todos los tipos de cocina
        if not cocinas:
            self.close()  # Si no hay tipos de cocina, cierra la ventana
            raise ValueError("La consulta no devolvió tipos de cocina.")
        for cocina in cocinas:
            self.ui.vccboBoxTipoCocina.addItem(cocina.nombre, cocina.tipo_cocina_id)  # Agrega los tipos de cocina al combo box

    def fill_cbobox_tipo_reserva(self):
        """
        Llena el combo box de tipos de reserva con los datos obtenidos desde el DAO.
        """
        self.ui.vccboBoxTipoRes.clear()  # Limpia el combo box antes de llenarlo
        reservas = self.dao_tipo_reserva.get_all()  # Obtiene todos los tipos de reserva
        if not reservas:
            self.close()  # Si no hay tipos de reserva, cierra la ventana
            raise ValueError("La consulta no devolvió tipos de reservas.")
        for reserva in reservas:
            self.ui.vccboBoxTipoRes.addItem(reserva.nombre, reserva.tipo_reserva_id)  # Agrega los tipos de reserva al combo box

    def set_fecha(self):
        """
        Establece la fecha en el calendario de la UI. Si es edición, establece la fecha de la reserva.
        """
        fecha_hoy = QDate.currentDate()  # Obtiene la fecha actual
        if self.es_editar:
            # Si es edición, establece la fecha de la reserva
            fecha_str = self.reserva_modificacion.fecha.strftime("%Y-%m-%d")
            fecha = QDate.fromString(fecha_str, "yyyy-MM-dd")
        else:
            fecha = fecha_hoy  # Si es nueva reserva, establece la fecha de hoy

        self.ui.vcdateEdit.setDate(fecha)  # Establece la fecha en el calendario
        self.ui.vcdateEdit.setMinimumDate(fecha_hoy)  # Asegura que la fecha mínima sea hoy
        self.ui.vcdateEdit.setCalendarPopup(True)  # Habilita el popup del calendario
        self.ui.vcdateEdit.setDisplayFormat("yyyy-MM-dd")  # Formato de visualización de la fecha

    def confirm_reserva(self):
        """
        Confirma la creación o modificación de la reserva.
        """
        nombre = self.ui.vcTxtNombre.text().strip()
        telefono = self.ui.vcTxtTelefono.text().strip()

        if not bool(nombre) or not bool(telefono):
            # Si falta algún campo obligatorio, muestra un mensaje de advertencia
            MessageBox("Todos los campos son obligatorios.", "warning").show()
            return

        reserva = self.set_reserva(nombre, telefono)  # Crea una nueva reserva con los datos
        if reserva:
            self.safe(reserva)  # Guarda la reserva en la base de datos

    def set_reserva(self, nombre, telefono):
        """
        Crea y devuelve un objeto ReservaModel con los datos de la reserva, si la fecha es válida.
        """
        fecha = self.ui.vcdateEdit.date().toPython()  # Convierte la fecha seleccionada a formato Python

        if self.dao_reserva.checkFechaOcupada(fecha, self.salon_id, self.reserva_id) == False:
            # Si la fecha no está ocupada, crea una nueva reserva
            return ReservaModel(
                reserva_id=self.reserva_id,
                persona=nombre,
                telefono=telefono,
                fecha=fecha, 
                tipo_reserva_id=self.ui.vccboBoxTipoRes.currentData(),
                salon_id=self.salon_id,
                tipo_cocina_id=self.ui.vccboBoxTipoCocina.currentData(),
                ocupacion=self.ui.vcSpinBoxNAsist.value(),
                jornadas=self.ui.vcSpinBoxJornadas.value(),
                habitaciones=int(self.ui.vcchkBoxHabitaciones.isChecked()),
            )
        else:
            # Si la fecha ya está ocupada, muestra un mensaje de advertencia
            MessageBox("La fecha no está disponible", "warning").show()

        return None

    def safe(self, reserva):
        """
        Guarda la reserva en la base de datos, ya sea actualizando o creando una nueva.
        """
        try:
            if self.es_editar:
                self.dao_reserva.update(reserva)  # Actualiza la reserva si es una modificación
            else:
                self.dao_reserva.create(reserva)  # Crea una nueva reserva si no es edición

            respuesta = MessageBox("Operación exitosa").show()  # Muestra un mensaje de éxito
            if respuesta:
                self.accept()  # Acepta el formulario y cierra la ventana
                self.close()

        except Exception as e:
            # Si ocurre un error al guardar, muestra un mensaje de error
            MessageBox("Error al procesar la operación", "error", str(e)).show()
