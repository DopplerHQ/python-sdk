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
        if raw is not None:
            self.raw = raw
        if computed is not None:
            self.computed = computed
        if note is not None:
            self.note = note


class SecretsGet200Response(BaseModel):
    def __init__(self, name: str = None, value: Value = None, **kwargs):
        """
        Initialize SecretsGet200Response
        Parameters:
        ----------
            name: str
            value: Value
        """
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
