from os import listdir

import psycopg2
import os
from relational_database.config import FIXTURES_PATH


def init_tables(cur: psycopg2.connect) -> None:
    fixtures_init_path = os.path.join(FIXTURES_PATH, "init")
    fixtures = [os.path.join(fixtures_init_path, f) for f in listdir(fixtures_init_path)]
    for fixture in fixtures:
        with open(fixture, 'r') as f:
            sql = f.read().strip()
            cur.execute(sql)


def drop_tables(cur: psycopg2.connect) -> None:
    tables = ["Employees", "OrderDetails", "Categories", "Customers",
              "Orders", "Products", "Shippers", "Suppliers"]
    for table in tables:
        cur.execute("DROP TABLE {};".format(table.lower()))


def fill_tables(cur: psycopg2.connect) -> None:
    fixtures_init_path = os.path.join(FIXTURES_PATH, "fill")
    fixtures = [os.path.join(fixtures_init_path, f) for f in listdir(fixtures_init_path)]
    for fixture in fixtures:
        with open(fixture, 'r') as f:
            sql = f.read().strip()
            cur.execute(sql)


def clear_tables(cur: psycopg2.connect) -> None:
    tables = ["Employees", "OrderDetails", "Categories", "Customers",
              "Orders", "Products", "Shippers", "Suppliers"]
    for table in tables:
        query = "DELETE FROM {} WHERE TRUE ;".format(table.lower())
        cur.execute(query)
