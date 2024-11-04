-- --------------------------------------------------------
-- Host:                         localhost
-- Versión del servidor:         8.0.30 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para gestor_biblioteca
CREATE DATABASE IF NOT EXISTS `gestor_biblioteca` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `gestor_biblioteca`;

-- Volcando estructura para tabla gestor_biblioteca.generos
CREATE TABLE IF NOT EXISTS `generos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `genero` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla gestor_biblioteca.generos: ~5 rows (aproximadamente)
INSERT INTO `generos` (`id`, `genero`) VALUES
	(1, 'Ficción'),
	(2, 'No ficción'),
	(3, 'Ciencia Ficción'),
	(4, 'Fantástico'),
	(5, 'Romántico');

-- Volcando estructura para tabla gestor_biblioteca.libros
CREATE TABLE IF NOT EXISTS `libros` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre_libro` varchar(100) NOT NULL,
  `autor` varchar(100) NOT NULL,
  `fecha_lanzamiento` date NOT NULL,
  `id_genero` int DEFAULT NULL,
  `creado_el` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `actualizado_el` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `estado` tinyint DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `id_genero` (`id_genero`),
  CONSTRAINT `libros_ibfk_1` FOREIGN KEY (`id_genero`) REFERENCES `generos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla gestor_biblioteca.libros: ~49 rows (aproximadamente)
INSERT INTO `libros` (`id`, `nombre_libro`, `autor`, `fecha_lanzamiento`, `id_genero`, `creado_el`, `actualizado_el`, `estado`) VALUES
	(2, 'El Gran Gatsby', 'F. Scott Fitzgerald', '1925-04-10', 1, '2024-11-04 04:15:05', '2024-11-04 04:15:05', 1),
	(3, 'Cien años de soledad', 'Gabriel García Márquez', '1967-05-30', 1, '2024-11-04 04:15:05', '2024-11-04 04:15:05', 1),
	(4, '1984', 'George Orwell', '1949-06-08', 1, '2024-11-04 04:15:05', '2024-11-04 04:15:05', 1),
	(5, 'Moby Dick', 'Herman Melville', '1851-10-18', 1, '2024-11-04 04:15:05', '2024-11-04 04:15:05', 1),
	(6, 'Orgullo y prejuicio', 'Jane Austen', '1813-01-28', 1, '2024-11-04 04:15:05', '2024-11-04 04:15:05', 1),
	(7, 'El túnel', 'Ernesto Sabato', '1948-04-01', 1, '2024-11-04 04:15:05', '2024-11-04 04:15:05', 1),
	(8, 'Crónica de una muerte anunciada', 'Gabriel García Márquez', '1981-04-01', 1, '2024-11-04 04:15:05', '2024-11-04 04:15:05', 1),
	(9, 'La sombra del viento', 'Carlos Ruiz Zafón', '2001-04-17', 1, '2024-11-04 04:15:05', '2024-11-04 04:15:05', 1),
	(10, 'El alquimista', 'Paulo Coelho', '1988-05-01', 1, '2024-11-04 04:15:05', '2024-11-04 04:15:05', 1),
	(11, 'Las cosas que perdimos en el fuego', 'Mariana Enriquez', '2016-08-01', 1, '2024-11-04 04:15:05', '2024-11-04 04:15:05', 1),
	(12, 'Sapiens: De animales a dioses', 'Yuval Noah Harari', '2011-01-01', 2, '2024-11-04 04:22:16', '2024-11-04 04:22:16', 1),
	(13, 'Educated', 'Tara Westover', '2018-02-20', 2, '2024-11-04 04:22:16', '2024-11-04 04:22:16', 1),
	(14, 'The Immortal Life of Henrietta Lacks', 'Rebecca Skloot', '2010-02-02', 2, '2024-11-04 04:22:16', '2024-11-04 04:22:16', 1),
	(15, 'Becoming', 'Michelle Obama', '2018-11-13', 2, '2024-11-04 04:22:16', '2024-11-04 04:22:16', 1),
	(16, 'The Wright Brothers', 'David McCullough', '2015-05-05', 2, '2024-11-04 04:22:16', '2024-11-04 04:22:16', 1),
	(17, 'In Cold Blood', 'Truman Capote', '1966-01-17', 2, '2024-11-04 04:22:16', '2024-11-04 04:22:16', 1),
	(18, 'Outliers', 'Malcolm Gladwell', '2008-11-18', 2, '2024-11-04 04:22:16', '2024-11-04 04:22:16', 1),
	(19, 'The Body Keeps the Score', 'Bessel van der Kolk', '2014-09-08', 2, '2024-11-04 04:22:16', '2024-11-04 04:22:16', 1),
	(20, 'Freakonomics', 'Steven D. Levitt y Stephen J. Dubner', '2005-04-12', 2, '2024-11-04 04:22:16', '2024-11-04 04:22:16', 1),
	(21, 'Born a Crime', 'Trevor Noah', '2016-11-15', 2, '2024-11-04 04:22:16', '2024-11-04 04:22:16', 1),
	(22, 'Dune', 'Frank Herbert', '1965-08-01', 3, '2024-11-04 04:23:47', '2024-11-04 04:23:47', 1),
	(23, 'Neuromancer', 'William Gibson', '1984-07-01', 3, '2024-11-04 04:23:47', '2024-11-04 04:23:47', 1),
	(24, 'The Hitchhiker\'s Guide to the Galaxy', 'Douglas Adams', '1979-10-12', 3, '2024-11-04 04:23:47', '2024-11-04 04:23:47', 1),
	(25, 'Foundation', 'Isaac Asimov', '1951-06-01', 3, '2024-11-04 04:23:47', '2024-11-04 04:23:47', 1),
	(26, 'Fahrenheit 451', 'Ray Bradbury', '1953-10-19', 3, '2024-11-04 04:23:47', '2024-11-04 04:23:47', 1),
	(27, 'Snow Crash', 'Neal Stephenson', '1992-06-01', 3, '2024-11-04 04:23:47', '2024-11-04 04:23:47', 1),
	(28, 'The Left Hand of Darkness', 'Ursula K. Le Guin', '1969-03-01', 3, '2024-11-04 04:23:47', '2024-11-04 04:23:47', 1),
	(29, 'Hyperion', 'Dan Simmons', '1989-05-01', 3, '2024-11-04 04:23:47', '2024-11-04 04:23:47', 1),
	(30, 'The Martian', 'Andy Weir', '2011-02-11', 3, '2024-11-04 04:23:47', '2024-11-04 04:23:47', 1),
	(31, 'El Hobbit', 'J.R.R. Tolkien', '1937-09-21', 4, '2024-11-04 04:25:31', '2024-11-04 04:25:31', 1),
	(32, 'Harry Potter y la piedra filosofal', 'J.K. Rowling', '1997-06-26', 4, '2024-11-04 04:25:31', '2024-11-04 04:25:31', 1),
	(33, 'Crónicas de Narnia: El león, la bruja y el armario', 'C.S. Lewis', '1950-10-16', 4, '2024-11-04 04:25:31', '2024-11-04 04:25:31', 1),
	(34, 'La historia interminable', 'Michael Ende', '1979-09-01', 4, '2024-11-04 04:25:31', '2024-11-04 04:25:31', 1),
	(35, 'El nombre del viento', 'Patrick Rothfuss', '2007-03-27', 4, '2024-11-04 04:25:31', '2024-11-04 04:25:31', 1),
	(36, 'American Gods', 'Neil Gaiman', '2001-06-19', 4, '2024-11-04 04:25:31', '2024-11-04 04:25:31', 1),
	(37, 'Un mago de Terramar', 'Ursula K. Le Guin', '1968-08-01', 4, '2024-11-04 04:25:31', '2024-11-04 04:25:31', 1),
	(38, 'El ciclo de la puerta de la muerte', 'Margaret Weis y Tracy Hickman', '1990-09-01', 4, '2024-11-04 04:25:31', '2024-11-04 04:25:31', 1),
	(39, 'La brújula dorada', 'Philip Pullman', '1995-07-01', 4, '2024-11-04 04:25:31', '2024-11-04 04:25:31', 1),
	(40, 'Elantris', 'Brandon Sanderson', '2005-04-21', 4, '2024-11-04 04:26:01', '2024-11-04 04:26:01', 1),
	(41, 'Orgullo y prejuicio', 'Jane Austen', '1813-01-28', 5, '2024-11-04 04:26:54', '2024-11-04 04:26:54', 1),
	(42, 'Cumbres borrascosas', 'Emily Brontë', '1847-12-01', 5, '2024-11-04 04:26:54', '2024-11-04 04:26:54', 1),
	(43, 'El diario de una pasión', 'Nicholas Sparks', '1996-10-01', 5, '2024-11-04 04:26:54', '2024-11-04 04:26:54', 1),
	(44, 'Bajo la misma estrella', 'John Green', '2012-01-10', 5, '2024-11-04 04:26:54', '2024-11-04 04:26:54', 1),
	(45, 'Como agua para chocolate', 'Laura Esquivel', '1989-01-01', 5, '2024-11-04 04:26:54', '2024-11-04 04:26:54', 1),
	(46, 'Cazadores de sombras: Ciudad de hueso', 'Cassandra Clare', '2007-03-27', 5, '2024-11-04 04:26:54', '2024-11-04 04:26:54', 1),
	(47, 'El psicoanalista', 'John Katzenbach', '2002-04-01', 5, '2024-11-04 04:26:54', '2024-11-04 04:26:54', 1),
	(48, 'El tiempo entre costuras', 'María Dueñas', '2013-04-01', 5, '2024-11-04 04:26:54', '2024-11-04 04:26:54', 1),
	(49, 'Un viaje a las estrellas', 'María García Esperón', '2010-11-01', 5, '2024-11-04 04:26:54', '2024-11-04 04:26:54', 1),
	(50, 'A todos los chicos de los que me enamoré', 'Jenny Han', '2014-04-15', 5, '2024-11-04 04:26:54', '2024-11-04 04:26:54', 1);

-- Volcando estructura para tabla gestor_biblioteca.prestamos
CREATE TABLE IF NOT EXISTS `prestamos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int NOT NULL,
  `libro_id` int NOT NULL,
  `fecha_prestamo` date NOT NULL,
  `fecha_devolucion_estimada` date NOT NULL,
  `fecha_devolucion_real` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usuario_id` (`usuario_id`),
  KEY `libro_id` (`libro_id`),
  CONSTRAINT `prestamos_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`),
  CONSTRAINT `prestamos_ibfk_2` FOREIGN KEY (`libro_id`) REFERENCES `libros` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla gestor_biblioteca.prestamos: ~0 rows (aproximadamente)

-- Volcando estructura para tabla gestor_biblioteca.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `dni` varchar(8) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `creado_el` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `actualizado_el` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `estado` tinyint DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `dni` (`dni`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla gestor_biblioteca.usuarios: ~59 rows (aproximadamente)
INSERT INTO `usuarios` (`id`, `nombre`, `apellido`, `dni`, `telefono`, `email`, `creado_el`, `actualizado_el`, `estado`) VALUES
	(1, 'Juan Manuel', 'Vargas', '45950603', '3482545829', 'juanmanuelcontacto332@gmail.com', '2024-10-27 17:10:25', '2024-10-27 22:47:59', 0),
	(2, 'Maximo', 'Checo', '66958658', '3482212526', 'checho@gmail.com', '2024-10-27 22:16:35', '2024-10-27 22:46:38', 0),
	(3, 'Rocio', 'Delgado', '45955605', '3482545829', 'rocio@gmail.com', '2024-10-27 23:05:42', '2024-10-27 23:05:42', 1),
	(4, 'Juan', 'Pérez', '12345678', '3482156789', 'juan.perez@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(5, 'María', 'Gómez', '23456789', '3482345670', 'maria.gomez@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(6, 'Luis', 'Rodríguez', '34567890', '3482765431', 'luis.rodriguez@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(7, 'Ana', 'Martínez', '45678901', '3482987654', 'ana.martinez@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(8, 'Carlos', 'Hernández', '56789012', '3482543210', 'carlos.hernandez@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(9, 'Laura', 'López', '67890123', '3482012345', 'laura.lopez@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(10, 'Pedro', 'González', '78901234', '3482765432', 'pedro.gonzalez@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(11, 'Lucía', 'Fernández', '89012345', '3482987651', 'lucia.fernandez@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(12, 'José', 'Jiménez', '90123456', '3482109876', 'jose.jimenez@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(13, 'Sofía', 'Vázquez', '12345679', '3482547890', 'sofia.vazquez@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(14, 'Javier', 'Moreno', '23456780', '3482765438', 'javier.moreno@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(15, 'Clara', 'Salazar', '34567891', '3482456789', 'clara.salazar@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(16, 'Fernando', 'Castillo', '45678902', '3482034567', 'fernando.castillo@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(17, 'Isabel', 'Cabrera', '56789013', '3482178901', 'isabel.cabrera@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(18, 'Diego', 'Mendoza', '67890124', '3482547891', 'diego.mendoza@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(19, 'Valeria', 'Rojas', '78901235', '3482912345', 'valeria.rojas@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(20, 'Alberto', 'Vega', '89012346', '3482754890', 'alberto.vega@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(21, 'Marta', 'Santos', '90123467', '3482345612', 'marta.santos@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(22, 'Andrés', 'Bravo', '12345680', '3482012348', 'andres.bravo@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(23, 'Natalia', 'Pérez', '23456781', '3482965432', 'natalia.perez@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(24, 'Gabriel', 'Morales', '34567892', '3482345678', 'gabriel.morales@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(25, 'Carla', 'Márquez', '45678903', '3482109874', 'carla.marquz@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(26, 'Ernesto', 'Riviera', '56789014', '3482512345', 'ernesto.riviera@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(27, 'Patricia', 'Cortez', '67890125', '3482754932', 'patricia.cortez@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(28, 'Hugo', 'Serrano', '78901236', '3482912340', 'hugo.serrano@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(29, 'Mónica', 'Quintero', '89012347', '3482765430', 'monica.quintero@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(30, 'Ricardo', 'Alvarez', '90123468', '3482109875', 'ricardo.alvarez@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(31, 'Cecilia', 'Paz', '12345681', '3482543211', 'cecilia.paz@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(32, 'Nicolás', 'Aguirre', '23456782', '3482987652', 'nicolas.aguirre@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(33, 'Mariana', 'Tello', '34567893', '3482012345', 'mariana.tello@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(34, 'Victor', 'Salas', '45678904', '3482765433', 'victor.salas@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(35, 'Angela', 'Moya', '56789015', '3482456780', 'angela.moya@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(36, 'Pablo', 'Villar', '67890126', '3482034560', 'pablo.villar@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(37, 'Luisa', 'Arrieta', '78901237', '3482178903', 'luisa.arrieta@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(38, 'Jorge', 'Salinas', '89012348', '3482547892', 'jorge.salinas@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(39, 'Estefanía', 'López', '90123469', '3482912348', 'estefania.lopez@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(40, 'Fernando', 'Ruiz', '12345682', '3482765434', 'fernando.ruiz@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(41, 'Ana', 'Salas', '23456783', '3482543212', 'ana.salas@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(42, 'Cristian', 'Ponce', '34567894', '3482987653', 'cristian.ponce@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(43, 'Juliana', 'Núñez', '45678905', '3482012347', 'juliana.nunez@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(44, 'Benjamín', 'Cano', '56789016', '3482765435', 'benjamin.cano@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(45, 'Marisol', 'García', '67890127', '3482456784', 'marisol.garcia@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(46, 'Andrés', 'Bravo', '78901238', '3482034561', 'andres.bravo@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(47, 'Natalia', 'González', '89012349', '3482178904', 'natalia.gonzalez@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(48, 'Ricardo', 'Torre', '90123470', '3482547896', 'ricardo.torre@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(49, 'Teresa', 'Marín', '12345683', '3482912343', 'teresa.marin@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(50, 'Héctor', 'Rios', '23456784', '3482765438', 'hector.rios@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(51, 'Joaquín', 'Lara', '34567895', '3482543213', 'joaquin.lara@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(52, 'Claudia', 'Rivas', '45678906', '3482987654', 'claudia.rivas@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(53, 'María', 'Vargas', '56789017', '3482012345', 'maria.vargas@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(54, 'Lucía', 'Córdova', '67890128', '3482765431', 'lucia.cordova@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(55, 'Alejandro', 'Moreno', '78901239', '3482456787', 'alejandro.moreno@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(56, 'Gloria', 'Cruz', '89012350', '3482034562', 'gloria.cruz@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(57, 'Santiago', 'Castillo', '90123471', '3482178903', 'santiago.castillo@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(58, 'Fernando', 'Gómez', '12345684', '3482547895', 'fernando.gomez@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1),
	(59, 'Claudia', 'Sánchez', '23456785', '3482912344', 'claudia.sanchez@example.com', '2024-11-04 04:33:56', '2024-11-04 04:33:56', 1);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
