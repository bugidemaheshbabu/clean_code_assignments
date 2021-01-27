import pytest
from fb_post.models import Reaction
from fb_post.utils import get_total_reaction_count

# ------Task 7 get total reaction count--------
@pytest.mark.django_db
def test_get_total_reaction_count_returns_count(user, user2, post, comment):
    # Arrange
    Reaction.objects.create(
        post=post, reaction="HAHA", reacted_by=user)
    Reaction.objects.create(
        post=post, reaction="HAHA", reacted_by=user2)
    Reaction.objects.create(
        comment=comment, reaction="ANGRY", reacted_by=user)

    # Act
    count = get_total_reaction_count()

    # Assert
    assert count['count'] == 3


@pytest.mark.django_db
def test_get_total_reaction_count_with_no_reactions_in_database_returns_zero():
    # Arrange

    # Act
    count = get_total_reaction_count()

    # Assert
    assert count['count'] == 0
