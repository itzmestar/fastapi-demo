from fastapi import APIRouter, Request, status, Response, Depends, HTTPException
from pydantic import BaseModel
import uuid
from sqlalchemy.orm import Session
from db.db_connect import get_db
from db.models import User

# In-memory storage for posts
posts_db = {}

router = APIRouter(prefix="/posts")


def verify_token(token: str):
    db = next(get_db())
    user = db.query(User).filter_by(token=token).first()
    if user:
        return user.email
    raise HTTPException(status_code=401, detail="Invalid or missing token")


class PostsRequest(BaseModel):
    text: str


@router.post('/AddPost', tags=["Posts"])
async def add_post(request: PostsRequest, user: str = Depends(verify_token)):
    # Validate payload size
    if request.headers.get('content-length') and int(request.headers['content-length']) > 1024 * 1024:
        raise HTTPException(status_code=413, detail="Payload too large. Limit to 1 MB")

    # Generate a unique post ID
    post_id = str(uuid.uuid4())
    # Save the post in the in-memory storage
    if user in posts_db:
        posts_db[user][post_id] = request.text
    else:
        posts_db[user] = {
            post_id: request.text
        }

    return {"postID": post_id}
