from django.db import models
from datetime import datetime
# Create your models here.

class User(models.Model) :
    name = models.CharField(max_length = 100)
    profile_pic = models.CharField(max_length = 100)
    
class Post(models.Model) :
    content = models.CharField(max_length = 1000)
    posted_at = models.DateTimeField(auto_now = True)
    posted_by = models.ForeignKey(User,
        on_delete = models.CASCADE
        )
    
class Comment(models.Model) :
    content = models.CharField(max_length = 1000)
    commented_at = models.DateTimeField(auto_now = True)
    commented_by = models.ForeignKey(User,
        on_delete = models.CASCADE
        )
    post = models.ForeignKey(Post,
        on_delete = models.CASCADE
        )
    parent_comment = models.ForeignKey('self',
        on_delete = models.CASCADE,
        null = True
    )

    
class Reaction(models.Model) :
    post = models.ForeignKey(Post,
        on_delete = models.CASCADE,
        null = True
        )
    comment = models.ForeignKey(Comment,
        on_delete = models.CASCADE,
        null = True
        )
    reaction_choices = [
        ('WOW','WOW'),
        ('LIT','LIT'),
        ('LOVE','LOVE'),
        ('HAHA','HAHA'),
        ('THUMBS-UP','THUMBS-UP'),
        ('ANGRY','ANGRY'),
        ('THUMBS-DOWN','THUMBS-DOWN'),
        ('SAD','SAD')
        ]
    reaction = models.CharField(
        max_length=100,
        choices=reaction_choices
        )
    reacted_at = models.DateTimeField(auto_now = True)
    reacted_by = models.ForeignKey(User,
        on_delete = models.CASCADE
        )


    