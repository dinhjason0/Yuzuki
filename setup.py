import os

DEBUG = os.getenv("DEBUG", False)

if DEBUG:
    from upkeep_files.settings import*
else:
    from upkeep_files.product import*