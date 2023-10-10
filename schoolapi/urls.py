"""Schoolapi urls.py

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
#router = routers.DefaultRouter()
#router = routers.DefaultRouter();
#router.register(r'Sitznachbar', views.SitznachbarList.as_view)



'''
urlpatterns = [
    #router.urls,
    path('Sitznachbar/', views.SitznachbarList.as_view(), name='Sitznachbar-list'),
    path('Sitznachbar/<int:pk>/', views.SitznachbarDetail.as_view(), name='Sitznachbar-detail'),
    path('account/register', views.UserCreate.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
'''
from .views import SitznachbarViewSet, UserCreateViewSet

router = routers.DefaultRouter()
router.register(r'sitznachbar-viewset', SitznachbarViewSet) # newly registered ViewSet
router.register(r'user-create-viewset', UserCreateViewSet) # newly registered ViewSet

urlpatterns = [
    #path('register-user', UserCreate.as_view()),
    path('', include(router.urls)),
]