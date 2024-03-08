import psycopg2
from psycopg2 import DatabaseError
import os


def get_connection():
    try:
        return psycopg2.connect(
            host=os.getenv("PGSQL_HOST"),
            user=os.getenv("PGSQL_USER"),
            password=os.getenv("PGSQL_PASSWORD"),
            database=os.getenv("PGSQL_DATABASE"),
        )
    except DatabaseError as db_ex:
        raise db_ex
