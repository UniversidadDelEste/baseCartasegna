drop table estilos;
CREATE TABLE estilos
(                    
 idEstilo integer NOT NULL,
 idCategoria integer references categorias (idCategoria),
 nombre text,
 fecha_cambio date,
 CONSTRAINT estilos_pkey PRIMARY KEY (idEstilo)
);

ALTER TABLE estilos ALTER COLUMN fecha_cambio
SET DEFAULT CURRENT_DATE;