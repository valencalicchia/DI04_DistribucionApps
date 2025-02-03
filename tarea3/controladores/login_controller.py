from PySide6.QtCore import QObject
from PySide6.QtWidgets import QWidget
from ..vistas.login_ui import Ui_Login
from ..utilidades.message_box import MessageBox

class LoginController(Ui_Login, QObject):
    """
    Controlador para gestionar el proceso de inicio de sesión en la interfaz de usuario.
    """

    def __init__(self, login_window: QWidget):
        """
        Constructor de la clase LoginController.

        Args:
            login_window (QWidget): La ventana de inicio de sesión.
        """
        self.bLogado = False  # Variable para controlar si el usuario ha iniciado sesión con éxito
        super().__init__()
        self.ui = Ui_Login()  # Inicializa la interfaz de usuario del login
        self.login_window = login_window  # Asigna la ventana pasada como parámetro
        self.ui.setupUi(self.login_window)  # Configura la UI en la ventana de login
        self.ui.vCBtnAcceder.clicked.connect(self.login)  # Conecta el botón de acceso con la función login
        
    def login(self):
        """
        Maneja el proceso de autenticación del usuario cuando se presiona el botón de acceso.
        """
        # Obtiene y limpia los datos ingresados por el usuario
        user = self.ui.vCTxtUsuario.text().strip()
        pwd = self.ui.vCTxtPwd.text().strip()

        message = "Logado con éxito" 
        msg_type = "error"

        # Verifica las credenciales ingresadas
        self.bLogado = self.autenticar(user, pwd)

        # Valida si los campos están vacíos
        if not user or not pwd:
            message = "Ambos campos son obligatorios"
        elif self.bLogado == False:
            message = "Usuario o contraseña incorrectos"
        elif self.bLogado:
            msg_type = "success"  # Cambia el tipo de mensaje a éxito si la autenticación es correcta
            
        # Crea y muestra un cuadro de mensaje personalizado con el resultado del login
        MessageBox(message, msg_type).show()

        # Si la autenticación es correcta, cierra la ventana de login
        if self.bLogado:
            self.login_window.close()

    def autenticar(self, user, pwd):
        """
        Verifica las credenciales del usuario.

        Args:
            user (str): Nombre de usuario ingresado.
            pwd (str): Contraseña ingresada.

        Returns:
            bool: True si las credenciales son correctas, False en caso contrario.
        """
        return user == "hotel" and pwd == "Brianda23$"