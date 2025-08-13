-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 08, 2025 at 12:36 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bd_las_menonas`
--

-- --------------------------------------------------------

--
-- Table structure for table `empleados`
--

CREATE TABLE `empleados` (
  `n_empleado` int(25) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `telefono` varchar(11) NOT NULL,
  `contrasena` varchar(64) NOT NULL,
  `fecha_ingreso` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `empleados`
--

INSERT INTO `empleados` (`n_empleado`, `nombre`, `apellidos`, `telefono`, `contrasena`, `fecha_ingreso`) VALUES
(6, 'IVAN', 'PORRAS', '911', 'a665a45920', '2025-07-25'),
(7, 'MAX', 'ORONA', '6189237889', 'a665a45920', '2025-07-25'),
(9, 'BRYAN', 'ANDIOLA', '6181162020', 'a665a45920', '2025-07-26'),
(10, '', 'INTO', '123456', 'a665a45920', '2025-07-29'),
(11, 'ANDRES', 'RIVERA', '1234567890', 'a665a45920', '2025-07-29'),
(12, 'OTINAPA', 'CAMPILLO', '9999', 'a665a45920', '2025-07-29'),
(13, 'CAMILO', 'LUIS', '61890', '03ac674216', '2025-07-29'),
(14, 'ANDRES', 'LEYVA', '777', 'a665a45920', '2025-07-31'),
(15, 'SOOO', 'SEE', '999', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', '2025-07-31'),
(16, 'SE', 'SA', '000', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', '2025-08-02'),
(17, 'SEBASTIAN', 'LEYVA RIVERA', '6181161701', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', '2025-08-06');

-- --------------------------------------------------------

--
-- Table structure for table `inventario`
--

CREATE TABLE `inventario` (
  `codigo` int(25) NOT NULL,
  `producto` varchar(50) NOT NULL,
  `cantidad` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `inventario`
--

INSERT INTO `inventario` (`codigo`, `producto`, `cantidad`) VALUES
(1, 'papa', 99),
(98, 'carne', 89),
(99, 'pollo', 20),
(100, 'pan', 92);

-- --------------------------------------------------------

--
-- Table structure for table `menu`
--

CREATE TABLE `menu` (
  `n_producto` int(25) NOT NULL,
  `producto` varchar(100) NOT NULL,
  `precio` float(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `menu`
--

INSERT INTO `menu` (`n_producto`, `producto`, `precio`) VALUES
(1, 'sencilla', 76.00),
(2, 'bbq', 78.00),
(3, 'pollo', 85.00),
(4, 'menonita', 96.00),
(5, 'doble', 92.00),
(6, 'mega', 110.00),
(7, 'pierna', 80.00),
(8, 'salchichon', 90.00),
(9, 'op', 50.00),
(10, 'niños', 75.00);

-- --------------------------------------------------------

--
-- Table structure for table `ventas`
--

CREATE TABLE `ventas` (
  `id_venta` int(25) NOT NULL,
  `total` float(10,2) NOT NULL,
  `fecha` date NOT NULL,
  `n_empleado` int(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ventas`
--

INSERT INTO `ventas` (`id_venta`, `total`, `fecha`, `n_empleado`) VALUES
(2, 230.00, '2025-08-04', 16),
(3, 154.00, '2025-08-06', 16),
(4, 76.00, '2025-08-06', 16);

-- --------------------------------------------------------

--
-- Table structure for table `venta_detalle`
--

CREATE TABLE `venta_detalle` (
  `id_detalle` int(25) NOT NULL,
  `id_venta` int(25) NOT NULL,
  `n_producto` int(25) NOT NULL,
  `cantidad` int(10) NOT NULL,
  `subtotal` float(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `venta_detalle`
--

INSERT INTO `venta_detalle` (`id_detalle`, `id_venta`, `n_producto`, `cantidad`, `subtotal`) VALUES
(1, 2, 1, 2, 152.00),
(2, 2, 2, 1, 78.00),
(4, 4, 1, 1, 76.00);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`n_empleado`),
  ADD UNIQUE KEY `telefono` (`telefono`);

--
-- Indexes for table `inventario`
--
ALTER TABLE `inventario`
  ADD PRIMARY KEY (`codigo`);

--
-- Indexes for table `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`n_producto`);

--
-- Indexes for table `ventas`
--
ALTER TABLE `ventas`
  ADD PRIMARY KEY (`id_venta`),
  ADD KEY `n_empleado` (`n_empleado`);

--
-- Indexes for table `venta_detalle`
--
ALTER TABLE `venta_detalle`
  ADD PRIMARY KEY (`id_detalle`),
  ADD KEY `id_venta` (`id_venta`),
  ADD KEY `n_producto` (`n_producto`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `empleados`
--
ALTER TABLE `empleados`
  MODIFY `n_empleado` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `inventario`
--
ALTER TABLE `inventario`
  MODIFY `codigo` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=102;

--
-- AUTO_INCREMENT for table `menu`
--
ALTER TABLE `menu`
  MODIFY `n_producto` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `ventas`
--
ALTER TABLE `ventas`
  MODIFY `id_venta` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `venta_detalle`
--
ALTER TABLE `venta_detalle`
  MODIFY `id_detalle` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `ventas`
--
ALTER TABLE `ventas`
  ADD CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`n_empleado`) REFERENCES `empleados` (`n_empleado`);

--
-- Constraints for table `venta_detalle`
--
ALTER TABLE `venta_detalle`
  ADD CONSTRAINT `venta_detalle_ibfk_1` FOREIGN KEY (`n_producto`) REFERENCES `menu` (`n_producto`),
  ADD CONSTRAINT `venta_detalle_ibfk_2` FOREIGN KEY (`id_venta`) REFERENCES `ventas` (`id_venta`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
