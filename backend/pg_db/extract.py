from .pg_conn import open_pg


def extract_persons():
    with open_pg() as cur:
        cur.execute('SELECT * FROM person;')
        data = cur.fetchall()
        return data
