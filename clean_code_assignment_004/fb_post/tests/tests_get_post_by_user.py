import pytest
from fb_post.utils import get_user_posts
from fb_post.exceptions import InvalidUserException
from .check_post_details import task13_compare_comments_value_in_get_post


#------- Task14 get_posts_by_user_id------
@pytest.mark.django_db
def test_get_user_post_returns_posts_details_list(
        users_data, posts_data, comments_data, reactions_data):
    # Arrange
    user_id = 3
    user3_posts = [{'post_id': 5,
                    'posted_by': {'name': 'Naveen', 'user_id': 3, 'profile_pic': 'naveen.com'},
                    'posted_at': '2020-04-08 14:55:35.459086',
                    'post_content': 'Naveen FIrst',
                    'reactions': {'count': 0, 'type': []},
                    'comments': [{'comment_id': 5,
                                  'commenter': {'user_id': 3, 'name': 'Naveen',
                                                'profile_pic': 'naveen.com'},
                                  'commented_at': '2020-04-08 14:55:35.459086',
                                  'comment_content': 'No replies for this comment',
                                  'reactions': {'count': 0, 'type': []},
                                  'replies_count': 0,
                                  'replies': []}],
                    'comments_count': 1},
                   {'post_id': 6,
                    'posted_by': {'name': 'Naveen', 'user_id': 3, 'profile_pic': 'naveen.com'},
                    'posted_at': '2020-04-08 14:55:35.459086',
                    'post_content': 'Naveen Second',
                    'reactions': {'count': 0, 'type': []},
                    'comments': [],
                    'comments_count': 0}]

    # Act
    get_user3_posts = get_user_posts(user_id)

    # Assert
    for post, get_post in zip(user3_posts, get_user3_posts):
        task13_compare_comments_value_in_get_post(get_post, post)


@pytest.mark.django_db
def test_get_user_posts_with_invalid_user_returns_exception():
    # Arrange
    user_id = 1

    # Act
    with pytest.raises(InvalidUserException):
        assert get_user_posts(user_id)


@pytest.mark.django_db
def test_get_user_post_if_user_has_no_post_returns_empty_list(user):
    # Arrange
    user_id = user.id
    user_posts_empty = []

    #Act
    user_posts = get_user_posts(user_id)

    # Assert
    assert user_posts == user_posts_empty
