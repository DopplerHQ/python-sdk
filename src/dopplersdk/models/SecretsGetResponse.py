from .base import BaseModel


class Value(BaseModel):
    def __init__(
        self, raw: str = None, computed: str = None, note: str = None, **kwargs
    ):
        """
        Initialize Value
        Parameters:
        ----------
            raw: str
            computed: str
            note: str
        """
        self.raw = raw
        self.computed = computed
        self.note = note


class SecretsGetResponse(BaseModel):
    def __init__(self, name: str = None, value: Value = None, **kwargs):
        """
        Initialize SecretsGetResponse
        Parameters:
        ----------
            name: str
            value: Value
        """
        self.name = name
        self.value = value
