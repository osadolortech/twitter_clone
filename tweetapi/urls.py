from django.urls import path
from .views import ProfileViews,ProfileDetails,Userview,TweetView,TweetDetails,CommentView,UserDetail,LikeTWEET,RetweetView
from .registerview import RegisterUserApi
from .login import Login,Logout,UserloginView
urlpatterns = [
    path('profile',ProfileViews.as_view(), name="profile"),
    path('profile/<int:pk>',ProfileDetails.as_view(),name='profile-details'),
    path('Users', Userview.as_view(),name='user view'),
    path('Users/<int:pk>', UserDetail.as_view(),name='user view'),
    path('tweet', TweetView.as_view()),
    path('register', RegisterUserApi.as_view(), name='Register'),
    path('login', Login.as_view(), name='Login'),
    path('userview', UserloginView.as_view(), name='users_Authemticated'),
    path('logout', Logout.as_view(), name='Logout'),
    path('tweet/<int:pk>', TweetDetails.as_view()),
    path('comment', CommentView.as_view()),
    path('like',LikeTWEET.as_view()),
    path('retweet',RetweetView.as_view())
]
