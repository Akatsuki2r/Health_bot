from databases import Database         # For async DB connection
import os                              # To get env variables
from dotenv import load_dotenv         # To load .env file

# Load variables from .env
load_dotenv()

# Gets the DATABASE_URL from the environment
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the Database object like a place holder or something.
database = Database(DATABASE_URL)

