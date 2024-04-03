from enum import Enum


class MemberType(Enum):
    WORKPLACE_USER = "workplace_user"

    def list():
        return list(map(lambda x: x.value, MemberType._member_map_.values()))
