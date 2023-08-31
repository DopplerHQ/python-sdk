from enum import Enum


class NameTransformer(Enum):
    CAMEL = "camel"
    UPPER_CAMEL = "upper-camel"
    LOWER_SNAKE = "lower-snake"
    TF_VAR = "tf-var"
    DOTNET = "dotnet"
    DOTNET_ENV = "dotnet-env"
    LOWER_KEBAB = "lower-kebab"

    def list():
        return list(map(lambda x: x.value, NameTransformer._member_map_.values()))
