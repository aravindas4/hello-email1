from . import api
from django.urls import include, path
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('category/list/', api.CategoriesCoursesAPIView.as_view())
]

router = SimpleRouter()

router.register(r'email', api.EmailModelViewSet, basename='email')

urlpatterns += router.urls
