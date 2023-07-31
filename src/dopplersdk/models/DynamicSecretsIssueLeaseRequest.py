from .base import BaseModel


class DynamicSecretsIssueLeaseRequest(BaseModel):
    def __init__(
        self, ttl_sec: int, dynamic_secret: str, config: str, project: str, **kwargs
    ):
        """
        Initialize DynamicSecretsIssueLeaseRequest
        Parameters:
        ----------
            ttl_sec: int
                The number of seconds until this lease is automatically revoked
            dynamic_secret: str
                The name of the dynamic secret for which to issue this lease
            config: str
                The config where the dynamic secret is located
            project: str
                The project where the dynamic secret is located
        """
        self.ttl_sec = ttl_sec
        self.dynamic_secret = dynamic_secret
        self.config = config
        self.project = project
