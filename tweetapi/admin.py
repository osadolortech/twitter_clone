from django.contrib import admin
from .models import Tweet_Model, ProfileModel,CommentModels,LikeModel,RetweetModel

# Register your models here.

admin.site.register(Tweet_Model)