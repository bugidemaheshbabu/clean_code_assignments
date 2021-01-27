from datetime import datetime
from fb_post.models import Reaction
from .valid_checks import (
    is_valid_user,
    is_valid_comment,
    is_valid_reaction_type
)

def undo_or_update_reaction(reaction_obj, reaction_type):
    is_both_reactions_same = reaction_obj.reaction == reaction_type

    if is_both_reactions_same:
        reaction_obj.delete()
    else:
        update_reaction(reaction_obj, reaction_type)

def update_reaction(reaction_obj, reaction_type):
    reaction_obj.reaction = reaction_type
    reaction_obj.reacted_at = datetime.now()
    reaction_obj.save()

# Task6
def react_to_comment(user_id, comment_id, reaction_type):

    is_valid_user(user_id)
    is_valid_comment(comment_id)
    is_valid_reaction_type(reaction_type)

    try:
        reaction_obj = Reaction.objects.get(
            reacted_by_id=user_id,
            comment_id=comment_id
        )

    except Reaction.DoesNotExist:
        Reaction.objects.create(
            comment_id=comment_id,
            reaction=reaction_type,
            reacted_at=datetime.now(),
            reacted_by_id=user_id)
        return

    undo_or_update_reaction(reaction_obj, reaction_type)
