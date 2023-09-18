from .base import BaseModel


class WorkplaceUpdateRequest(BaseModel):
    def __init__(
        self,
        name: str = None,
        billing_email: str = None,
        security_email: str = None,
        **kwargs,
    ):
        """
        Initialize WorkplaceUpdateRequest
        Parameters:
        ----------
            name: str
                Workplace name
            billing_email: str
            security_email: str
        """
        self.name = name
        self.billing_email = billing_email
        self.security_email = security_email
