from django.urls import path
from .views import ProfileViews,ProfileDetails,Userview

urlpatterns = [
    path('profile',ProfileViews.as_view(), name="profile"),
    path('profile/<int:pk>',ProfileDetails.as_view(),name='profile-details'),
    path('Users', Userview.as_view(),name='user view')
]