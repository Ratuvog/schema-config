import os

from schema_config.AppConfig import AppConfig
from schema_config.ConfigSchema import ConfigSchema, ParameterSource
from schema_config.helper import config
from schema_config.sources.ArgvConfigSource import ArgvConfigSource
from schema_config.sources.EnvironmentConfigSource import \
    EnvironmentConfigSource
from schema_config.sources.YamlConfigSource import YamlConfigSource

sources = [
    YamlConfigSource(os.path.join(
        os.path.dirname(__file__),
        'defaults.yml'
    )),
    EnvironmentConfigSource(),
    ArgvConfigSource()
]


class CustomSchema(ConfigSchema):
    A = [
        ParameterSource(YamlConfigSource, 'test.A')
    ]
    B = [
        ParameterSource(YamlConfigSource, 'test.B'),
        ParameterSource(EnvironmentConfigSource, 'PWD')
    ]
    C = [
        ParameterSource(EnvironmentConfigSource, 'PWD')
    ]
    D = [
        ParameterSource(YamlConfigSource, 'test.D'),
        ParameterSource(EnvironmentConfigSource, 'PWD')
    ]
    E = [
        ParameterSource(ArgvConfigSource, 'e')
    ]
    F = [
        ParameterSource(ArgvConfigSource, 'f')
    ]


AppConfig().initialize(CustomSchema(), sources)

print(config(CustomSchema.A))
print(config(CustomSchema.B))
print(config(CustomSchema.C))
print(config(CustomSchema.D))
print(config(CustomSchema.E))
print(config(CustomSchema.F))
