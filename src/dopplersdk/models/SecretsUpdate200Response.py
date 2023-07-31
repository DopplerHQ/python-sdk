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
        if raw is not None:
            self.raw = raw
        if computed is not None:
            self.computed = computed
        if note is not None:
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
        if raw is not None:
            self.raw = raw
        if computed is not None:
            self.computed = computed
        if note is not None:
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
        if raw is not None:
            self.raw = raw
        if computed is not None:
            self.computed = computed
        if note is not None:
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
        if STRIPE is not None:
            self.STRIPE = STRIPE
        if ALGOLIA is not None:
            self.ALGOLIA = ALGOLIA
        if DATABASE is not None:
            self.DATABASE = DATABASE


class SecretsUpdate200Response(BaseModel):
    def __init__(self, secrets: Secrets = None, **kwargs):
        """
        Initialize SecretsUpdate200Response
        Parameters:
        ----------
            secrets: Secrets
        """
        if secrets is not None:
            self.secrets = secrets
