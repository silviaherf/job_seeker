from src.app import app
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='src/.env')


PORT = os.getenv("PORT")

app.run("0.0.0.0",PORT,debug=True)