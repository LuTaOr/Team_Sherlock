CREATE TABLE `suministros` (
  `suministro_id` int PRIMARY KEY,
  `pieza_id` int,
  `proveedor_id` int,
  `cantidad` int,
  `fecha` timestamp
);

CREATE TABLE `proveedores` (
  `proveedor_id` int PRIMARY KEY,
  `nombre` char,
  `direccion` char,
  `cuidad` char
);

CREATE TABLE `ciudades` (
  `ciudad` char PRIMARY KEY,
  `provincia` char
);

CREATE TABLE `piezas` (
  `pieza_id` int PRIMARY KEY,
  `nombre` char,
  `color_id` int,
  `precio` float,
  `categoria_id` int
);

CREATE TABLE `categorias` (
  `categoria_id` int PRIMARY KEY,
  `nombre` char
);

CREATE TABLE `colores` (
  `color_id` int PRIMARY KEY,
  `color` char
);

ALTER TABLE `suministros` ADD FOREIGN KEY (`proveedor_id`) REFERENCES `proveedores` (`proveedor_id`);

ALTER TABLE `piezas` ADD FOREIGN KEY (`categoria_id`) REFERENCES `categorias` (`categoria_id`);

ALTER TABLE `suministros` ADD FOREIGN KEY (`pieza_id`) REFERENCES `piezas` (`pieza_id`);

ALTER TABLE `proveedores` ADD FOREIGN KEY (`cuidad`) REFERENCES `ciudades` (`ciudad`);

ALTER TABLE `piezas` ADD FOREIGN KEY (`color_id`) REFERENCES `colores` (`color_id`);
