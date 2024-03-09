from db.db import get_connection
from .entities.property import Property
import os


class PropertyModel:
    # get methods
    @classmethod
    def get_all_properties(self, user_id):
        try:
            connection = get_connection()
            properties = []

            with connection.cursor() as cursor:
                cursor.callproc("getallproperties", [user_id])
                result_set = cursor.fetchall()
                print(f"This is result_set {result_set}")
                for row in result_set:
                    prop = Property(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                        row[9],
                        row[10],
                        row[11],
                        row[12],
                    )
                    properties.append(prop.to_JSON())
            connection.close()
            return properties
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_property_by_id(self, property_id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.callproc("getpropertybyid", [property_id])
                row = cursor.fetchone()
                prop = None
                if row != None:
                    prop = Property(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                        row[9],
                        row[10],
                        row[11],
                        row[12],
                    )
                    prop = prop.to_JSON()

            connection.close()
            return prop
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_property_by_barrio(self, user_id, barrio):
        try:
            connection = get_connection()
            properties = []

            with connection.cursor() as cursor:
                if user_id:
                    cursor.callproc("GetPropertiesByBarrioAndId", [
                                    user_id, barrio])
                else:
                    cursor.callproc("GetPropertiesByBarrio", [barrio])
                result_set = cursor.fetchall()
                for row in result_set:
                    prop = Property(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                        row[9],
                        row[10],
                        row[11],
                        row[12],
                    )
                    properties.append(prop.to_JSON())
            connection.close()
            return properties
        except Exception as ex:
            raise Exception(ex)

    # post method
    @classmethod
    def add_property(self, property):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    f"""INSERT INTO {os.getenv('PGSQL_TABLENAME')}(id, barrio, estrato, direccion, nivel_propiedad, antiguedad, area_propiedad, numero_habitaciones, garage, numero_banos, numero_pisos, tipo_cocina, owner) VALUES(%s,%s,%s,%s,%s,%s,
                        %s,%s,%s,%s,%s,%s,%s)""",
                    (
                        property.id,
                        property.barrio,
                        property.estrato,
                        property.direccion,
                        property.nivel_propiedad,
                        property.antiguedad,
                        property.area_propiedad,
                        property.numero_habitaciones,
                        property.garage,
                        property.numero_banos,
                        property.numero_pisos,
                        property.tipo_cocina,
                        property.owner,
                    ),
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)

    # patch method
    @classmethod
    def update_property(self, property):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = f"""UPDATE {os.getenv('PGSQL_TABLENAME')} SET barrio = %s, 
                estrato = %s, direccion = %s, nivel_propiedad = %s, antiguedad = %s,
                area_propiedad = %s, numero_habitaciones = %s, garage = %s, numero_banos = %s,
                numero_pisos = %s, tipo_cocina = %s, owner = %s WHERE {os.getenv('PGSQL_TABLENAME')}.id = %s"""
                cursor.execute(
                    sql,
                    (
                        property.barrio,
                        property.estrato,
                        property.direccion,
                        property.nivel_propiedad,
                        property.antiguedad,
                        property.area_propiedad,
                        property.numero_habitaciones,
                        property.garage,
                        property.numero_banos,
                        property.numero_pisos,
                        property.tipo_cocina,
                        property.owner,
                        property.id,
                    ),
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)

    # delete method
    @classmethod
    def delete_property(self, property):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = f"DELETE FROM {os.getenv('PGSQL_TABLENAME')} WHERE property.id = {property.id}"
                cursor.execute(sql)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)

    # filter by estrato
    @classmethod
    def get_property_by_estrato(self, user_id, estrato):
        try:
            connection = get_connection()
            properties = []
            print("estamos en get property by estrtato")

            with connection.cursor() as cursor:
                if user_id:
                    sql = f"""SELECT id, barrio, estrato, direccion, nivel_propiedad, antiguedad, area_propiedad, numero_habitaciones, garage, numero_banos, numero_pisos, tipo_cocina, owner FROM {os.getenv("PGSQL_TABLENAME")} WHERE {os.getenv("PGSQL_TABLENAME")}.owner = %s AND {os.getenv("PGSQL_TABLENAME")}.estrato = %s"""
                    print(sql)
                    cursor.execute(sql, (user_id, estrato))
                else:
                    sql = f"""SELECT id, barrio, estrato, direccion,
                      nivel_propiedad,
                        antiguedad,
                          area_propiedad,
                            numero_habitaciones,
                              garage, numero_banos,
                                numero_pisos, tipo_cocina,
                                  owner FROM {os.getenv("PGSQL_TABLENAME")} WHERE {os.getenv("PGSQL_TABLENAME")}.estrato = %s"""
                    print(sql)
                    cursor.execute(sql, (estrato))
                result_set = cursor.fetchall()
                for row in result_set:
                    prop = Property(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                        row[9],
                        row[10],
                        row[11],
                        row[12],
                    )
                    properties.append(prop.to_JSON())
            connection.close()
            return properties
        except Exception as ex:
            raise Exception(ex)
