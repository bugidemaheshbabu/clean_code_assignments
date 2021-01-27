from datetime import datetime
from fb_post.models import Comment
from .valid_checks import (
    is_valid_user,
    is_valid_post,
    is_comment_content_empty
)


# Task13
def create_comment(user_id, post_id, comment_content):
    is_valid_user(user_id)
    is_valid_post(post_id)
    is_comment_content_empty(comment_content)

    created_comment = Comment.objects.create(
        content=comment_content,
        commented_at=datetime.now(),
        commented_by_id=user_id,
        post_id=post_id
    )
    return created_comment.id
