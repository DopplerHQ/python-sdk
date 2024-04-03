from .base import BaseModel


class Stripe(BaseModel):
    def __init__(
        self,
        raw: str = None,
        computed: str = None,
        note: str = None,
        rawVisibility: str = None,
        computedVisibility: str = None,
        **kwargs,
    ):
        """
        Initialize Stripe
        Parameters:
        ----------
            raw: str
            computed: str
            note: str
            rawVisibility: str
            computedVisibility: str
        """
        self.raw = raw
        self.computed = computed
        self.note = note
        self.rawVisibility = rawVisibility
        self.computedVisibility = computedVisibility


class Algolia(BaseModel):
    def __init__(
        self,
        raw: str = None,
        computed: str = None,
        note: str = None,
        rawVisibility: str = None,
        computedVisibility: str = None,
        **kwargs,
    ):
        """
        Initialize Algolia
        Parameters:
        ----------
            raw: str
            computed: str
            note: str
            rawVisibility: str
            computedVisibility: str
        """
        self.raw = raw
        self.computed = computed
        self.note = note
        self.rawVisibility = rawVisibility
        self.computedVisibility = computedVisibility


class Database(BaseModel):
    def __init__(
        self,
        raw: str = None,
        computed: str = None,
        note: str = None,
        rawVisibility: str = None,
        computedVisibility: str = None,
        **kwargs,
    ):
        """
        Initialize Database
        Parameters:
        ----------
            raw: str
            computed: str
            note: str
            rawVisibility: str
            computedVisibility: str
        """
        self.raw = raw
        self.computed = computed
        self.note = note
        self.rawVisibility = rawVisibility
        self.computedVisibility = computedVisibility


class User(BaseModel):
    def __init__(
        self,
        raw: str = None,
        computed: str = None,
        note: str = None,
        rawVisibility: str = None,
        computedVisibility: str = None,
        **kwargs,
    ):
        """
        Initialize User
        Parameters:
        ----------
            raw: str
            computed: str
            note: str
            rawVisibility: str
            computedVisibility: str
        """
        self.raw = raw
        self.computed = computed
        self.note = note
        self.rawVisibility = rawVisibility
        self.computedVisibility = computedVisibility


class Secrets(BaseModel):
    def __init__(
        self,
        STRIPE: Stripe = None,
        ALGOLIA: Algolia = None,
        DATABASE: Database = None,
        USER: User = None,
        **kwargs,
    ):
        """
        Initialize Secrets
        Parameters:
        ----------
            STRIPE: Stripe
            ALGOLIA: Algolia
            DATABASE: Database
            USER: User
        """
        self.STRIPE = STRIPE
        self.ALGOLIA = ALGOLIA
        self.DATABASE = DATABASE
        self.USER = USER


class SecretsListResponse(BaseModel):
    def __init__(self, secrets: Secrets = None, **kwargs):
        """
        Initialize SecretsListResponse
        Parameters:
        ----------
            secrets: Secrets
        """
        self.secrets = secrets
