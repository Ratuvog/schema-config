from schema_config.AppConfig import AppConfig


def config(parameter_id):
    return AppConfig().get(parameter_id)
