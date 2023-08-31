from .base import BaseModel

Value = dict


class IssueLeaseResponse(BaseModel):
    def __init__(
        self,
        success: bool = None,
        id: str = None,
        expires_at: str = None,
        value: Value = None,
        **kwargs,
    ):
        """
        Initialize IssueLeaseResponse
        Parameters:
        ----------
            success: bool
            id: str
            expires_at: str
            value: Value
        """
        if success is not None:
            self.success = success
        if id is not None:
            self.id = id
        if expires_at is not None:
            self.expires_at = expires_at
        if value is not None:
            self.value = value
