from fastapi import status, APIRouter

from app.post import schemas
from app.post.services import post as post_service

router = APIRouter()


# Get All Posts
@router.get(
    path='/',
    status_code=status.HTTP_200_OK
)
def get_posts(limit: int = 10):
    posts = post_service.get_posts(limit)
    return posts


# Create Post
@router.post(
    path='/',
    status_code=status.HTTP_201_CREATED
)
def create_post(post: schemas.CreatePostRequest):
    new_post = post_service.create_post(post)
    return new_post


# Get Post By id
@router.get(
    path="/{id}",
    status_code=status.HTTP_200_OK
)
def get_post_by_id(id: str):
    return post_service.find_post_by_id(id)


# Update Post
@router.patch(
    path='/{id}',
    status_code=status.HTTP_200_OK
)
def update_post(id: str, body: schemas.UpdatePostRequest):
    return post_service.update_post(id, body)


# Delete Post
@router.delete(
    path='/{id}',
    status_code=status.HTTP_200_OK
)
def delete_post(id: str):
    post_service.delete_post(id)
    return {"message": f"Post with id: {id} deleted!"}
