from .base import BaseModel


class RevokeLeaseRequest(BaseModel):
    def __init__(
        self, slug: str, dynamic_secret: str, config: str, project: str, **kwargs
    ):
        """
        Initialize RevokeLeaseRequest
        Parameters:
        ----------
            slug: str
                The slug of the lease to revoke
            dynamic_secret: str
                The name of the dynamic secret from which this lease was issued
            config: str
                The config where the dynamic secret is located
            project: str
                The project where the dynamic secret is located
        """
        self.slug = slug
        self.dynamic_secret = dynamic_secret
        self.config = config
        self.project = project
