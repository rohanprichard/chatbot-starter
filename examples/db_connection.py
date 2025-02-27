import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from backend.database.db import engine

try:
    with engine.connect() as connection:

        print("Database connection test result: Success!")
except Exception as e:
    print("Error connecting to the database:", e)
