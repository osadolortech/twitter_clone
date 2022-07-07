
from django.db import models
from django.contrib.auth.models import User


class ProfileModel(models.Model):
    first_name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")
    username = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    Bio = models.CharField(max_length=60)
    Location = models.CharField(max_length=30)
    Birth_date = models.DateField(editable=True)

class Tweet_Model(models.Model):
    owner = models.ForeignKey(User, related_name='tweet', on_delete=models.CASCADE)
    content = models.CharField(max_length=168, null=True)
    created_time = models.TimeField(auto_now_add=True)
    # retweet = models.ManyToManyField(User, related_name='retweet')
    # like = models.ManyToManyField(User,related_name='like')

    def __str__(self):
        return self.content

    @property
    def number_of_comment(self):
        return CommentModels.objects.filter(tweet=self).count()

    @property
    def number_of_likes(self):
        return LikeModel.objects.filter(tweet=self).count()
    
    @property
    def number_of_retweets(self):
        return RetweetModel.objects.filter(tweet=self).count()

    
    

class CommentModels(models.Model):
    created_time =models.TimeField(auto_now_add=True)
    tweet = models.ForeignKey(Tweet_Model,related_name='comment',on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=168)
    owner = models.ForeignKey(User, related_name='comment',on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class LikeModel(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name='like')
    tweet = models.ForeignKey('Tweet_Model',on_delete=models.CASCADE, related_name='like')
    created_time= models.DateTimeField(auto_now_add=True)

class RetweetModel(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name='retweet')
    tweet = models.ForeignKey(Tweet_Model,on_delete=models.CASCADE, related_name='retweet')
    created_time= models.DateField(auto_now_add=True)
