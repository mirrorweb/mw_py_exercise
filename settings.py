import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

LOCAL_HOST = os.getenv("LOCAL_HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")
