from .base import BaseModel


class Workplace(BaseModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        billing_email: str = None,
        security_email: str = None,
        **kwargs,
    ):
        """
        Initialize Workplace
        Parameters:
        ----------
            id: str
            name: str
            billing_email: str
            security_email: str
        """
        self.id = id
        self.name = name
        self.billing_email = billing_email
        self.security_email = security_email


class WorkplaceUpdateResponse(BaseModel):
    def __init__(self, workplace: Workplace = None, **kwargs):
        """
        Initialize WorkplaceUpdateResponse
        Parameters:
        ----------
            workplace: Workplace
        """
        self.workplace = workplace
