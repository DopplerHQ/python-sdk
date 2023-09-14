from enum import Enum


class Type(Enum):
    WORKPLACE_USER = "workplace_user"
    GROUP = "group"
    INVITE = "invite"
    SERVICE_ACCOUNT = "service_account"

    def list():
        return list(map(lambda x: x.value, Type._member_map_.values()))
