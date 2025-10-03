import os
from dotenv import load_dotenv

import uvicorn


load_dotenv()

port = int(os.getenv("PORT", 8000)) 


if __name__ == "__main__":
    uvicorn.run("src.app:app", host = "0.0.0.0", port = port, reload = True)
    