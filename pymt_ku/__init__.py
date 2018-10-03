#! /usr/bin/env python

from .bmi import BmiKuMethod


__all__ = ["BmiKuMethod"]

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
