import pytest
from fb_post.utils import get_posts_with_more_positive_reactions


# ------- Task10 get post with more positive reactions--------
@pytest.mark.django_db
def test_get_post_with_more_positive_reactions_returns_post_ids(
        users_data, posts_data, comments_data, reactions_data):
    # Arrange
    list_of_posts = [1, 2, 3]

    # Act
    post_id_with_positive_reactions = get_posts_with_more_positive_reactions()

    # Assert
    assert post_id_with_positive_reactions == list_of_posts
