"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

import os
from django.urls import path, include
from rest_framework import routers
from . import views

# Helper to get codespace base URL
def get_codespace_base_url():
    codespace_name = os.environ.get('CODESPACE_NAME', None)
    if codespace_name:
        return f"https://{codespace_name}-8000.app.github.dev"
    return "http://localhost:8000"


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'workouts', views.WorkoutViewSet)
router.register(r'leaderboard', views.LeaderboardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', views.api_root, name='api-root'),
]

# Optionally, you can add a view to return the API base URL for debugging
from django.http import JsonResponse
def api_base_url(request):
    return JsonResponse({"api_base_url": get_codespace_base_url() + "/api/"})

urlpatterns += [
    path('api-base-url/', api_base_url, name='api-base-url'),
]
