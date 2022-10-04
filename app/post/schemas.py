from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from bson.objectid import ObjectId


class CreatePostRequest(BaseModel):
    title: str
    content: str
    category: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "title": "example",
                "content": "Lorem ipsum",
                "category": "category"
            }
        }


class UpdatePostRequest(BaseModel):
    title: Optional[str]
    content: Optional[str]
    category: Optional[str]
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "title": "example",
                "content": "Lorem ipsum",
                "category": "category"
            }
        }


class Post(BaseModel):
    id: str
    title: str
    content: str
    category: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
