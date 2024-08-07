from typing import Dict

from .logger import logger
from .pg_conn import open_pg


def load_person_data(data: Dict[str, str]):
    with open_pg() as cur:
        query = '''
        INSERT INTO person (id, first_name, last_name)
        VALUES (%s, %s, %s)
        ON CONFLICT (id) DO NOTHING;'''
        for person in data:
            cur.execute(query,
                        (person['id'],
                         person['first_name'],
                         person['last_name']))
            if cur.rowcount == 0:
                logger.info(
                    f'[Info] Person with id {person["id"]} already exists.')
