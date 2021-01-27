def compare_users_data(expected_user, output_user):
    assert expected_user['user_id'] == output_user['user_id']
    assert expected_user['name'] == output_user['name']
    assert expected_user['profile_pic'] == output_user['profile_pic']


def compare_reactions(expected_output_reactions, output_data_reactions):
    assert (expected_output_reactions['count'] ==
            output_data_reactions['count'])
    assert expected_output_reactions['type'] == output_data_reactions['type']


def compare_comments_and_replies_comments(expected_comment, output_comment):
    assert expected_comment['comment_id'] == output_comment['comment_id']
    assert expected_comment['commented_at'] == output_comment['commented_at']
    assert (expected_comment['comment_content'] ==
            output_comment['comment_content'])

    # comparing reply commented users
    expected_comment_user = expected_comment['commenter']
    output_comment_user = output_comment['commenter']

    compare_users_data(expected_comment_user, output_comment_user)

    # comparing reactions for this comment
    expected_comment_reactions = expected_comment['reactions']
    output_comment_reactions = output_comment['reactions']
    compare_reactions(expected_comment_reactions, output_comment_reactions)


def compare_comments(expected_comment, output_comment):
    assert expected_comment['comment_id'] == output_comment['comment_id']
    assert expected_comment['commented_at'] == output_comment['commented_at']
    assert (expected_comment['comment_content'] ==
            output_comment['comment_content'])
    assert (expected_comment['replies_count'] ==
            output_comment['replies_count'])

    # comparing reply commented users
    expected_comment_user = expected_comment['commenter']
    output_comment_user = output_comment['commenter']

    compare_users_data(expected_comment_user, output_comment_user)

    # comparing reactions for this comment
    expected_comment_reactions = expected_comment['reactions']
    output_comment_reactions = output_comment['reactions']
    compare_reactions(expected_comment_reactions, output_comment_reactions)

    # comparing reply comments for this comment
    expected_comment_replies = expected_comment['replies']
    output_comment_replies = output_comment['replies']

    for expected_reply, output_reply in zip(
            expected_comment_replies, output_comment_replies):
        compare_comments_and_replies_comments(expected_reply, output_reply)


def task13_compare_comments_value_in_get_post(output_data, expected_output):
    # comparing user details
    expected_output_posted_by = expected_output['posted_by']
    output_data_posted_by = output_data['posted_by']
    compare_users_data(expected_output_posted_by, output_data_posted_by)
    # comparing reactions
    expected_output_reactions = expected_output['reactions']
    output_data_reactions = output_data['reactions']
    compare_reactions(expected_output_reactions, output_data_reactions)
    # comparing commments of the post
    expected_output_comments = expected_output['comments']
    output_data_comments = output_data['comments']
    for expected_comment, output_comment in zip(
            expected_output_comments, output_data_comments):
        compare_comments(expected_comment, output_comment)
