from django.urls import path
from news.api.views import (
    ArticleListCreateApiView,
    ArticleDetailApiView,
    JournalistListCreateAPIView,
)

# from news.api.views import article_list_create_api_view, article_detail_api_view

urlpatterns = [
    path("articles/", ArticleListCreateApiView.as_view(), name="article-list"),
    path("articles/<int:pk>", ArticleDetailApiView.as_view(), name="article-detail"),
    path(
        "journalists/", JournalistListCreateAPIView.as_view(), name="journalists-list"
    ),
    # path("articles/", article_list_create_api_view, name="article-list"),
    # path("articles/<int:pk>", article_detail_api_view, name="article-detail"),
]
