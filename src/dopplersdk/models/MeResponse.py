from .base import BaseModel


class Workplace(BaseModel):
    def __init__(self, slug: str = None, name: str = None, **kwargs):
        """
        Initialize Workplace
        Parameters:
        ----------
            slug: str
            name: str
        """
        self.slug = slug
        self.name = name


class MeResponse(BaseModel):
    def __init__(
        self,
        slug: str = None,
        name: str = None,
        created_at: str = None,
        last_seen_at: str = None,
        token_preview: str = None,
        workplace: Workplace = None,
        type_: str = None,
        **kwargs,
    ):
        """
        Initialize MeResponse
        Parameters:
        ----------
            slug: str
            name: str
            created_at: str
            last_seen_at: str
            token_preview: str
            workplace: Workplace
            type_: str
        """
        self.slug = slug
        self.name = name
        self.created_at = created_at
        self.last_seen_at = last_seen_at
        self.token_preview = token_preview
        self.workplace = workplace
        self.type_ = type_
