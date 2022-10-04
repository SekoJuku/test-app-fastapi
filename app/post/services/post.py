from datetime import datetime

from bson.objectid import ObjectId
from fastapi import HTTPException, status
from pymongo.collection import ReturnDocument

from app.post import schemas
from app.database import db
from app.mappers.postMapper import map_dict_to_object

post_dao = db["posts"]


def get_posts(limit: int):
    pipeline = [{
        "$match": {}
    }, {
        "$limit": limit
    }]
    result = post_dao.aggregate(pipeline)
    return [map_dict_to_object(post) for post in result]


def create_post(post: schemas.CreatePostRequest):
    post.created_at = datetime.utcnow()
    result = post_dao.insert_one(post.dict())
    return find_post_by_id(result.inserted_id)


def find_post_by_id(id: str):
    result = post_dao.find_one(
        {'_id': ObjectId(id)}
    )
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Post with id: {id} is not found'
        )
    return map_dict_to_object(result)


def update_post(id: str, body: schemas.UpdatePostRequest):
    body.updated_at = datetime.utcnow()
    updated_post = post_dao.find_one_and_update(
        {'_id': ObjectId(id)},
        {'$set': body.dict(exclude_none=True)},
        return_document=ReturnDocument.AFTER
    )
    if not updated_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'No post with this id: {id} found'
        )
    return map_dict_to_object(updated_post)


def delete_post(id: str):
    post = post_dao.find_one_and_delete({'_id': ObjectId(id)})
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'No post with this id: {id} found'
        )
