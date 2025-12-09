class RMAError(Exception):
    """Base class for all RMA exceptions."""
    pass

class InvalidDraftFormatError(RMAError):
    """Raised when the generator produces malformed output."""
    pass

class DraftRejectedError(RMAError):
    """Raised when a draft is rejected fatally."""
    pass

class MaxIterationsError(RMAError):
    """Raised when the supervisor exceeds the retry limit."""
    pass
