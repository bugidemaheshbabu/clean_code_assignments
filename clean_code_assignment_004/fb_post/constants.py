from datetime import datetime
from django.db import models

class ReactionType(models.TextChoices):
    WOW = 'WOW'
    HAHA = 'HAHA'
    THUMBS_UP = 'THUMBS-UP'
    LOVE = 'LOVE'
    LIT = 'LIT'
    SAD = 'SAD'
    ANGRY = 'ANGRY'
    THUMBS_DOWN = 'THUMBS_DOWN'


def get_datetime(datetime_value):
    return datetime.strftime(
        datetime_value, "%Y-%m-%d %X.%f")
