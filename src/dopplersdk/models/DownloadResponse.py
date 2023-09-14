from .base import BaseModel


class DownloadResponse(BaseModel):
    def __init__(
        self,
        STRIPE: str = None,
        ALGOLIA: str = None,
        DATABASE: str = None,
        USER: str = None,
        **kwargs,
    ):
        """
        Initialize DownloadResponse
        Parameters:
        ----------
            STRIPE: str
            ALGOLIA: str
            DATABASE: str
            USER: str
        """
        self.STRIPE = STRIPE
        self.ALGOLIA = ALGOLIA
        self.DATABASE = DATABASE
        self.USER = USER
