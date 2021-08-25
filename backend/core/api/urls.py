
from django.urls import path
from .views import PostView, PostCreateView


urlpatterns = [
    path('home/',PostView.as_view(), name = 'home'),
    path('create/',PostCreateView.as_view(), name = 'create'),

]
