from typing import Dict


class ConfigSource:
    DEFAULT_ID = None

    def __init__(self, id: str):
        self.id = id

    def get(self, key: str, options: Dict):
        raise NotImplemented

    def exists(self, key: str, options: Dict) -> bool:
        return self.get(key, options) is not None
