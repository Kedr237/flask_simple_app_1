from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent
ENV_FILE = BASE_DIR / '.env'


class PgSettings(BaseSettings):
    host: str
    port: str
    name: str
    user: str
    password: str

    class Config:
        env_file = ENV_FILE
        env_prefix = 'db_'
        extra = 'ignore'


pg_settings = PgSettings()
