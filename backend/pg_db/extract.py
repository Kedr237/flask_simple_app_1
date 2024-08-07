from typing import Dict, List

from .pg_conn import open_pg


def extract_persons() -> List[Dict[str, str]]:
    with open_pg() as cur:
        cur.execute('SELECT * FROM person;')
        data = cur.fetchall()
        return data
