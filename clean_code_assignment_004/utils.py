import operator
import datetime
from django.db import *
from fb_post.models import *
from django.db.models import *
from fb_post.exceptions import *


def invalid_post_content_error(post_content):
    if not(post_content):
        raise InvalidPostContent


def invalid_user_id_exception_error(user_id):
    if not(User.objects.filter(id=user_id).exists()):
        raise InvalidUserException


def invalid_post_id_exception(post_id):
    if not(Post.objects.filter(id=post_id).exists()):
        raise InvalidPostException


def invalid_comment_content_error(comment_content):
    if not(comment_content):
        raise InvalidCommentContent


def invalid_comment_id_exception(comment_id):
    if not(Comment.objects.filter(id=comment_id).exists()):
        raise InvalidCommentException


def invalid_reply_content_error(reply_content):
    if not(reply_content):
        raise InvalidReplyContent


def invalid_reaction_type_exception(reaction_type):
    reactions = ['WOW', 'LIT', 'LOVE', 'HAHA',
                 'THUMBS-UP', 'THUMBS-DOWN', 'ANGRY', 'SAD']
    if reaction_type not in reactions:
        raise InvalidReactionTypeException


# Task2
def create_post(user_id, post_content):
    invalid_user_id_exception_error(user_id)
    invalid_post_content_error(post_content)

    post = Post.objects.create(
                content=post_content,
                posted_at=datetime.datetime.now(),
                posted_by_id=user_id)
    return post.id


# Task3
def create_comment(user_id, post_id, comment_content):
    invalid_user_id_exception_error(user_id)
    invalid_post_id_exception(post_id)
    invalid_comment_content_error(comment_content)
    comment = Comment.objects.create(
                content=comment_content,
                commented_at=datetime.datetime.now(),
                commented_by_id=user_id,
                post_id=post_id)
    return comment.id


# Task4
def reply_to_comment(user_id, comment_id, reply_content):
    invalid_user_id_exception_error(user_id)
    none = None
    try:
        comment = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        invalid_comment_id_exception(comment_id)
    invalid_reply_content_error(reply_content)

    if comment.parent_comment_id != none:
        comment_id = comment.parent_comment_id
    new_comment = Comment.objects.create(
                content=reply_content,
                commented_at=datetime.datetime.now(),
                commented_by_id=user_id,
                post_id=comment.post_id,
                parent_comment_id=comment_id)
    return new_comment.id


# Task5
def react_to_post(user_id, post_id, reaction_type):
    invalid_user_id_exception_error(user_id)
    invalid_post_id_exception(post_id)
    invalid_reaction_type_exception(reaction_type)
    try:
        r = Reaction.objects.get(
            reacted_by_id=user_id, post_id=post_id)
        if r:
            if r.reaction == reaction_type:
                r.delete()
            else:
                r.reaction = reaction_type
                r.reacted_at = datetime.datetime.now()
                r.save()
    except Reaction.DoesNotExist:
        Reaction.objects.create(
            post_id=post_id,
            reaction=reaction_type,
            reacted_at=datetime.datetime.now(),
            reacted_by_id=user_id)


# Task6
def react_to_comment(user_id, comment_id, reaction_type):
    invalid_user_id_exception_error(user_id)
    invalid_comment_id_exception(comment_id)
    invalid_reaction_type_exception(reaction_type)
    try:
        r = Reaction.objects.get(reacted_by_id=user_id,
                                 comment_id=comment_id)
        if r:
            if r.reaction == reaction_type:
                r.delete()
            else:
                r.reaction = reaction_type
                r.reacted_at = datetime.datetime.now()
                r.save()
    except Reaction.DoesNotExist:
        Reaction.objects.create(
            comment_id=comment_id,
            reaction=reaction_type,
            reacted_at=datetime.datetime.now(),
            reacted_by_id=user_id)


# Task7
def get_total_reaction_count():
    return {'count': Reaction.objects.all().count()}


# Task8
def get_reaction_metrics(post_id):
    invalid_post_id_exception(post_id)
    qs = Reaction.objects.filter(
        post_id=post_id).values_list(
            'reaction').annotate(count=Count('id')).order_by('-count')
    return_dict = {}
    for q in qs:
        return_dict[q[0]] = q[1]
    return return_dict


# Task9
def delete_post(user_id, post_id):
    invalid_user_id_exception_error(user_id)
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise InvalidPostException
    if operator.ne(post.posted_by_id, user_id):
        raise UserCannotDeletePostException
    else:
        post.delete()


# Task10
def get_posts_with_more_positive_reactions():
    positive = Count('reaction', filter=Q(
                    reaction__reaction__in=['HAHA', 'THUMBS-UP',
                                            'LOVE', 'WOW', 'LIT']))
    negative = Count('reaction', filter=Q(
                reaction__reaction__in=['SAD', 'THUMBS-DOWN', 'ANGRY']))
    qs = Post.objects.values_list('id', flat=True).annotate(
        positive=positive, negative=negative).filter(
            positive__gt=F('negative'))
    return list(qs)


