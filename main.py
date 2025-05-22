from fastapi import FastAPI
from settings import Settings
from .bootstrap import init_app

settings = Settings()
app = init_app(settings)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)