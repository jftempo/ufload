import cloud
import db
import httpfile

__version__ = '0.7'

# null progress, can be overridden by importers
def _progress(p):
    pass

progress = _progress
