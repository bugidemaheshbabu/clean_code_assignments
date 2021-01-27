from datetime import datetime
from fb_post.models import Reaction
from .valid_checks import (
    is_valid_user,
    is_valid_post,
    is_valid_reaction_type)
from .react_to_comment import undo_or_update_reaction


def react_to_post(user_id, post_id, reaction_type):
    is_valid_user(user_id)
    is_valid_post(post_id)
    is_valid_reaction_type(reaction_type)

    try:
        reaction = Reaction.objects.get(
            reacted_by_id=user_id, post_id=post_id)
    except Reaction.DoesNotExist:
        Reaction.objects.create(
            post_id=post_id,
            reaction=reaction_type,
            reacted_at=datetime.now(),
            reacted_by_id=user_id)
        return

    undo_or_update_reaction(reaction, reaction_type)
