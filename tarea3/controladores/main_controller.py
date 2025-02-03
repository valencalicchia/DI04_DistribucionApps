from PySide6.QtWidgets import QAbstractItemView, QDialog, QHeaderView, QMainWindow
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtCore import QModelIndex

from ..vistas.reservas_ui import Ui_MostrarReservas
from ..modelos.datos import ReservasDAO, SalonesDAO, TiposCocinaDAO, TiposReservasDAO, BaseDAO
from ..controladores.reserva_controller import ReversaController
from ..utilidades.message_box import MessageBox

class MainCotroller(QMainWindow):
    def __init__(self):
        """
        Constructor de la clase MainCotroller, que se encarga de gestionar la ventana principal 
        y las interacciones con las reservas de los salones.
        """
        super().__init__()
        self.ui = Ui_MostrarReservas()  # Inicializa la interfaz de usuario
        self.ui.setupUi(self)  # Configura la interfaz en la ventana principal
        self.salon_maping = {}  # Mapa para almacenar las relaciones entre salon_id y su nombre

        self.init_daos()  # Inicializa los DAOs (Data Access Objects) necesarios
        self.init_ui()  # Configura la UI

    def init_daos(self):
        """
        Inicializa los DAOs necesarios para interactuar con la base de datos.
        """
        try:
            self.dao_salon = SalonesDAO()  # DAO para salones
            self.dao_tipo_cocina = TiposCocinaDAO()  # DAO para tipos de cocina
            self.dao_tipo_reserva = TiposReservasDAO()  # DAO para tipos de reservas
        except Exception as e:
            MessageBox("Error al inicializar los DAOS", "error", str(e)).show()  # Muestra un mensaje de error si ocurre una excepción

    def init_ui(self):
        """
        Configura la interfaz de usuario, incluyendo la obtención de salones, 
        configuración de eventos y de la tabla de reservas.
        """
        try:
            self.get_salones()  # Obtiene la lista de salones
            self.config_events()  # Configura los eventos de la UI
            self.config_table()  # Configura la tabla de reservas
        except Exception as e:
            MessageBox("Error al configurar la UI", "error", str(e)).show()  # Muestra un mensaje de error si algo sale mal

    def get_salones(self):
        """
        Obtiene la lista de salones desde la base de datos y los mapea para su uso en la UI.
        """
        salones = self.dao_salon.get_all()  # Obtiene todos los salones de la base de datos

        if not salones:
            raise ValueError("La consulta no devolvió salones.")  # Si no se encuentran salones, lanza una excepción

        for salon in salones:
            self.salon_maping[salon.salon_id] = salon.nombre  # Asocia el salon_id con su nombre

        self.ui.vcListWidSalones.clear()  # Limpia la lista de salones
        self.ui.vcListWidSalones.addItems(list(self.salon_maping.values()))  # Añade los nombres de los salones a la lista
        self.ui.vcListWidSalones.setCurrentRow(0)  # Selecciona el primer salón
        self.salon_selecionado = 1  # Establece el salón seleccionado por defecto

    def config_events(self):
        """
        Configura los eventos de la interfaz de usuario.
        """
        self.ui.vcGridReservas.clicked.connect(self.click_reserva)  # Conecta el clic en la tabla de reservas a la función click_reserva
        self.ui.vcListWidSalones.currentTextChanged.connect(self.salon_changed)  # Conecta el cambio de salón seleccionado a la función salon_changed
        self.ui.vcbtnModificar.clicked.connect(lambda: self.open_modal(False))  # Abre el modal de modificación de reserva
        self.ui.vcbtnReservar.clicked.connect(lambda: self.open_modal(True))  # Abre el modal para una nueva reserva

    def salon_changed(self, salon_select):
        """
        Actualiza el salón seleccionado cuando el usuario cambia la selección en la lista de salones.
        """
        salon_nombre = salon_select
        
        for salon_id, nombre in self.salon_maping.items():
            if nombre == salon_nombre:
                self.salon_selecionado = salon_id  # Actualiza el salón seleccionado
                break
        
        self.config_table()  # Actualiza la tabla de reservas para el salón seleccionado

    def config_table(self):
        """
        Configura la tabla de reservas, mostrando las reservas para el salón seleccionado.
        """
        dao_reserva = ReservasDAO()  # DAO para las reservas
        self.reserva_seleccionada = 0  # Inicializa la variable de reserva seleccionada
        headers = ["Fecha", "Persona", "Teléfono", "Tipo de Reserva", "Id"]  # Encabezados de la tabla

        # Obtener datos desde los DAOs
        reservas = dao_reserva.get_by_salon_id(self.salon_selecionado)  # Obtiene las reservas para el salón seleccionado
        tipos_reserva = self.dao_tipo_reserva.get_all()  # Obtiene todos los tipos de reserva

        # Crear un diccionario para mapear tipo_reserva_id -> nombre
        mapa_tipos = {tipo.tipo_reserva_id: tipo.nombre for tipo in tipos_reserva}

        # Mapear cada reserva para agregar el nombre del tipo de reserva
        for reserva in reservas:
            reserva.tipo_reserva_nombre = mapa_tipos.get(reserva.tipo_reserva_id, "Desconocido")

        # Crear el modelo de la tabla
        self.model = QStandardItemModel(len(reservas), len(headers))  # Modelo de la tabla con las filas y columnas necesarias
        self.model.setHorizontalHeaderLabels(headers)  # Establece los encabezados de la tabla

        # Llenar el modelo con datos de las reservas
        for row, reserva in enumerate(reservas):
            fecha_str = reserva.fecha.strftime("%Y-%m-%d")  # 🔹 Convierte la fecha a string
            self.model.setItem(row, 0, QStandardItem(fecha_str))  # Coloca la fecha en la primera columna
            self.model.setItem(row, 1, QStandardItem(reserva.persona))  # Coloca el nombre de la persona en la segunda columna
            self.model.setItem(row, 2, QStandardItem(reserva.telefono))  # Coloca el teléfono en la tercera columna
            self.model.setItem(row, 3, QStandardItem(reserva.tipo_reserva_nombre))  # Coloca el tipo de reserva
            self.model.setItem(row, 4, QStandardItem(str(reserva.reserva_id)))  # Coloca el ID de la reserva en la última columna

        # Configura la vista de la tabla
        self.ui.vcGridReservas.setModel(self.model)  # Establece el modelo de datos en la vista de la tabla
        self.ui.vcGridReservas.setColumnHidden(4, True)  # Esconde la columna 4 (ID) de la vista
        self.ui.vcGridReservas.resizeColumnsToContents()  # Ajusta el tamaño de las columnas automáticamente
        self.ui.vcGridReservas.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 🔹 Estira las columnas para ocupar todo el espacio disponible
        self.ui.vcGridReservas.horizontalHeader().setMinimumSectionSize(100)  # Establece un tamaño mínimo de sección
        self.ui.vcGridReservas.horizontalHeader().setStretchLastSection(True)  # Asegura que la última columna se estire
        self.ui.vcGridReservas.setSelectionBehavior(QAbstractItemView.SelectRows)  # Selecciona filas completas
        self.ui.vcGridReservas.setSelectionMode(QAbstractItemView.SingleSelection)  # 🔹 Solo permite la selección de una fila a la vez

        self.ui.vcGridReservas.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )  # Desactiva la edición de las celdas de la tabla

    def open_modal(self, nueva):
        """
        Abre el modal para crear o modificar una reserva.
        """
        if self.reserva_seleccionada != 0 or nueva:
            if nueva:
                self.controlador = ReversaController(None, self.salon_selecionado)  # Controlador para nueva reserva
            else:
                self.controlador = ReversaController(self.reserva_seleccionada, self.salon_selecionado)  # Controlador para modificar una reserva existente

            if not isinstance(self.controlador, QDialog):
                raise TypeError(
                    "El controlador debe heredar de QDialog para ser modal."
                )  # Asegura que el controlador sea un QDialog modal
            self.controlador.setModal(True)  # Establece el controlador como modal
            self.controlador.finished.connect(self.config_table)  # Cuando el modal se cierra, actualiza la tabla
            self.controlador.exec()  # Ejecuta el modal
        else:
            MessageBox("Seleccione una reserva para modificar", "warning").show()  # Muestra un mensaje de advertencia si no hay ninguna reserva seleccionada

    def click_reserva(self, index: QModelIndex):
        """
        Maneja el clic sobre una reserva en la tabla para seleccionarla.
        """
        row = index.row()  # Obtiene la fila seleccionada

        # Obtiene el valor de la columna 4 (ID) de esa fila
        reserva_id_item = self.model.item(row, 4)  # Columna 4 (index base 0)

        if reserva_id_item:
            self.reserva_seleccionada = reserva_id_item.text() or 0  # Obtiene el ID de la reserva como texto o 0 si no se encuentra
