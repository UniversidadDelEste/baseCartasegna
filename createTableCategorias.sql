﻿drop table cervezas;
CREATE TABLE cervezas
(                    
 idCerveza integer NOT NULL,
 nombre text,
 idCerveceria integer  references cervecerias (id),
 idCategoria integer references categorias (idCategoria),
 idEstilo integer references estilos (idEstilo),
 adv integer,
 ibu integer,
 srm integer,
 upc integer,
 descripcion text,
 fecha_cambio date, 
 CONSTRAINT cervezas_pkey PRIMARY KEY (idCerveza)
);

ALTER TABLE cervezas ALTER COLUMN fecha_cambio
SET DEFAULT CURRENT_DATE;
