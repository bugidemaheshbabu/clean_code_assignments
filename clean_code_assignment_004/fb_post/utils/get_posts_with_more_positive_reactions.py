from django.db.models import F, Count, Q
from fb_post.models import Post
from fb_post.constants import ReactionType


#Task10
def get_posts_with_more_positive_reactions():
    positive_reactions = Q(
        reaction__reaction__in=[
            ReactionType.HAHA,
            ReactionType.LIT,
            ReactionType.LOVE,
            ReactionType.THUMBS_UP,
            ReactionType.WOW])

    post_ids_list = list(
        Post.objects
        .values_list('id', flat=True)
        .annotate(
            positive=Count('reaction', filter=positive_reactions),
            negative=Count('reaction', filter=~positive_reactions)
            )
        .filter(positive__gt=F('negative'))
    )

    return post_ids_list
