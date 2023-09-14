from .base import BaseModel
from enum import Enum


class Access(Enum):
    """
    Token's capabilities.
    """

    READ = "read"
    READ_WRITE = "read/write"

    def list():
        return list(map(lambda x: x.value, Access._member_map_.values()))


class ServiceTokensCreateRequest(BaseModel):
    def __init__(
        self,
        name: str,
        config: str,
        project: str,
        expire_at: str = None,
        access: Access = None,
        **kwargs,
    ):
        """
        Initialize ServiceTokensCreateRequest
        Parameters:
        ----------
            name: str
                Name of the service token.
            config: str
                Name of the config object.
            project: str
                Unique identifier for the project object.
            expire_at: str
                Unix timestamp of when token should expire.
            access: str
                Token's capabilities.
        """
        self.name = name
        self.config = config
        self.project = project
        self.expire_at = expire_at
        self.access = (
            self._enum_matching(access, Access.list(), "access") if access else None
        )
