import pytest
from freezegun import freeze_time
from fb_post.exceptions import (
    InvalidPostException
    )
from fb_post.utils import get_post
from .check_post_details import task13_compare_comments_value_in_get_post


@pytest.mark.django_db
def test_get_post_with_valid_post_id_returns_post_details(
        users_data, posts_data, comments_data, reactions_data):
    # Arrange
    post_id = 2
    postt_details = {'post_id': 2,
                     'posted_by': {
                         'name': 'Mahesh',
                         'user_id': 1,
                         'profile_pic': 'mahesh.com'},
                     'posted_at': '2020-04-08 14:55:35.459086',
                     'post_content': 'Mahesh Second',
                     'reactions': {'count': 5,
                                   'type': ['HAHA', 'SAD', 'ANGRY', 'THUMBS-UP', 'LOVE']},
                     'comments': [{'comment_id': 2,
                                   'commenter': {
                                       'user_id': 1,
                                       'name': 'Mahesh',
                                       'profile_pic': 'mahesh.com'},
                                   'commented_at': '2020-04-08 14:55:35.459086',
                                   'comment_content': 'comment to post 2',
                                   'reactions': {'count': 4,
                                                 'type': ['HAHA', 'SAD', 'ANGRY', 'THUMBS-UP']},
                                   'replies_count': 1,
                                   'replies': [{'comment_id': 6,
                                                'commenter': {
                                                    'user_id': 2,
                                                    'name': 'Ravi',
                                                    'profile_pic': 'ravi.com'},
                                                'commented_at': '2020-04-08 14:55:35.459086',
                                                'comment_content': 'comment to comment 2',
                                                'reactions': {'count': 0, 'type': []}}]}],
                     'comments_count': 1}
    expected_output = postt_details
    expected_output_posted_by = expected_output['posted_by']
    expected_output_reactions = expected_output['reactions']
    expected_output_comments = expected_output['comments']

    # Act
    output_data = get_post(post_id)

    # Assert
    assert expected_output['post_content'] == output_data['post_content']
    assert expected_output['posted_at'] == output_data['posted_at']
    assert expected_output['comments_count'] == output_data['comments_count']
    output_data_posted_by = output_data['posted_by']
    assert expected_output_posted_by == output_data_posted_by
    output_data_reactions = output_data['reactions']
    assert expected_output_reactions == output_data_reactions
    output_data_comments = output_data['comments']
    assert expected_output_comments == output_data_comments
    task13_compare_comments_value_in_get_post(output_data, expected_output)


@pytest.mark.django_db
def test_get_post_with_invalid_post_returns_exception():
    # Arrange
    post_id = 1

    # Act
    with pytest.raises(InvalidPostException):
        assert get_post(post_id)

@pytest.mark.django_db
def test_get_post_without_comments_retruns_comments_values_an_empty_list(
        users_data, posts_data, comments_data):
    # Arrange
    post_id = 6
    post6_details = {'post_id': 6,
                     'posted_by': {
                         'name': 'Naveen',
                         'user_id': 3,
                         'profile_pic': 'naveen.com'},
                     'posted_at': '2020-04-08 14:55:35.459086',
                     'post_content': 'Naveen Second',
                     'reactions': {'count': 0, 'type': []},
                     'comments': [],
                     'comments_count': 0}

    # Act
    get_post_without_comments = get_post(post_id)

    # Assert
    assert [i for i in post6_details if i not in get_post_without_comments] == []
    task13_compare_comments_value_in_get_post(get_post_without_comments, post6_details)


@freeze_time("2020-04-08 14:55:35.453203")
@pytest.mark.django_db
def test_get_post_without_replies_to_comment_returns_empty_list_for_replies(
        users_data, posts_data, comments_data, reactions_data):
    # Arrange
    post5_details = {'post_id': 5,
                     'posted_by': {
                         'name': 'Naveen',
                         'user_id': 3,
                         'profile_pic': 'Naveen.com'},
                     'posted_at': '2020-04-08 14:55:35.459086',
                     'post_content': 'Naveen FIrst',
                     'reactions': {'count': 0, 'type': []},
                     'comments': [{'comment_id': 5,
                                   'commenter': {
                                       'user_id': 3,
                                       'name': 'Naveen',
                                       'profile_pic': 'naveen.com'},
                                   'commented_at': '2020-04-08 14:55:35.459086',
                                   'comment_content': 'No replies for this comment',
                                   'reactions': {'count': 0, 'type': []},
                                   'replies_count': 0,
                                   'replies': []}],
                     'comments_count': 1}
    post_id = 5
    post5_comments = post5_details['comments']

    # Act
    get_post_without_comment_replies = get_post(post_id)

    # Assert
    get_post5_comments = get_post_without_comment_replies['comments']

    for comment, get_comment in zip(post5_comments, get_post5_comments):
        assert comment['replies'] == get_comment['replies'] == []


@pytest.mark.django_db
def test_get_post_with_no_reactions_to_post_or_comments_returns_reactions_count_zero_type_empty_list(
        users_data, posts_data, comments_data, reactions_data):
    # Arrange
    post5_details = {'post_id': 5,
                     'posted_by': {
                         'name': 'Naveen',
                         'user_id': 3,
                         'profile_pic': 'naveen.com'},
                     'posted_at': '2020-04-08 14:55:35.459086',
                     'post_content': 'Naveen FIrst',
                     'reactions': {'count': 0, 'type': []},
                     'comments': [{'comment_id': 5,
                                   'commenter': {
                                       'user_id': 3,
                                       'name': 'Naveen',
                                       'profile_pic': 'naveen.com'},
                                   'commented_at': '2020-04-08 14:55:35.459086',
                                   'comment_content': 'No replies for this comment',
                                   'reactions': {'count': 0, 'type': []},
                                   'replies_count': 0,
                                   'replies': []}],
                     'comments_count': 1}
    post_id = 5

    # Act
    get_post_without_comment_replies = get_post(post_id)

    # Assert
    reactions_dict = post5_details['reactions']
    get_reactions_dict = get_post_without_comment_replies['reactions']
    assert reactions_dict['count'] == get_reactions_dict['count'] == 0
    assert reactions_dict['type'] == get_reactions_dict['type'] == []


@pytest.mark.django_db
def test_get_post_check_unique_type_of_reactions_returns_true_if_unique(
        users_data, posts_data, comments_data, reactions_data):
    # Arrange
    post_id = 2
    post2_reactions_type = ['HAHA', 'SAD', 'ANGRY', 'THUMBS-UP', 'LOVE']

    # Act
    get_post2_details = get_post(post_id)

    # Assert
    get_post2_reactions = get_post2_details['reactions']
    get_post2_reactions_type = get_post2_reactions['type']
    assert len(set(get_post2_reactions_type)) == len(get_post2_reactions_type)
    assert get_post2_reactions_type == post2_reactions_type
