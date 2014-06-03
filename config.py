import os
import base64

CSRF_ENABLED = True
SECRET_KEY = str(base64.b64encode(os.urandom(15)))
