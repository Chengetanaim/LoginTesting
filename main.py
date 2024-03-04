from fastapi import FastAPI
from app.routers import user, auth
from fastapi.middleware.cors import CORSMiddleware
from app import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Claxon Business Solutions Time Sheets",
    description="This is the official API for Claxon Business Solutions Time Sheets",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI(title="Login Testing", description="Testing Login")


@app.get("/index")
def index():
    return {"message": "Welcome home"}


app.include_router(user.router)
app.include_router(auth.router)
