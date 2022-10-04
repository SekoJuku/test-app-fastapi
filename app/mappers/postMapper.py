from app.post.schemas import Post


def map_dict_to_object(post) -> Post:
    return Post(
        id=str(post["_id"]),
        title=post["title"],
        category=post["category"],
        content=post["content"],
        created_at=post["created_at"] if post["created_at"] else None,
        updated_at=post["updated_at"] if post["updated_at"] else None
    )


def map_object_to_dict(post: Post) -> dict:
    return {
        "id": post.id,
        "title": post.title,
        "category": post.category,
        "content": post.content,
        "created_at": post.created_at,
        "updated_at": post.updated_at
    }
