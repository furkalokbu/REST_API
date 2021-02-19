from django.urls import include, path
from questions.api import views as qv
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"questions", qv.QuestionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
