from pathlib import Path

from pydantic import ConfigDict
from pydantic_settings import BaseSettings

ROOT_DIR: Path = Path(__file__).parent
ENV_FILE_PATH: Path = ROOT_DIR / '.env'


class ConfigProject(BaseSettings):
    model_config = ConfigDict(extra='ignore')

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    SETTINGS_FILE: Path = ROOT_DIR / 'all_settings.json'

    def DATABASE_URL_psycopg(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


Const = ConfigProject(_env_file=ENV_FILE_PATH, _env_file_encoding='utf-8')
