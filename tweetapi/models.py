
from django.db import models
from django.contrib.auth.models import User


class ProfileModel(models.Model):
    first_name = models.CharField(User,max_length=20)
    last_name = models.CharField(User,max_length=20)
    Bio = models.CharField(max_length=60)
    Location = models.CharField(max_length=30)
    Birth_date = models.DateField(editable=True)

class Tweet_Model(models.Model):
    username = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    tweet_text = models.CharField(max_length=168, null=False)
    created_time = models.TimeField(auto_now_add=True)
    retweet = models.ManyToManyField(User, related_name='retweeted_user')
    like = models.ManyToManyField(User, related_name='like_tweet')
    comment = models.CharField(max_length=168, null=True)

    def __str__(self):
        return self.tweet_text

class CommentModels(models.Model):
    created_time =models.TimeField(auto_now_add=True)
    body = models.CharField(max_length=168)
    owner = models.ForeignKey(User, related_name='comment',on_delete=models.CASCADE)
