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
        self.success = success
        self.id = id
        self.expires_at = expires_at
        self.value = value
