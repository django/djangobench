import time
t1 = time.time()

# Make sure the models and settings are loaded, then we're done.
# Calling get_models() will make sure settings get loaded.

from django.db import models
models.get_models()

print time.time() - t1