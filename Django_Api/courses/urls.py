from django.urls import path
from django.urls.conf import path, include
from . import views
from rest_framework import routers

# to get the data or to save the data we required router
router = routers.DefaultRouter()
# we can use any name in place of 'courses'
router.register('courses', views.CourseView)

urlpatterns = [
    path('', include(router.urls)),


]
