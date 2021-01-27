from django.db import *
from fb_post.models import *
from fb_post.utils import *
from django.db.models import *
from fb_post.exceptions import *
from freezegun import freeze_time
from freezegun import freeze_time
import pytest
import datetime
import itertools


#------database fixtures-----
@pytest.fixture
@freeze_time("2020-04-08 14:55:35.459086")
def users_data():
    users = User.objects.bulk_create([
        User(name = 'Mahesh', profile_pic = 'mahesh.com'),
        User(name = 'Ravi', profile_pic = 'ravi.com'),
        User(name = 'Naveen', profile_pic = 'naveen.com'),
        User(name = 'varun', profile_pic = 'varun.com'),
        User(name = 'pavan', profile_pic = 'pavan.com'),
        User(name = 'Prabhas', profile_pic = 'prabhas.com')
        ])
    return users
    
@pytest.fixture
@freeze_time("2020-04-08 14:55:35.459086")
def posts_data():
    posts = Post.objects.bulk_create([
        Post(content = 'Mahesh FIrst',posted_at = datetime.datetime.now(), posted_by_id= 1),
        Post(content = 'Mahesh Second',posted_at = datetime.datetime.now(), posted_by_id = 1),
        Post(content = 'Ravi FIrst',posted_at = datetime.datetime.now(), posted_by_id = 2),
        Post(content = 'Ravi Second',posted_at = datetime.datetime.now(), posted_by_id = 2),
        Post(content = 'Naveen FIrst',posted_at = datetime.datetime.now(), posted_by_id = 3),
        Post(content = 'Naveen Second',posted_at = datetime.datetime.now(), posted_by_id = 3)
        ])
    return posts

@pytest.fixture
@freeze_time("2020-04-08 14:55:35.459086")
def comments_data():
    comments = Comment.objects.bulk_create([
        Comment(content = 'comment to post 1', commented_at = datetime.datetime.now(), 
                    commented_by_id = 2 , post_id = 1),
        Comment(content = 'comment to post 2', commented_at = datetime.datetime.now(), 
                    commented_by_id = 1 , post_id = 2),
        Comment(content = 'comment to post 3', commented_at = datetime.datetime.now(), 
                    commented_by_id = 4 , post_id = 3),
        Comment(content = 'comment to post 4', commented_at = datetime.datetime.now(), 
                    commented_by_id = 3 , post_id = 4),
        Comment(content = 'No replies for this comment', commented_at = datetime.datetime.now(),  
                    commented_by_id = 3 , post_id = 5),
        Comment(content = 'comment to comment 2', commented_at = datetime.datetime.now(), 
                    commented_by_id = 2 , post_id = 2, parent_comment_id = 2),
        Comment(content = 'comment to comment 1', commented_at = datetime.datetime.now(), 
                    commented_by_id = 1 , post_id = 1, parent_comment_id = 1),
        
        Comment(content = 'comment to comment 3', commented_at = datetime.datetime.now(), 
                    commented_by_id = 3 , post_id = 3, parent_comment_id = 3),
        Comment(content = 'comment to comment 4', commented_at = datetime.datetime.now(), 
                    commented_by_id = 4 , post_id = 4, parent_comment_id = 4)
        ])
    return comments
    
