from .base import BaseModel


class DeleteRequest(BaseModel):
    def __init__(self, project: str, **kwargs):
        """
        Initialize DeleteRequest
        Parameters:
        ----------
            project: str
                Unique identifier for the project object.
        """
        self.project = project