# Task11
def get_posts_reacted_by_user(user_id):
    invalid_user_id_exception_error(user_id)
    return list(Reaction.objects.values_list(
            'post_id', flat=True).filter(reacted_by_id=user_id))


# Task12
def get_reactions_to_post(post_id):
    invalid_post_id_exception(post_id)
    qs = Reaction.objects.filter(post_id=post_id)
    return [{
                'user_id': item.reacted_by_id,
                'name': item.reacted_by.name,
                'profile_pic': item.reacted_by.profile_pic,
                'reaction': item.reaction
            } for item in qs]


# Task13 functions
def user_details_posted_by(user):
    return {
        'name': user.name,
        'user_id': user.id,
        'profile_pic': user.profile_pic
    }


def user_details(user):
    return {
        'user_id': user.id,
        'name': user.name,
        'profile_pic': user.profile_pic
    }


def reactions_type(reactions):
    return list(dict.fromkeys([type.reaction for type in reactions]))


def reaction_details(reactions):
    return {
        'count': len(reactions),
        'type': reactions_type(reactions)
    }


def child_comments_details(child_comments, parent_comment_id):
    from datetime import datetime
    return [{
                'comment_id': child.id,
                'commenter': user_details(child.commented_by),
                'commented_at': datetime.strftime(
                    child.commented_at, "%Y-%m-%d %X.%f"),
                'comment_content': child.content,
                'reactions': reaction_details(child.comment_reactions)
            } for child in child_comments if operator.eq(
                child.parent_comment_id, parent_comment_id)]


def no_of_replies(child_comments, parent_comment_id):
    child_comment_ids = [child.parent_comment_id for child in child_comments]
    return child_comment_ids.count(parent_comment_id)


def comments_details(parent_comments, child_comments):
    from datetime import datetime
    list_of_comments = []
    for cmnt in parent_comments:
        temp = {
            'comment_id': cmnt.id,
            'commenter': user_details(cmnt.commented_by),
            'commented_at': datetime.strftime(
                cmnt.commented_at, "%Y-%m-%d %X.%f"),
            'comment_content': cmnt.content,
            'reactions': reaction_details(cmnt.comment_reactions),
            'replies_count': no_of_replies(child_comments, cmnt.id),
            'replies': child_comments_details(child_comments, cmnt.id)
        }
        list_of_comments.append(temp)
    return list_of_comments


def post_details(post):
    from datetime import datetime
    parent_comments = []
    child_comments = []
    none = None
    for comment in post.comments:
        if comment.parent_comment_id == none:
            parent_comments.append(comment)
        else:
            child_comments.append(comment)

    post_details = {
        'post_id': post.id,
        'posted_by': user_details_posted_by(post.posted_by),
        'posted_at': datetime.strftime(
            post.posted_at, "%Y-%m-%d %X.%f"),
        'post_content': post.content,
        'reactions': reaction_details(post.reactions),
        'comments': comments_details(parent_comments, child_comments),
        'comments_count': len(parent_comments)
    }
    return post_details


# Task13
def get_post(post_id):
    from datetime import datetime
    invalid_post_id_exception(post_id)
    qs = Comment.objects.select_related(
        'commented_by').prefetch_related(
            Prefetch('reaction_set', to_attr='comment_reactions'))
    post = Post.objects.filter(id=post_id).select_related(
        'posted_by').prefetch_related(
            Prefetch('reaction_set', to_attr='reactions'),
            Prefetch('comment_set', queryset=qs, to_attr='comments')
        ).first()
    return post_details(post)


# Task14
def get_user_posts(user_id):
    invalid_user_id_exception_error(user_id)
    qs = Comment.objects.select_related(
        'commented_by').prefetch_related(
            Prefetch('reaction_set', to_attr='comment_reactions')
        )
    posts = Post.objects.filter(
        posted_by_id=user_id).select_related(
            'posted_by').prefetch_related(
                Prefetch('reaction_set', to_attr='reactions'),
                Prefetch('comment_set', queryset=qs, to_attr='comments')
            )
    return [post_details(post) for post in posts]


# Task15
def get_replies_for_comment(comment_id):
    from datetime import datetime
    invalid_comment_id_exception(comment_id)
    replies = Comment.objects.filter(
        parent_comment_id=comment_id).select_related('commented_by')
    return [{
            'comment_id': r.id,
            'commenter': user_details(r.commented_by),
            'commented_at': datetime.strftime(
                r.commented_at, "%Y-%m-%d %X.%f"),
            'comment_content': r.content
            } for r in replies]
