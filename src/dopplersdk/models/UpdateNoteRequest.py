from .base import BaseModel


class UpdateNoteRequest(BaseModel):
    def __init__(
        self, note: str, secret: str, project: str, config: str = None, **kwargs
    ):
        """
        Initialize UpdateNoteRequest
        Parameters:
        ----------
            note: str
                The note you want to set on the secret. This note will be applied to the specified secret in all environments.
            secret: str
                The name of the secret
            project: str
                Unique identifier for the project object.
            config: str
                Deprecated: Config is no longer required as notes have always been set at the project level.
        """
        self.note = note
        self.secret = secret
        self.project = project
        self.config = config
