from .base import BaseModel


class DynamicSecretsRevokeLease200Response(BaseModel):
    def __init__(self, success: bool = None, **kwargs):
        """
        Initialize DynamicSecretsRevokeLease200Response
        Parameters:
        ----------
            success: bool
        """
        if success is not None:
            self.success = success
