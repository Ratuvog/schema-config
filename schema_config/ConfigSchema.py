from typing import List, Dict, Union

from schema_config.ConfigSource import ConfigSource


class ParameterSource:
    def __init__(self, source_id: Union[str, type], key: str, options: Dict = None):
        if issubclass(source_id, ConfigSource):
            self.source_id = source_id.DEFAULT_ID
        else:
            self.source_id = source_id
        self.key = key
        self.options = options or {}


class ConfigSchemaBuilder(type):
    def __call__(cls, *args, **kwargs):
        params = {}
        for key, p in cls.__dict__.items():
            if isinstance(p, list):
                setattr(cls, key, key)
                params[key] = p

        setattr(cls, '_parameters', params)
        return super(ConfigSchemaBuilder, cls).__call__(*args, **kwargs)


class ConfigSchema(metaclass=ConfigSchemaBuilder):
    _parameters = None

    @classmethod
    def get_parameters(cls) -> Dict[str, List[ParameterSource]]:
        return cls._parameters

    @classmethod
    def get_parameter(cls, key):
        return cls._parameters.get(key)
