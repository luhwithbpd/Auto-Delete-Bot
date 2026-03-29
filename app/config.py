import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
CANAL_PERMITIDO_ID = int(os.getenv("CANAL_PERMITIDO_ID"))