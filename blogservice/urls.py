from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about),
    path('post/<int:id>/', show_post, name='post'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('addpost/', add_post, name = 'addpost'),
    path("like/", likes,)
]