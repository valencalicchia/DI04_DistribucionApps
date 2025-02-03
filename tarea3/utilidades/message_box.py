from PySide6.QtWidgets import QMessageBox

class MessageBox(QMessageBox):
    def __init__(self, message, message_type="info", details=None):
        """
        Inicializa un cuadro de mensaje genérico.

        Args:
            message (str): El mensaje a mostrar.
            message_type (str): Tipo de mensaje ('info', 'error', 'warning', 'success').
            details (str, opcional): Detalles adicionales del mensaje.
        """
        super().__init__()
        self.setWindowTitle(message_type.capitalize())
        self.setText(message)
        
        icon_mapping = {
            "info": QMessageBox.Icon.Information,
            "error": QMessageBox.Icon.Critical,
            "warning": QMessageBox.Icon.Warning,
            "success": QMessageBox.Icon.Information,
        }
        
        self.setIcon(icon_mapping.get(message_type, QMessageBox.Icon.Information))
        
        if details:
            self.setDetailedText(details)
    
    def show(self):
        """
        Muestra el cuadro de mensaje.
        """
        return self.exec()