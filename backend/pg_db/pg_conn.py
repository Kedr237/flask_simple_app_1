from contextlib import contextmanager
from typing import Generator

import psycopg
from psycopg import ClientCursor
from psycopg.rows import dict_row

from .backoff import backoff
from .logger import logger
from .settings import pg_settings


@backoff()
def create_pg_conn() -> psycopg.Connection:
    try:
        conn = psycopg.connect(
            host=pg_settings.host,
            port=pg_settings.port,
            dbname=pg_settings.name,
            user=pg_settings.user,
            password=pg_settings.password,
            row_factory=dict_row,
        )
        logger.info('[Info] Successfully connected to postgresql')
        return conn
    except Exception as e:
        logger.error(f'[Error] Error connecting to postgresql: {e}')
        raise


@contextmanager
def open_pg() -> Generator[psycopg.Cursor, None, None]:
    conn = create_pg_conn()
    try:
        yield conn.cursor()
    finally:
        conn.commit()
        conn.close()
