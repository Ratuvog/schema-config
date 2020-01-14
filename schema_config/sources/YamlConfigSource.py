import logging
from typing import Dict, Union, List

import staticconf

from schema_config.ConfigSource import ConfigSource


class YamlConfigSource(ConfigSource):
    DEFAULT_ID = 'yaml'

    def __init__(self, file_path: Union[str, List[str]], id: str = None):
        super().__init__(id or self.DEFAULT_ID)
        self.files = [file_path] if isinstance(file_path, str) else file_path
        self.inited = False

    def init(self):
        for file in self.files:
            try:
                staticconf.YamlConfiguration(file)
            except Exception as e:
                logging.warning({'message': f'Can\'t open config file - {file} - {e}'})

    def get(self, key: str, options: Dict):
        if not self.inited:
            self.init()
            self.inited = True

        try:
            return staticconf.read(key)
        except:
            return None