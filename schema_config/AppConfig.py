from typing import List, Dict, Any

from schema_config import ConfigSchema
from schema_config.ConfigSource import ConfigSource
from schema_config.singleton import Singleton


class AppConfig(metaclass=Singleton):
    sources: Dict[str, ConfigSource] = {}
    schema: ConfigSchema = None
    cache: Dict[str, Any] = {}

    def get(self, parameter_id: str) -> Any:
        if parameter_id in self.cache:
            return self.cache[parameter_id]

        value = None
        schema_parameter = self.schema.get_parameter(parameter_id)
        for conf in schema_parameter:
            source_id = conf.source_id
            parameter_key = conf.key
            source = self.sources.get(source_id)

            value = source.get(parameter_key, conf.options)
            if value:
                break

        self.cache[parameter_id] = value
        return value

    def initialize(self, schema: ConfigSchema, sources: List[ConfigSource]):
        self.schema = schema
        self.sources = {s.id: s for s in sources}
        empty_values = []

        schema_params = self.schema.get_parameters()
        for key, parameter in schema_params.items():
            assert parameter, f'Sources not defined for parameter {key}'

            value_exists = False
            for conf in parameter:
                source_id = conf.source_id
                assert source_id, f'source_id not defined for parameter {key}'

                source = self.sources.get(source_id)
                assert source, f'Undefined source with id {source_id} for parameter {key}'

                parameter_key = conf.key
                assert parameter_key, f'Parameter key is not defined for parameter {key} from {source_id}'

                value_exists |= source.exists(parameter_key, conf.options)
                if value_exists:
                    break

            if not value_exists:
                empty_values.append(key)

        if empty_values:
            empty_values_str = '\n'.join(empty_values)
            assert False, f'Values is not exists for parameters: \n {empty_values_str}'
