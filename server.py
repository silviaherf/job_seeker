from src import app
import os
import dotenv

dotenv.load_dotenv()

PORT = os.getenv("PORT")

app.run("0.0.0.0",PORT,debug=True)