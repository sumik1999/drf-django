from django.urls import path
from .views import PostList,PostDetail

urlspatterns = [
    path("",PostList.as_view(),"listposts"),
    path("/<int:pk>/",PostDetail.as_view(),name="postdetail")
]