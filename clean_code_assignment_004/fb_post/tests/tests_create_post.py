import pytest
from freezegun import freeze_time
from fb_post.models import Post
from fb_post.utils import create_post
from fb_post.exceptions import (
    InvalidPostContent,
    InvalidUserException
    )
# ------create post------
@pytest.mark.django_db
def test_create_post_with_invalid_user_returns_exception():
    # Arrange
    user_id = 1
    post_content = "My first post"

    # Act
    with pytest.raises(InvalidUserException):
        assert create_post(
            user_id=user_id, post_content=post_content)  # Assert


@pytest.mark.django_db
def test_create_post_with_empty_content_returns_exception(user):
    # Arrange
    user_id = user.id
    post_content = ""

    # Act
    with pytest.raises(InvalidPostContent):
        assert create_post(user_id, post_content)  # Assert


@pytest.mark.django_db
@freeze_time("2020-04-08 14:55:35.453090+00:00")
def test_create_post_returns_post_id(user):
    # Arrange
    user_id = user.id
    post_content = "My first post"
    posted_at = "2020-04-08 14:55:35.453090+00:00"

    # Act
    post_id = create_post(user_id=user_id, post_content=post_content)

    # Assert
    post = Post.objects.get(id=post_id)
    assert post.posted_by_id == user_id
    assert post.content == post_content
    assert str(post.posted_at) == posted_at
