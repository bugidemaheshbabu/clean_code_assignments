import pytest
from fb_post.exceptions import InvalidPostException
from fb_post.utils import get_reaction_metrics


# -------Task8 get reaction metrics------------
@pytest.mark.django_db
def test_get_reaction_metrics_of_a_post_with_invalild_post_returns_exception(
        ):
    # Arrange
    post_id = 1

    # Act
    with pytest.raises(InvalidPostException):
        get_reaction_metrics(post_id=post_id)  # Assert


@pytest.mark.django_db
def test_get_reaction_metrics_of_a_post_returns_reaction_type_and_its_count_in_dictionary(
        users_data, posts_data, comments_data, reactions_data):
    # Arrange
    post_id = 2
    expected_metrics = {'ANGRY': 1, 'HAHA': 1, 'LOVE': 1,
                        'SAD': 1, 'THUMBS-UP': 1}

    # Act
    reaction_dictionary = get_reaction_metrics(post_id=post_id)

    # Assert
    assert reaction_dictionary['HAHA'] == expected_metrics['HAHA']
    assert reaction_dictionary['ANGRY'] == expected_metrics['ANGRY']
    assert reaction_dictionary['SAD'] == expected_metrics['SAD']
    assert reaction_dictionary['LOVE'] == expected_metrics['LOVE']
    assert reaction_dictionary['THUMBS-UP'] == expected_metrics['THUMBS-UP']
