from .base import BaseModel
from enum import Enum


class Type_(Enum):
    WORKPLACE_USER = "workplace_user"

    def list():
        return list(map(lambda x: x.value, Type_._member_map_.values()))


class AddMemberRequest(BaseModel):
    def __init__(self, type_: Type_, slug: str, **kwargs):
        """
        Initialize AddMemberRequest
        Parameters:
        ----------
            type_: str
            slug: str
                The member's slug
        """
        self.type_ = self._enum_matching(type_, Type_.list(), "type_")
        self.slug = slug
