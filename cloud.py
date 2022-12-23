import base64
from utils import *

class CloudTouch(object):
    def cloud(*args):
        try:
            pass
        except Exception:
            pass
    
    def addfile(*args, filename):
        data = open(filename, 'a')
        with open(filename, 'w') as f:
            f.write(str(data))
            f.close()
