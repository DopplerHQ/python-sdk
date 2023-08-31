from .base import BaseModel


class UpdateNoteResponse(BaseModel):
    def __init__(self, secret: str = None, note: str = None, **kwargs):
        """
        Initialize UpdateNoteResponse
        Parameters:
        ----------
            secret: str
            note: str
        """
        if secret is not None:
            self.secret = secret
        if note is not None:
            self.note = note
