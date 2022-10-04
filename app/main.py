from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.post.routes.post import router as post_router


app = FastAPI()
app.include_router(post_router, tags=["post"], prefix="/api/post")


@app.get("/")
def health() -> JSONResponse:
    return JSONResponse(
        jsonable_encoder({"message": "hello"})
    )