@pytest.fixture
@freeze_time("2020-04-08 14:55:35.459086")
def reactions_data():
    reactions = Reaction.objects.bulk_create([
        Reaction(post_id = 1 , reaction = 'HAHA', reacted_at = datetime.datetime.now(), reacted_by_id = 1),
        Reaction(post_id = 1 , reaction = 'LIKE', reacted_at = datetime.datetime.now(), reacted_by_id = 2),
        Reaction(post_id = 1 , reaction = 'ANGRY', reacted_at = datetime.datetime.now(), reacted_by_id = 3),
        Reaction(post_id = 1 , reaction = 'THUMBS-UP', reacted_at = datetime.datetime.now(), reacted_by_id = 4),
        Reaction(post_id = 1 , reaction = 'LOVE', reacted_at = datetime.datetime.now(), reacted_by_id = 5),
        Reaction(post_id = 2 , reaction = 'HAHA', reacted_at = datetime.datetime.now(), reacted_by_id = 1),
        Reaction(post_id = 2 , reaction = 'SAD', reacted_at = datetime.datetime.now(), reacted_by_id = 2),
        Reaction(post_id = 2 , reaction = 'ANGRY', reacted_at = datetime.datetime.now(), reacted_by_id = 3),
        Reaction(post_id = 2 , reaction = 'THUMBS-UP', reacted_at = datetime.datetime.now(), reacted_by_id = 4),
        Reaction(post_id = 2 , reaction = 'LOVE', reacted_at = datetime.datetime.now(), reacted_by_id = 5),
        Reaction(post_id = 3 , reaction = 'HAHA', reacted_at = datetime.datetime.now(), reacted_by_id = 1),
        Reaction(post_id = 3 , reaction = 'SAD', reacted_at = datetime.datetime.now(), reacted_by_id = 2),
        Reaction(post_id = 3 , reaction = 'ANGRY', reacted_at = datetime.datetime.now(), reacted_by_id = 3),
        Reaction(post_id = 3 , reaction = 'THUMBS-UP', reacted_at = datetime.datetime.now(), reacted_by_id = 4),
        Reaction(post_id = 3 , reaction = 'LOVE', reacted_at = datetime.datetime.now(), reacted_by_id = 5),
        
        Reaction(comment_id = 1 , reaction = 'HAHA', reacted_at = datetime.datetime.now(), reacted_by_id = 1),
        Reaction(comment_id = 1 , reaction = 'SAD', reacted_at = datetime.datetime.now(), reacted_by_id = 2),
        Reaction(comment_id = 1 , reaction = 'ANGRY', reacted_at = datetime.datetime.now(), reacted_by_id = 3),
        Reaction(comment_id = 1 , reaction = 'THUMBS-UP', reacted_at = datetime.datetime.now(), reacted_by_id = 4),
        Reaction(comment_id = 2 , reaction = 'HAHA', reacted_at = datetime.datetime.now(), reacted_by_id = 1),
        Reaction(comment_id = 2 , reaction = 'SAD', reacted_at = datetime.datetime.now(), reacted_by_id = 2),
        Reaction(comment_id = 2 , reaction = 'ANGRY', reacted_at = datetime.datetime.now(), reacted_by_id = 3),
        Reaction(comment_id = 2 , reaction = 'THUMBS-UP', reacted_at = datetime.datetime.now(), reacted_by_id = 4),
        Reaction(comment_id = 3 , reaction = 'HAHA', reacted_at = datetime.datetime.now(), reacted_by_id = 1),
        Reaction(comment_id = 3 , reaction = 'SAD', reacted_at = datetime.datetime.now(), reacted_by_id = 2),
        Reaction(comment_id = 3 , reaction = 'ANGRY', reacted_at = datetime.datetime.now(), reacted_by_id = 3),
        Reaction(comment_id = 3 , reaction = 'THUMBS-UP', reacted_at = datetime.datetime.now(), reacted_by_id = 4)
        ])
    return reactions

@pytest.fixture
def user() :
    user = User.objects.create(name = "Mahesh", profile_pic = "mahesh@profile.com")
    return user

@pytest.fixture
def user2() :
    user2 = User.objects.create(name = "you", profile_pic = "you@profile.com")
    return user2
    
@pytest.fixture
def post():
    post = Post.objects.create(content = 'Mahesh FIrst',posted_at = datetime.datetime.now(), posted_by_id= 1)
    return post

@pytest.fixture
def comment():
    comment = Comment.objects.create(content = 'comment to post 1', commented_at = datetime.datetime.now(), 
                    commented_by_id = 2 , post_id = 1)
    return comment
