from .base import BaseModel


class SecretsDownload200Response(BaseModel):
    def __init__(
        self,
        STRIPE: str = None,
        ALGOLIA: str = None,
        DATABASE: str = None,
        USER: str = None,
        **kwargs,
    ):
        """
        Initialize SecretsDownload200Response
        Parameters:
        ----------
            STRIPE: str
            ALGOLIA: str
            DATABASE: str
            USER: str
        """
        if STRIPE is not None:
            self.STRIPE = STRIPE
        if ALGOLIA is not None:
            self.ALGOLIA = ALGOLIA
        if DATABASE is not None:
            self.DATABASE = DATABASE
        if USER is not None:
            self.USER = USER
