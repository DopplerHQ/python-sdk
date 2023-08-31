from enum import Enum


class Type(Enum):
    WORKPLACE_USER = "workplace_user"

    def list():
        return list(map(lambda x: x.value, Type._member_map_.values()))
