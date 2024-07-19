# make the interactive namespace easier to use
# for `from geopandas import *` demos.

from . import _version

__version__ = _version.get_versions()["version"]
