import os
from typing import Dict

from dotenv import load_dotenv

from schema_config.ConfigSource import ConfigSource


class EnvironmentConfigSource(ConfigSource):
    DEFAULT_ID = 'env'

    def __init__(self, env_path: str = None, id: str = None):
        super().__init__(id or self.DEFAULT_ID)
        if env_path:
            load_dotenv(dotenv_path=env_path, verbose=True, override=False)

    def get(self, key: str, options: Dict):
        return os.getenv(key, None)
