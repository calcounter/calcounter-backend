from django.conf.urls import include, url
from api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'^meals', views.MealViewSet)

urlpatterns = [
    url(r'^profile/$', views.ProfileView.as_view()),
    url(r'^', include(router.urls)),
]
