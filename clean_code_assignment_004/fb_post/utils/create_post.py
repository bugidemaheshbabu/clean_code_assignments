from datetime import datetime
from fb_post.models import Post
from .valid_checks import (
    is_valid_user,
    is_post_content_empty
)

# Task2
def create_post(user_id, post_content):
    is_valid_user(user_id)
    is_post_content_empty(post_content)

    created_post = Post.objects.create(
        content=post_content,
        posted_at=datetime.now(),
        posted_by_id=user_id)
    return created_post.id
