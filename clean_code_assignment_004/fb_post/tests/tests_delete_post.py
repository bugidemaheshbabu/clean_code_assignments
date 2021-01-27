import pytest
from fb_post.exceptions import (
    InvalidUserException,
    UserCannotDeletePostException,
    InvalidPostException
    )
from fb_post.utils import delete_post
from fb_post.models import Post


# ------Task 9 delete post--------
@pytest.mark.django_db
def test_delete_post_with_invalid_user_returns_exception():
    # Arrange
    user_id = 1
    post_id = 1

    # Act
    with pytest.raises(InvalidUserException):
        assert delete_post(user_id=user_id, post_id=post_id)  # Assert


@pytest.mark.django_db
def test_delete_post_with_invalid_post_returns_exception(user):
    # Arrange
    user_id = user.id
    post_id = 1

    # Act
    with pytest.raises(InvalidPostException):
        assert delete_post(user_id=user_id, post_id=post_id)  # Assert


@pytest.mark.parametrize("user", [1, 5])
@pytest.mark.django_db
def test_delete_post_with_another_user_returns_exception(
        users_data, posts_data, user):
    # Arrange
    user_id = user
    post_id = 4

    # Act
    with pytest.raises(UserCannotDeletePostException):
        assert delete_post(user_id=user_id, post_id=post_id)  # Assert


@pytest.mark.django_db
def test_delete_post_with_valid_details_deletes_post(user, post):
    # Arrange
    false = False

    # Act
    delete_post(user_id=user.id, post_id=post.id)

    # Assert
    assert Post.objects.filter(id=post.id).exists() == false
