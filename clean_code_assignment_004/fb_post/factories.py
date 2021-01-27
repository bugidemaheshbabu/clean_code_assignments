import datetime
import factory
import random

from fb_post import models

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    name = factory.Sequence(lambda n: "Agent %03d" % n)
    profile_pic = factory.LazyAttribute(lambda obj: '%s@example.com' % obj.name)


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Post

    content = factory.Sequence(lambda n: "Hello World %02d" % n)
    posted_at = factory.LazyFunction(datetime.datetime.now)
    posted_by = factory.Iterator(models.User.objects.all())


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Comment

    content = factory.Sequence(lambda n: "Hii! Welcome %02d" % n)
    commented_by = factory.Iterator(models.User.objects.all())
    commented_at = factory.LazyFunction(datetime.datetime.now)
    post = factory.Iterator(models.Post.objects.all())


class ReplyCommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Comment

    content = factory.Sequence(lambda n: "Hii! Welcome Reply Comment %02d" % n)
    commented_by = factory.Iterator(models.User.objects.all())
    commented_at = factory.LazyFunction(datetime.datetime.now)
    parent_comment = factory.Iterator(models.Comment.objects.all())
    post = factory.Iterator(models.Post.objects.all())


class PostReactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Reaction

    reacted_by = factory.Iterator(models.User.objects.all())
    post = factory.Iterator(models.Post.objects.all())
    reacted_at = factory.LazyFunction(datetime.datetime.now)
    reaction = "LIKE"


class CommentReactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Reaction

    reacted_by = factory.Iterator(models.User.objects.all())
    comment = factory.Iterator(models.Comment.objects.all())
    reacted_at = factory.LazyFunction(datetime.datetime.now)
    reaction = "LIKE"
