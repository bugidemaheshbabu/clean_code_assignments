import pytest
from fb_post.utils import react_to_post
from fb_post.exceptions import (
    InvalidUserException,
    InvalidPostException,
    InvalidReactionTypeException)
from fb_post.models import Reaction

#------react to post------
@pytest.mark.django_db
def test_react_to_post_with_invalid_user_returns_exception():
    # Arrange
    user_id = 1
    post_id = 1
    reaction_type = "ANGRY"

    # Act
    with pytest.raises(InvalidUserException):
        assert react_to_post(
            user_id=user_id, post_id=post_id, reaction_type=reaction_type)


@pytest.mark.django_db
def test_react_to_post_with_invalid_post_returns_exception(user):
    # Arrange
    post_id = 1
    reaction_type = "ANGRY"

    # Act
    with pytest.raises(InvalidPostException):
        assert react_to_post(
            user_id=user.id, post_id=post_id, reaction_type=reaction_type)


@pytest.mark.django_db
def test_react_to_post_with_invalid_reaction_type_returns_exception(
        user, user2, post):
    # Arrange
    user_id = 2
    post_id = 1
    reaction_type = "SMILE"

    # Act
    with pytest.raises(InvalidReactionTypeException):
        assert react_to_post(
            user_id=user_id,
            post_id=post_id, reaction_type=reaction_type)


@pytest.mark.django_db
def test_react_to_post_for_the_second_time_with_same_reaction_type_deletes_reaction(
        users_data, posts_data, comments_data, reactions_data):
    # Arrange
    user_id = 3
    post_id = 2
    reaction_type = "ANGRY"
    false = False

    # Act
    react_to_post(
        user_id=user_id, post_id=post_id,
        reaction_type=reaction_type)

    # Assert
    assert Reaction.objects.filter(
        reacted_by_id=user_id, post_id=post_id,
        reaction=reaction_type
        ).exists() == false


@pytest.mark.parametrize("reactions_type", ["WOW", "ANGRY"])
@pytest.mark.django_db
def test_react_to_post_for_the_second_time_with_another_reaction_type_updates_reaction(
        users_data, posts_data, comments_data,
        reactions_data, reactions_type):
    # Arrange
    user_id = 1
    post_id = 1
    reaction_type = reactions_type

    # Act
    react_to_post(
        user_id=user_id, post_id=post_id, reaction_type=reaction_type)

    # Assert
    reaction = Reaction.objects.get(
        reacted_by_id=user_id, post_id=post_id,
        reaction=reaction_type)
    assert reaction.reaction == reaction_type
    assert reaction.reacted_by_id == user_id
    assert reaction.post_id == post_id


@pytest.mark.django_db
def test_react_to_post_create_reaction_for_the_post(
        users_data, posts_data):
    # Arrange
    user_id = 4
    post_id = 2
    reaction_type = "HAHA"
    # Act
    react_to_post(user_id, post_id, reaction_type)

    # Assert
    react = Reaction.objects.get(id=1)
    assert react.reaction == reaction_type
    assert react.reacted_by_id == user_id
    assert react.post_id == post_id
