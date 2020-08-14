from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = User.objects.filter(pk = self.request.user.id)
        return queryset
    
    @action(detail=True, methods=['post'], permission_classes=[AllowAny])
    def sign_up(self, request):
        data = request.data
        user_serializer = serializers.UserSerializer(data=data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return Response({'data':data})
    
    @action(detail=True, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response({
                    "is_authenticated": True,
                    "user": serializers.UserSerializer(request.user).data,
                    "auth_token": user.auth_token.key
                })
        else:
            return Response({"is_authenticated": False,"message":"Email ID is Wrong"}, status=status.HTTP_403_FORBIDDEN)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def logout(self, request):
        logout(request)
        return Response({"logged_out": True})