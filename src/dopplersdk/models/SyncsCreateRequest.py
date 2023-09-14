from .base import BaseModel
from enum import Enum

"""
Configuration data for the sync
"""
Data = dict


class ImportOption(Enum):
    """
    An option indicating if and how Doppler should attempt to import secrets from the sync destination
    """

    NONE = "none"
    PREFER_DOPPLER = "prefer_doppler"
    PREFER_INTEGRATION = "prefer_integration"

    def list():
        return list(map(lambda x: x.value, ImportOption._member_map_.values()))


class SyncsCreateRequest(BaseModel):
    def __init__(
        self, data: Data, integration: str, import_option: ImportOption = None, **kwargs
    ):
        """
        Initialize SyncsCreateRequest
        Parameters:
        ----------
            data: Data
                Configuration data for the sync
            integration: str
                The integration slug which the sync will use
            import_option: str
                An option indicating if and how Doppler should attempt to import secrets from the sync destination
        """
        self.data = data
        self.integration = integration
        self.import_option = (
            self._enum_matching(import_option, ImportOption.list(), "import_option")
            if import_option
            else None
        )
