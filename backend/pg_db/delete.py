from typing import Dict, List

from .logger import logger
from .pg_conn import open_pg


def delete_person_info(id: str):
    with open_pg() as cur:
        query = 'DELETE FROM person WHERE person.id = %s'
        cur.execute(query, (id,))
        if cur.rowcount == 0:
            logger.info(
                f'[Info] Person with id {id} does not extst.')
        else:
            logger.info(
                f'[Info] Person with id {id} was successfully deleted.')
