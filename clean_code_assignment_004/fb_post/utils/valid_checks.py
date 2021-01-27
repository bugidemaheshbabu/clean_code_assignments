from fb_post.models import (User, Comment, Post)
from fb_post.exceptions import (
    InvalidUserException,
    InvalidPostException,
    InvalidCommentException,
    InvalidPostContent,
    InvalidCommentContent,
    InvalidReplyContent,
    InvalidReactionTypeException
    )
from fb_post.constants import ReactionType


def is_valid_user(user_id):
    user_does_not_exists = not User.objects.filter(id=user_id).exists()
    if user_does_not_exists:
        raise InvalidUserException


def is_valid_post(post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise InvalidPostException
    return post


def is_post_content_empty(post_content):
    empty_post_content = not post_content
    if empty_post_content:
        raise InvalidPostContent


def is_valid_comment(comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        raise InvalidCommentException
    return comment


def is_comment_content_empty(comment_content):
    empty_comment_content = not comment_content
    if empty_comment_content:
        raise InvalidCommentContent


def is_reply_content_empty(reply_content):
    empty_reply_content = not reply_content
    if empty_reply_content:
        raise InvalidReplyContent


def is_valid_reaction_type(reaction_type):
    if reaction_type not in ReactionType:
        raise InvalidReactionTypeException
