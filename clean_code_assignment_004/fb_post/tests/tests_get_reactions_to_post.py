from datetime import datetime
import pytest
from fb_post.models import Reaction
from fb_post.utils import get_reactions_to_post
from fb_post.exceptions import InvalidPostException


# -------Task12 get reactions to post---------
def task12_get_reactions_to_post_asserts(expected, output):
    assert expected['user_id'] == output['user_id']
    assert expected['name'] == output['name']
    assert expected['profile_pic'] == output['profile_pic']
    assert expected['reaction'] == output['reaction']


@pytest.mark.django_db
def test_get_reactions_to_post(users_data, post):
    # Arrange
    Reaction.objects.bulk_create([
        Reaction(
            post_id=1, reaction='HAHA',
            reacted_at=datetime.now(), reacted_by_id=1),
        Reaction(
            post_id=1, reaction='LIKE',
            reacted_at=datetime.now(), reacted_by_id=2),
        Reaction(
            post_id=1, reaction='ANGRY',
            reacted_at=datetime.now(), reacted_by_id=3)
        ])
    post_id = post.id
    expected_reactions_data = [
        {
            'user_id': 1,
            'name': 'Mahesh',
            'profile_pic': 'mahesh.com',
            'reaction': 'HAHA'
        },
        {
            'user_id': 2,
            'name': 'Ravi',
            'profile_pic': 'ravi.com',
            'reaction': 'LIKE'
        },
        {
            'user_id': 3,
            'name': 'Naveen',
            'profile_pic': 'naveen.com',
            'reaction': 'ANGRY'
        }
        ]

    # Act
    output_reactions_data = get_reactions_to_post(post_id)

    # Assert
    for expected, output in zip(
            expected_reactions_data, output_reactions_data):
        task12_get_reactions_to_post_asserts(expected, output)


@pytest.mark.django_db
def test_get_reactions_to_post_with_invalid_post_returns_exception():
    # Arrange
    post_id = 1

    # Act
    with pytest.raises(InvalidPostException):
        assert get_reactions_to_post(post_id)  # Assert
