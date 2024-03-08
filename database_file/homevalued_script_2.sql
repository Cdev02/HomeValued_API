-- Database: homevalued

--DROP DATABASE IF EXISTS homevalued;
CREATE DATABASE Homevalued
    WITH
    ENCODING = 'UTF8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE public.property (
    id integer NOT NULL,
    barrio text NOT NULL,
    estrato smallint NOT NULL,
    direccion text NOT NULL,
    nivel_propiedad smallint NOT NULL,
    antiguedad smallint NOT NULL,
    area_propiedad double precision NOT NULL,
    numero_habitaciones smallint NOT NULL,
    garage boolean NOT NULL,
    numero_banos smallint NOT NULL,
    numero_pisos smallint NOT NULL,
    tipo_cocina character varying(15) NOT NULL,
    owner integer,
    CONSTRAINT property_antiguedad_check CHECK (((antiguedad >= 0) AND (antiguedad <= 500))),
    CONSTRAINT property_area_propiedad_check CHECK (((area_propiedad >= (0)::double precision) AND (area_propiedad <= (20000)::double precision))),
    CONSTRAINT property_estrato_check CHECK (((estrato >= 1) AND (estrato <= 6))),
    CONSTRAINT property_nivel_propiedad_check CHECK (((nivel_propiedad >= 0) AND (nivel_propiedad <= 100))),
    CONSTRAINT property_numero_banos_check CHECK (((numero_banos >= 0) AND (numero_banos <= 30))),
    CONSTRAINT property_numero_habitaciones_check CHECK (((numero_habitaciones >= 0) AND (numero_habitaciones <= 30))),
    CONSTRAINT property_numero_pisos_check CHECK (((numero_pisos >= 1) AND (numero_pisos <= 30))),
    CONSTRAINT property_tipo_cocina_check CHECK (((tipo_cocina)::text = ANY (ARRAY[('integral'::character varying)::text, ('no-integral'::character varying)::text])))
);


CREATE TABLE public.property_user (
    id integer NOT NULL,
    user_name text,
    user_lastname text,
    age smallint,
    creation_date date,
    job text
);

CREATE TABLE public.prediction (
    id integer NOT NULL,
	property_id integer NOT NULL,
	pred_date date default CURRENT_DATE,
    prop_value double precision
);


ALTER TABLE ONLY public.property
    ADD CONSTRAINT property_pkey PRIMARY KEY (id);
ALTER TABLE ONLY public.property_user
    ADD CONSTRAINT property_user_pkey PRIMARY KEY (id);
ALTER TABLE ONLY public.prediction
    ADD CONSTRAINT prediction_id_pkey PRIMARY KEY (id);
ALTER TABLE ONLY public.property
    ADD CONSTRAINT property_owner_fkey FOREIGN KEY (owner) REFERENCES public.property_user(id);
ALTER TABLE ONLY public.prediction
    ADD CONSTRAINT property_id_fkey FOREIGN KEY (property_id) REFERENCES public.property(id);
	
	
	
	
CREATE OR REPLACE PROCEDURE deletepropertybyid(p_property_id INTEGER)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM property WHERE id = p_property_id;
END
$$;

CREATE OR REPLACE FUNCTION getallproperties(owner_id INTEGER)
RETURNS TABLE(id integer, barrio text, estrato smallint, direccion text, nivel_propiedad smallint, antiguedad smallint, area_propiedad double precision, numero_habitaciones smallint, garage boolean, numero_banos smallint, numero_pisos smallint, tipo_cocina character varying, owner integer)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY SELECT property.id, property.barrio, property.estrato, property.direccion,
                 property.nivel_propiedad, property.antiguedad, property.area_propiedad,
                 property.numero_habitaciones, property.garage, property.numero_banos,
                 property.numero_pisos, property.tipo_cocina, property.owner
                 FROM property
                 WHERE property.owner = owner_id;
END
$$;


