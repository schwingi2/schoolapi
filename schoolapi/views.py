# Create your views here.
from .models import Sitznachbar
from django.contrib.auth.models import User
from .serializers import SitznachbarSerializer
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view  
from rest_framework.response import Response  
from rest_framework.reverse import reverse  
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import BasePermission, AllowAny

from .permissions import IsOwnerOrReadOnly
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet


'''
@api_view(["GET"])  # new
def api_root(request, format=None):
    return Response(
        {
            "Sitznachbar": reverse("Sitznachbar-list", request=request, format=format),
        }
    )
'''

'''class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, )
'''
class UserCreateViewSet(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    model = User
    serializer_class = UserSerializer
    permission_classes = [AllowAny,]

'''
class SitznachbarList(generics.ListCreateAPIView):
    queryset = Sitznachbar.objects.all()
    serializer_class = SitznachbarSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):  # new
        serializer.save(owner=self.request.user)


class SitznachbarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sitznachbar.objects.all()
    serializer_class = SitznachbarSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

'''

class SitznachbarViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Sitznachbar.objects.all()
    serializer_class = SitznachbarSerializer
    #permission_classes = [BasePermission,]
    permission_classes = [IsOwnerOrReadOnly,]
    def perform_create(self, serializer):  # new
        serializer.save(owner=self.request.user)
