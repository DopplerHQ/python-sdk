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
        if slug is not None:
            self.slug = slug
        if name is not None:
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
        if slug is not None:
            self.slug = slug
        if name is not None:
            self.name = name
        if created_at is not None:
            self.created_at = created_at
        if last_seen_at is not None:
            self.last_seen_at = last_seen_at
        if token_preview is not None:
            self.token_preview = token_preview
        if workplace is not None:
            self.workplace = workplace
        if type_ is not None:
            self.type_ = type_
