from .base import BaseModel


class Stripe(BaseModel):
    def __init__(
        self, raw: str = None, computed: str = None, note: str = None, **kwargs
    ):
        """
        Initialize Stripe
        Parameters:
        ----------
            raw: str
            computed: str
            note: str
        """
        self.raw = raw
        self.computed = computed
        self.note = note


class Algolia(BaseModel):
    def __init__(
        self, raw: str = None, computed: str = None, note: str = None, **kwargs
    ):
        """
        Initialize Algolia
        Parameters:
        ----------
            raw: str
            computed: str
            note: str
        """
        self.raw = raw
        self.computed = computed
        self.note = note


class Database(BaseModel):
    def __init__(
        self, raw: str = None, computed: str = None, note: str = None, **kwargs
    ):
        """
        Initialize Database
        Parameters:
        ----------
            raw: str
            computed: str
            note: str
        """
        self.raw = raw
        self.computed = computed
        self.note = note


class Secrets(BaseModel):
    def __init__(
        self,
        STRIPE: Stripe = None,
        ALGOLIA: Algolia = None,
        DATABASE: Database = None,
        **kwargs,
    ):
        """
        Initialize Secrets
        Parameters:
        ----------
            STRIPE: Stripe
            ALGOLIA: Algolia
            DATABASE: Database
        """
        self.STRIPE = STRIPE
        self.ALGOLIA = ALGOLIA
        self.DATABASE = DATABASE


class SecretsUpdateResponse(BaseModel):
    def __init__(self, secrets: Secrets = None, **kwargs):
        """
        Initialize SecretsUpdateResponse
        Parameters:
        ----------
            secrets: Secrets
        """
        self.secrets = secrets
