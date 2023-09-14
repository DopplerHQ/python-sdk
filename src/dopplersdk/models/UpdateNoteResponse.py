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
        self.secret = secret
        self.note = note
