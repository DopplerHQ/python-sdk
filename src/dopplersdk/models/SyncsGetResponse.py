from .base import BaseModel


class Sync(BaseModel):
    def __init__(
        self,
        slug: str = None,
        integration: str = None,
        project: str = None,
        config: str = None,
        enabled: bool = None,
        lastSyncedAt: str = None,
        **kwargs,
    ):
        """
        Initialize Sync
        Parameters:
        ----------
            slug: str
            integration: str
            project: str
            config: str
            enabled: bool
            lastSyncedAt: str
        """
        self.slug = slug
        self.integration = integration
        self.project = project
        self.config = config
        self.enabled = enabled
        self.lastSyncedAt = lastSyncedAt


class SyncsGetResponse(BaseModel):
    def __init__(self, sync: Sync = None, **kwargs):
        """
        Initialize SyncsGetResponse
        Parameters:
        ----------
            sync: Sync
        """
        self.sync = sync
