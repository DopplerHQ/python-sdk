from .base import BaseModel


class ServiceTokensDeleteRequest(BaseModel):
    def __init__(
        self, config: str, project: str, slug: str = None, token: str = None, **kwargs
    ):
        """
        Initialize ServiceTokensDeleteRequest
        Parameters:
        ----------
            config: str
                Name of the config object.
            project: str
                Unique identifier for the project object.
            slug: str
                The slug of the service token.
            token: str
                The token value.
        """
        self.config = config
        self.project = project
        if slug is not None:
            self.slug = slug
        if token is not None:
            self.token = token
