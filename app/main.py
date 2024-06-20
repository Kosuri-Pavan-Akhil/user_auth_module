from fastapi import FastAPI
from app.routers import auth, roles, users
from app.utils.database import engine
from app.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(roles.router)
app.include_router(users.router)