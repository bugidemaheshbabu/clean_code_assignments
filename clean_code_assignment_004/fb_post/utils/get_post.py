import operator
from django.db.models import Prefetch
from fb_post.models import Post, Comment
from fb_post.constants import get_datetime
from .valid_checks import (
    is_valid_post,
    is_valid_user,
    is_valid_comment
    )


# Task13 functions
def get_user_dict(user):
    return {
        'name': user.name,
        'user_id': user.id,
        'profile_pic': user.profile_pic
    }


def get_reactions_count_and_type_dict(reactions):
    return {
        'count': len(reactions),
        'type': get_reactions_type_dict(reactions)
    }


def get_reactions_type_dict(reactions):
    return list(dict.fromkeys([type.reaction for type in reactions]))

def get_comment_dict(comment):
    return {
        'comment_id': comment.id,
        'commenter': get_user_dict(comment.commented_by),
        'commented_at': get_datetime(comment.commented_at),
        'comment_content': comment.content
    }

def get_reply_comments_details_for_a_comment(
        reply_comments_list, comment_parent_id):
    reply_comments_details_list = []
    for reply_comment in reply_comments_list:
        if operator.eq(reply_comment.parent_comment_id, comment_parent_id):
            comment_dict_with_reactions = (
                get_comment_details_dict_with_reactions(reply_comment))
            reply_comments_details_list.append(comment_dict_with_reactions)
    return reply_comments_details_list

def get_comment_details_dict_with_reactions(comment):
    comment_dict_with_reactions = get_comment_dict(comment)
    comment_dict_with_reactions['reactions'] = (
        get_reactions_count_and_type_dict(comment.comment_reactions)
        )
    return comment_dict_with_reactions

def counting_the_reply_comments_for_comment(
        reply_comments, comment_parent_id):
    reply_comment_ids = [
        reply_comment.parent_comment_id for reply_comment in reply_comments]
    return reply_comment_ids.count(comment_parent_id)


def get_comments_details_list(comments_list, reply_comments_list):
    comment_details_list = []
    for comment in comments_list:
        comment_dict = get_comment_dict_with_reactions_replies_count_replies(
            comment, reply_comments_list)
        comment_details_list.append(comment_dict)
    return comment_details_list


def get_comment_dict_with_reactions_replies_count_replies(
        comment, reply_comments_list):
    comment_dict = get_comment_dict(comment)
    comment_dict_update = {
        'reactions': get_reactions_count_and_type_dict(
            comment.comment_reactions),
        'replies_count': counting_the_reply_comments_for_comment(
            reply_comments_list, comment.id),
        'replies': get_reply_comments_details_for_a_comment(
            reply_comments_list, comment.id)
    }
    comment_dict.update(comment_dict_update)
    return comment_dict

def seperating_comment_and_reply_comments(post):
    comments_list = []
    reply_comments_list = []
    for comment in post.comments:
        comments_list, reply_comments_list = (
            get_comment_and_reply_comment_lists(
                comment, comments_list, reply_comments_list))

    return comments_list, reply_comments_list

def get_comment_and_reply_comment_lists(
        comment, comments_list, reply_comments_list):
    none = None
    is_reply_comment = comment.parent_comment_id != none
    if is_reply_comment:
        reply_comments_list.append(comment)
    else:
        comments_list.append(comment)
    return comments_list, reply_comments_list

def post_details(post):
    comments_list, reply_comments_list = (
        seperating_comment_and_reply_comments(post))

    details_of_given_post_dict = {
        'post_id': post.id,
        'posted_by': get_user_dict(post.posted_by),
        'posted_at': get_datetime(post.posted_at),
        'post_content': post.content,
        'reactions': get_reactions_count_and_type_dict(post.reactions),
        'comments': get_comments_details_list(
            comments_list, reply_comments_list),
        'comments_count': len(comments_list)
    }
    return details_of_given_post_dict


# Task13
def get_post(post_id):

    is_valid_post(post_id)

    queryset = Comment.objects\
        .select_related('commented_by')\
        .prefetch_related(
            Prefetch('reaction_set', to_attr='comment_reactions')
        )

    post = Post.objects.filter(id=post_id)\
        .select_related('posted_by')\
        .prefetch_related(
            Prefetch('reaction_set', to_attr='reactions'),
            Prefetch('comment_set', queryset=queryset, to_attr='comments')
        ).first()

    return post_details(post)


# Task14
def get_user_posts(user_id):
    is_valid_user(user_id)
    queryset = Comment.objects\
        .select_related('commented_by')\
        .prefetch_related(
            Prefetch('reaction_set', to_attr='comment_reactions')
        )

    posts = Post.objects\
            .filter(posted_by_id=user_id)\
            .select_related('posted_by')\
            .prefetch_related(
                Prefetch('reaction_set', to_attr='reactions'),
                Prefetch('comment_set', queryset=queryset, to_attr='comments')
            )

    return [post_details(post) for post in posts]


# Task15
def get_replies_for_comment(comment_id):
    is_valid_comment(comment_id)
    reply_comments_list = Comment.objects\
            .filter(parent_comment_id=comment_id)\
            .select_related('commented_by')

    return [get_comment_dict(reply) for reply in reply_comments_list]
