from .base import BaseModel


class SecretsUpdateNoteRequest(BaseModel):
    def __init__(self, note: str, secret: str, config: str, project: str, **kwargs):
        """
        Initialize SecretsUpdateNoteRequest
        Parameters:
        ----------
            note: str
            secret: str
            config: str
                Name of the config object.
            project: str
                Unique identifier for the project object.
        """
        self.note = note
        self.secret = secret
        self.config = config
        self.project = project
