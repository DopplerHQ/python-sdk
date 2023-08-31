from enum import Enum


class Format(Enum):
    JSON = "json"
    DOTNET_JSON = "dotnet-json"
    ENV = "env"
    YAML = "yaml"
    DOCKER = "docker"
    ENV_NO_QUOTES = "env-no-quotes"

    def list():
        return list(map(lambda x: x.value, Format._member_map_.values()))
