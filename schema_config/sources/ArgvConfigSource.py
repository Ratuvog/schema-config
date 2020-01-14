import sys
from typing import Dict

from schema_config.ConfigSource import ConfigSource


class ArgvConfigSource(ConfigSource):
    DEFAULT_ID = 'argv'

    def __init__(self, id: str = None):
        super().__init__(id or self.DEFAULT_ID)
        argv = sys.argv[1:]
        self.params = {}
        for arg in argv:
            parts = arg.split('=')
            if len(parts) == 1:
                self.params[parts[0]] = True
            elif len(parts) == 2:
                self.params[parts[0]] = parts[1]

    def get(self, key: str, options: Dict):
        return self.params.get(key, False)
