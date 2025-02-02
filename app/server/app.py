from fastapi import FastAPI
from app.server.routes.student import router as StudentRouter
app = FastAPI()

app.include_router(StudentRouter, tags=["Students"], prefix="/students")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
