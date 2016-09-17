drop table cervecerias;
CREATE TABLE cervecerias
(                    
 id integer NOT NULL,
 nombre text,
 calle1 text,
 calle2 text,
 city text,
 state text,
 zipcode text,
 website text,
 descripcion text,
 CONSTRAINT calles_pkey PRIMARY KEY (id)
);