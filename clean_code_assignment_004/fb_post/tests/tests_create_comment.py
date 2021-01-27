import pytest
from fb_post.exceptions import (
    InvalidUserException,
    InvalidCommentContent,
    InvalidPostException)
from fb_post.models import Comment
from fb_post.utils import create_comment


# -----create comments------
@pytest.mark.django_db
def test_create_comment_with_invalid_user_returns_exception():
    # Arrange
    user_id = 2
    post_id = 1
    comment_content = "My first post"

    # Act
    with pytest.raises(InvalidUserException):
        assert create_comment(
            user_id=user_id, post_id=post_id,
            comment_content=comment_content)  # Assert


@pytest.mark.django_db
def test_create_comment_with_invalid_post_returns_exception(user):
    # Arrange
    user_id = user.id
    post_id = 1
    comment_content = "My first post"

    # Act
    with pytest.raises(InvalidPostException):
        assert create_comment(
            user_id=user_id, post_id=post_id,
            comment_content=comment_content)  # Assert


@pytest.mark.django_db
def test_create_comment_with_empty_content_returns_exception(user, post):
    # Arrange
    user_id = user.id
    post_id = post.id
    comment_content = ""

    # Act
    with pytest.raises(InvalidCommentContent):
        assert create_comment(
            user_id=user_id, post_id=post_id,
            comment_content=comment_content)  # Assert


@pytest.mark.django_db
def test_create_comment_returns_comment_id(user, user2, post):
    # Arrange
    user_id = user2.id
    post_id = post.id
    comment_content = "Hi mahesh"

    # Act
    comment_id = create_comment(
        user_id=user_id, post_id=post_id,
        comment_content=comment_content)

    # Assertf
    comment = Comment.objects.get(id=comment_id)
    assert comment.post == post
    assert comment.commented_by == user2
    assert comment.content == comment_content
