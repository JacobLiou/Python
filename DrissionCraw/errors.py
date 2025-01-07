"""

"""

from .functions.settings import Settings as S



class Error(Exception):
    """Base class for all errors."""
    
    def __init__(self, *args, **kwargs):
        self._kwargs = kwargs
        self._args = args if args else [S._lang.get(self.__class__.__name__.upper())]

    def __str__(self):
        return f"{self._args[0]} {self._kwargs}"



