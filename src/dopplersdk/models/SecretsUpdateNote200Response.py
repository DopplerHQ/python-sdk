from .base import BaseModel


class SecretsUpdateNote200Response(BaseModel):
    def __init__(self, secret: str = None, note: str = None, **kwargs):
        """
        Initialize SecretsUpdateNote200Response
        Parameters:
        ----------
            secret: str
            note: str
        """
        if secret is not None:
            self.secret = secret
        if note is not None:
            self.note = note
