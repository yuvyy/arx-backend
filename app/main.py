from fastapi import FastAPI
from app.api import user
from app.core.database import init_db

app = FastAPI()
app.include_router(user.router, prefix="/api")

@app.get("/")
def read_root():    
    return {"message": "Hello, World!!"}

@app.on_event("startup")
def startup_event():
    init_db()
    print("Database initialized and ready to use.")