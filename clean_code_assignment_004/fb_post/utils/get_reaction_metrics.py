from django.db.models import Count
from fb_post.models import Reaction
from .valid_checks import is_valid_post


# Task8
def get_reaction_metrics(post_id):
    is_valid_post(post_id)

    reaction_metrics_of_the_post = Reaction.objects\
        .filter(post_id=post_id)\
        .values_list('reaction')\
        .annotate(count=Count('id'))\
        .order_by('-count')

    return dict(reaction_metrics_of_the_post)
