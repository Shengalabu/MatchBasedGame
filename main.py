import sys
import io

import src.app as app

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
app_instance = app.App(None)


