import pytest
from fb_post.utils import get_replies_for_comment
from fb_post.exceptions import InvalidCommentException


# -----Task15 get replies for comment-------
def task15_comment_and_replies_for_comment_assert(
        comment, replies_for_comment):
    assert comment['comment_id'] == replies_for_comment['comment_id']
    assert (comment['comment_content'] ==
            replies_for_comment['comment_content'])
    assert comment['commented_at'] == replies_for_comment['commented_at']
    replies_for_comment_user = replies_for_comment['commenter']
    comment_user = comment['commenter']
    assert comment_user['user_id'] == replies_for_comment_user['user_id']
    assert comment_user['name'] == replies_for_comment_user['name']
    assert (comment_user['profile_pic'] ==
            replies_for_comment_user['profile_pic'])


def task15_verifying_comments_details(
        comments_data, expected_replies_for_comment):
    for comment, replies_for_comment in zip(
            comments_data, expected_replies_for_comment):
        task15_comment_and_replies_for_comment_assert(
            comment, replies_for_comment)

@pytest.mark.django_db
def test_get_replies_for_comment_returns_dictionary_of_comments_data(
        users_data, posts_data, comments_data):
    # Arrange
    comment_id = 2
    expected_replies_for_comment = [{'comment_id': 6,
                                     'commenter': {
                                         'user_id': 2,
                                         'name': 'Ravi',
                                         'profile_pic': 'ravi.com'},
                                     'commented_at': '2020-04-08 14:55:35.459086',
                                     'comment_content': 'comment to comment 2'}]

    # Act
    comments_data = get_replies_for_comment(comment_id)

    # Assert
    task15_verifying_comments_details(
        comments_data, expected_replies_for_comment)


@pytest.mark.django_db
def test_get_replies_for_comment_with_invalid_comment_id_raises_exception():
    # Arrange
    comment_id = 1

    # Act
    with pytest.raises(InvalidCommentException):
        get_replies_for_comment(comment_id)  # Assert
