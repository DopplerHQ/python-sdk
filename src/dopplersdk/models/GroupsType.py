from enum import Enum


class GroupsType(Enum):
    WORKPLACE_USER = "workplace_user"

    def list():
        return list(map(lambda x: x.value, GroupsType._member_map_.values()))
