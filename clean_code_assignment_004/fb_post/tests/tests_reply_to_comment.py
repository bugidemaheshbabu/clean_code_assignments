from datetime import datetime
import pytest
from fb_post.models import Comment, User, Post
from fb_post.utils import reply_to_comment
from fb_post.exceptions import (
    InvalidUserException,
    InvalidCommentException,
    InvalidReplyContent)


# ----reply to comment-----
@pytest.mark.django_db
def test_reply_to_comment_with_invalid_user_returns_exception():
    # Arrange
    user_id = 1
    comment_id = 1
    reply_content = "My first post"

    # Act
    with pytest.raises(InvalidUserException):
        assert reply_to_comment(
            user_id=user_id, comment_id=comment_id,
            reply_content=reply_content)  # Assert


@pytest.mark.django_db
def test_reply_to_comment_with_invalid_comment_id_returns_exception():
    # Arrange
    user_me = User.objects.create(
        name="Mahesh", profile_pic="mahesh@profile.com")
    comment_id = 1
    comment_content = "My FIrst Post"

    # Act
    with pytest.raises(InvalidCommentException):
        assert reply_to_comment(user_me.id, comment_id, comment_content)


@pytest.mark.django_db
def test_reply_to_comment_with_empty_reply_content_returns_exception():
    # Arrange
    user_me = User.objects.create(
        name="Mahesh", profile_pic="mahesh@profile.com")
    User.objects.create(
        name="you", profile_pic="you@profile.com")
    Post.objects.create(
        content='Mahesh FIrst',
        posted_at=datetime.now(), posted_by_id=1)
    comment = Comment.objects.create(
        content='comment to post 1',
        commented_at=datetime.now(),
        commented_by_id=2, post_id=1)
    user_id = user_me.id
    comment_id = comment.id
    content = ""

    # Act
    with pytest.raises(InvalidReplyContent):
        assert reply_to_comment(user_id, comment_id, content)


@pytest.mark.django_db
def test_reply_to_comment_with_parent_comment_id_is_not_none_returns_same_parent_comment_id(
        user, user2, post, comment):
    # Arrange
    reply_comment = Comment.objects.create(
        content='comment to comment 1',
        commented_at=datetime.now(),
        commented_by_id=2, post_id=1, parent_comment_id=1)
    user_id = user.id
    comment_id = reply_comment.id
    reply_content = "reply to reply"
    parent_comment_id = comment.id

    # Act
    new_reply_comment_id = reply_to_comment(
        user_id=user_id, comment_id=comment_id,
        reply_content=reply_content)

    # Assert
    new_reply_comment = Comment.objects.get(id=new_reply_comment_id)
    assert new_reply_comment.parent_comment_id == parent_comment_id
    assert new_reply_comment.content == reply_content


@pytest.mark.django_db
def test_reply_to_comment_returns_parent_comment_id(
        user, user2, post, comment):
    # Arrange
    user_id = 2
    comment_id = 1
    reply_content = "Hi"

    # Act
    reply_comment_id = reply_to_comment(
        user_id=user_id, comment_id=comment_id,
        reply_content=reply_content)

    # Assert
    reply_comment = Comment.objects.get(id=reply_comment_id)
    assert reply_comment.parent_comment_id == comment_id
    assert reply_comment.content == reply_content