CREATE OR REPLACE FUNCTION getpropertiesbybarrio(barrio_name TEXT)
RETURNS TABLE(id integer, barrio text, estrato smallint, direccion text, nivel_propiedad smallint, antiguedad smallint, area_propiedad double precision, numero_habitaciones smallint, garage boolean, numero_banos smallint, numero_pisos smallint, tipo_cocina character varying, owner integer)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY SELECT property.id, property.barrio, property.estrato, property.direccion,
                 property.nivel_propiedad, property.antiguedad, property.area_propiedad,
                 property.numero_habitaciones, property.garage, property.numero_banos,
                 property.numero_pisos, property.tipo_cocina, property.owner
                 FROM property
                 WHERE property.barrio = barrio_name;
END
$$;




CREATE OR REPLACE FUNCTION getpropertiesbybarrioandid(owner_id INTEGER, barrio_name TEXT) 
RETURNS TABLE(id integer, barrio text, estrato smallint, direccion text, nivel_propiedad smallint, antiguedad smallint, area_propiedad double precision, numero_habitaciones smallint, garage boolean, numero_banos smallint, numero_pisos smallint, tipo_cocina character varying, owner integer)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY SELECT property.id, property.barrio, property.estrato, property.direccion,
                 property.nivel_propiedad, property.antiguedad, property.area_propiedad,
                 property.numero_habitaciones, property.garage, property.numero_banos,
                 property.numero_pisos, property.tipo_cocina, property.owner
                 FROM property
                 WHERE property.barrio = barrio_name AND property.owner = owner_id;
END
$$;


CREATE OR REPLACE FUNCTION getpropertybyid(p_property_id INTEGER) 
RETURNS TABLE(id integer, barrio text, estrato smallint, direccion text, nivel_propiedad smallint, antiguedad smallint, area_propiedad double precision, numero_habitaciones smallint, garage boolean, numero_banos smallint, numero_pisos smallint, tipo_cocina character varying, owner integer)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY SELECT property.id, property.barrio, property.estrato, property.direccion,
                 property.nivel_propiedad, property.antiguedad, property.area_propiedad,
                 property.numero_habitaciones, property.garage, property.numero_banos,
                 property.numero_pisos, property.tipo_cocina, property.owner
                 FROM property
                 WHERE property.id = p_property_id;
END
$$;

CREATE OR REPLACE FUNCTION insertnewproperty(p_id integer, p_barrio text, p_estrato smallint, p_direccion text, p_nivel_propiedad smallint, p_antiguedad double precision, p_area_propiedad double precision, p_numero_habitaciones smallint, p_garage boolean, p_numero_banos smallint, p_numero_pisos smallint, p_tipo_cocina text, p_owner integer) RETURNS void
    LANGUAGE plpgsql
    AS $$
BEGIN
    INSERT INTO property (id, barrio, estrato, direccion, nivel_propiedad, antiguedad, area_propiedad,
                          numero_habitaciones, garage, numero_banos, numero_pisos, tipo_cocina, owner)
    VALUES (p_id::INTEGER, p_barrio::TEXT, p_estrato::SMALLINT, p_direccion::TEXT,
            p_nivel_propiedad::SMALLINT, p_antiguedad::FLOAT, p_area_propiedad::FLOAT,
            p_numero_habitaciones::SMALLINT, p_garage::BOOLEAN, p_numero_banos::SMALLINT,
            p_numero_pisos::SMALLINT, p_tipo_cocina::TEXT, p_owner::INTEGER);
END
$$;

CREATE PROCEDURE insertproperty(IN p_id integer, IN p_barrio text, IN p_estrato smallint, IN p_direccion text, IN p_nivel_propiedad smallint, IN p_antiguedad smallint, IN p_area_propiedad double precision, IN p_numero_habitaciones smallint, IN p_garage boolean, IN p_numero_banos smallint, IN p_numero_pisos smallint, IN p_tipo_cocina character varying, IN p_owner integer)
    LANGUAGE plpgsql
    AS $$
BEGIN
    INSERT INTO property (id, barrio, estrato, direccion, nivel_propiedad, antiguedad, area_propiedad,
                          numero_habitaciones, garage, numero_banos, numero_pisos, tipo_cocina, owner)
    VALUES (p_id, p_barrio, p_estrato, p_direccion, p_nivel_propiedad, p_antiguedad, p_area_propiedad,
            p_numero_habitaciones, p_garage, p_numero_banos, p_numero_pisos, p_tipo_cocina, p_owner);
END
$$;

