from datetime import datetime
import pytest
from fb_post.models import Post, User, Reaction
from fb_post.utils import get_posts_reacted_by_user
from fb_post.exceptions import InvalidUserException

# ------Task11 get posts reacted by user------
@pytest.mark.django_db
def test_get_post_reacted_by_user_if_reacted_to_no_post_returns_empty_list(
        user, user2, post):
    # Arrange
    Post.objects.create(posted_by=user2, content="2nd user post")
    list_of_posts_ids = []
    user_id = user.id

    # Act
    list_of_posts_from_function = get_posts_reacted_by_user(user_id=user_id)

    # Assert
    assert list_of_posts_from_function == list_of_posts_ids


@pytest.mark.django_db
def test_get_posts_reacted_by_the_user_with_invalid_user_returns_exception():
    # Arrange
    user_id = 1

    # Act
    with pytest.raises(InvalidUserException):
        assert get_posts_reacted_by_user(user_id)  # Assert


@pytest.mark.django_db
def test_get_posts_reacted_by_user():
    # Arrange
    User.objects.bulk_create([
        User(name='Mahesh', profile_pic='mahesh.com'),
        User(name='Ravi', profile_pic='ravi.com'),
        User(name='Naveen', profile_pic='Naveen.com')
        ])
    Post.objects.bulk_create([
        Post(
            content='Mahesh FIrst',
            posted_at=datetime.now(), posted_by_id=1),
        Post(
            content='Ravi FIrst',
            posted_at=datetime.now(), posted_by_id=2)
        ])
    Reaction.objects.bulk_create([
        Reaction(
            post_id=1, reaction='HAHA',
            reacted_at=datetime.now(), reacted_by_id=3),
        ])
    user_id = 3
    list_of_posts_ids = [1]

    # Act
    list_of_posts_from_function = get_posts_reacted_by_user(user_id=user_id)

    # Assert
    assert list_of_posts_from_function == list_of_posts_ids
