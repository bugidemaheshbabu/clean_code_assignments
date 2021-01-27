from fb_post.models import Reaction
from .valid_checks import is_valid_user

#Task11
def get_posts_reacted_by_user(user_id):
    is_valid_user(user_id)

    post_ids_reacted_by_user_list = list(
        Reaction.objects
        .values_list('post_id', flat=True)
        .filter(reacted_by_id=user_id)
        )

    return post_ids_reacted_by_user_list
