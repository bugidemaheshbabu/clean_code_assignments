from datetime import datetime
from fb_post.models import Comment
from .valid_checks import (
    is_valid_user,
    is_valid_comment,
    is_reply_content_empty)


# Task4
def reply_to_comment(user_id, comment_id, reply_content):
    is_valid_user(user_id)
    comment = is_valid_comment(comment_id)
    is_reply_content_empty(reply_content)
    none = None

    is_comment_has_parent_comment_id = comment.parent_comment_id != none
    if is_comment_has_parent_comment_id:
        comment_id = comment.parent_comment_id
    reply_comment = Comment.objects.create(
        content=reply_content,
        commented_at=datetime.now(),
        commented_by_id=user_id,
        post_id=comment.post_id,
        parent_comment_id=comment_id)

    return reply_comment.id
