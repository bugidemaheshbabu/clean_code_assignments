from fb_post.models import Reaction
from .valid_checks import is_valid_post
from .get_post import get_user_dict

# Task12
def get_reactions_to_post(post_id):
    is_valid_post(post_id)

    reactions_queryset = Reaction.objects.filter(post_id=post_id)

    reactions_to_post_list = []
    for reaction in reactions_queryset:
        reaction_dict = get_user_dict(reaction.reacted_by)
        reaction_dict['reaction'] = reaction.reaction
        reactions_to_post_list.append(reaction_dict)

    return reactions_to_post_list
