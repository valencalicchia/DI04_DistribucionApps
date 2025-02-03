from setuptools import setup, find_packages

setup(
    # Nombre del paquete
    name="tarea4",
    
    # Versión del paquete
    version="1.0",
    
    # Encontrar automáticamente los paquetes dentro de "tarea3"
    packages=find_packages(include=["tarea3", "tarea3.*"]),
    
    # Dependencias necesarias para el funcionamiento del paquete
    install_requires=[
        "click==8.1.8",  # Herramienta para crear interfaces de línea de comandos
        "colorama==0.4.6",  # Colores en la terminal
        "mysql-connector-python==9.2.0",  # Conector para bases de datos MySQL
        "PyQt6==6.4.2",  # Framework para crear interfaces gráficas con Qt en Python
        "pyqt6-plugins==6.4.2.2.3",  # Plugins adicionales para PyQt6
        "PyQt6-Qt6==6.4.3",  # Dependencia específica de Qt6 para PyQt6
        "pyqt6-tools==6.4.2.3.3",  # Herramientas adicionales para PyQt6
        "PyQt6_sip==13.9.1",  # Paquete de compatibilidad para PyQt6
        "PySide6==6.8.1.1",  # Alternativa a PyQt6 para trabajar con Qt en Python
        "PySide6_Addons==6.8.1.1",  # Complementos para PySide6
        "PySide6_Essentials==6.8.1.1",  # Funcionalidades esenciales de PySide6
        "python-dotenv==1.0.1",  # Manejo de variables de entorno desde archivos .env
        "qt6-applications==6.4.3.2.3",  # Aplicaciones prediseñadas para Qt6
        "qt6-tools==6.4.3.1.3",  # Herramientas adicionales para Qt6
        "shiboken6==6.8.1.1"  # Generador de enlaces C++ para PySide6
    ],
    
    # Información del autor del paquete
    author="Valentina Alessandra Calicchia",
    author_email="valentinacalicchia@gmail.com",
    
    # Breve descripción del paquete
    description="Un sistema de gestión de reservas",
    
    # Descripción detallada obtenida del archivo README.md
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type='text/markdown',

    # Definición de scripts de línea de comandos
    entry_points={
        "console_scripts": [
            "tarea4 = tarea3.main:main",  # Ejecuta la función `main()` dentro de `tarea3/main.py`
        ]
    },
    
    # Clasificación del paquete según criterios estándar
    classifiers=[
        'Programming Language :: Python :: 3',  # Indica que es compatible con Python 3
        'License :: OSI Approved :: MIT License',  # Licencia MIT
        'Operating System :: OS Independent',  # Compatible con cualquier sistema operativo
    ],
    
    # Versión mínima de Python requerida
    python_requires='>=3.10.12',
)
