CREATE SCHEMA `TAREA3DI`;

USE TAREA3DI;

-- Inicia la transacción
START TRANSACTION;

-- Creación de la tabla de tipos de cocina
CREATE TABLE tipos_cocina (
    tipo_cocina_id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    PRIMARY KEY (tipo_cocina_id)
);

-- Creación de la tabla de salones
CREATE TABLE salones (
    salon_id INT NOT NULL AUTO_INCREMENT UNIQUE,
    nombre VARCHAR(255) NOT NULL,
    PRIMARY KEY (salon_id)
);

-- Creación de la tabla de tipos de reserva
CREATE TABLE tipos_reservas (
    tipo_reserva_id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    requiere_jornadas TINYINT(1) NOT NULL DEFAULT 0,
    requiere_habitaciones TINYINT(1) NOT NULL DEFAULT 0,
    PRIMARY KEY (tipo_reserva_id)
);

-- Creación de la tabla de reservas
CREATE TABLE reservas (
    reserva_id INT NOT NULL AUTO_INCREMENT,
    tipo_reserva_id INT NOT NULL,
    salon_id INT NOT NULL,
    tipo_cocina_id INT NOT NULL,
    persona VARCHAR(255) NOT NULL,
    telefono VARCHAR(25) NOT NULL,
    fecha DATE NOT NULL,
    ocupacion INT NOT NULL,
    jornadas INT NOT NULL,
    habitaciones INT NOT NULL DEFAULT 0,
    PRIMARY KEY (reserva_id),
    FOREIGN KEY (tipo_reserva_id) REFERENCES tipos_reservas(tipo_reserva_id),
    FOREIGN KEY (tipo_cocina_id) REFERENCES tipos_cocina(tipo_cocina_id),
    FOREIGN KEY (salon_id) REFERENCES salones(salon_id),
    UNIQUE KEY (salon_id, fecha)
);

-- Inserción de datos en la tabla tipos_reservas
INSERT INTO tipos_reservas (tipo_reserva_id, nombre, requiere_jornadas, requiere_habitaciones) VALUES
(1, 'Banquete', 0, 0),
(2, 'Jornada', 0, 0),
(3, 'Congreso', 1, 1);

-- Inserción de datos en la tabla tipos_cocina
INSERT INTO tipos_cocina (tipo_cocina_id, nombre) VALUES
(1, 'Bufé'),
(2, 'Carta'),
(3, 'Pedir cita con el chef'),
(4, 'No precisa');

-- Inserción de datos en la tabla salones
INSERT INTO salones (salon_id, nombre) VALUES
(1, 'Salón Habana'),
(2, 'Otro Salón');

-- Creación del índice único para reservas
CREATE UNIQUE INDEX index_reservas ON reservas (fecha, salon_id);

-- Inserción de datos en la tabla reservas
INSERT INTO reservas (reserva_id, tipo_reserva_id, salon_id, tipo_cocina_id, persona, telefono, fecha, ocupacion, jornadas, habitaciones) VALUES
(1, 1, 1, 1, 'David', '600123456', '2024-12-20', 35, 0, 0),
(2, 2, 2, 2, 'Juan', '123456780', '2024-11-17', 2, 0, 0),
(3, 1, 2, 1, 'Juan', '123456789', '2024-11-16', 1, 0, 0),
(4, 2, 2, 1, 'Perico', '666778899', '2024-11-15', 3, 0, 0),
(5, 1, 1, 2, 'David', '111223344', '2024-11-20', 35, 0, 0),
(6, 1, 1, 1, 'David', '222334455', '2024-11-21', 3, 0, 0),
(7, 3, 2, 3, 'Jacinto', '333445566', '2024-12-21', 2, 2, 0),
(8, 1, 1, 1, 'Jacinto', '444556677', '2024-10-21', 1, 0, 0),
(9, 1, 2, 1, 'Fernando', '555667788', '2024-10-21', 1, 0, 0),
(10, 3, 1, 2, 'Luis', '645704341', '2024-12-01', 3, 1, 1),
(11, 2, 1, 2, 'Azucena', '345243654', '2024-10-01', 5, 0, 0),
(12, 2, 1, 2, 'Azucena', '345243654', '2024-10-02', 5, 0, 0);

-- Confirma la transacción
COMMIT;
