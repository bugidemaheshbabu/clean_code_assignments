import operator
from fb_post.exceptions import UserCannotDeletePostException
from .valid_checks import is_valid_user, is_valid_post


# Task9
def delete_post(user_id, post_id):
    is_valid_user(user_id)
    post = is_valid_post(post_id)
    is_post_posted_by_user = not operator.ne(post.posted_by_id, user_id)

    if is_post_posted_by_user:
        post.delete()
    else:
        raise UserCannotDeletePostException
