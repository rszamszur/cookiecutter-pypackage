"""{{cookiecutter.project_description}}"""
import logging

from .version import __version__

# initialize logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

__all__ = ("__version__",)
