from .base import BaseModel


class Secrets(BaseModel):
    """
    Object of secrets you would like to save to the config. Try it with the sample secrets below:
    """

    def __init__(
        self, STRIPE: str, ALGOLIA: str = None, DATABASE: str = None, **kwargs
    ):
        """
        Initialize Secrets
        Parameters:
        ----------
            STRIPE: str
            ALGOLIA: str
            DATABASE: str
        """
        self.STRIPE = STRIPE
        self.ALGOLIA = ALGOLIA
        self.DATABASE = DATABASE


class UpdateRequest(BaseModel):
    def __init__(self, secrets: Secrets, config: str, project: str, **kwargs):
        """
        Initialize UpdateRequest
        Parameters:
        ----------
            secrets: Secrets
                Object of secrets you would like to save to the config. Try it with the sample secrets below:
            config: str
                Name of the config object.
            project: str
                Unique identifier for the project object.
        """
        self.secrets = secrets
        self.config = config
        self.project = project
