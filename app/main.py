from fastapi import FastAPI
from app.post.routes.post import router as post_router

app = FastAPI()

app.include_router(post_router, tags=["post"], prefix="/api/post")


@app.get("/")
def health():
    return {"message": "hello"}
