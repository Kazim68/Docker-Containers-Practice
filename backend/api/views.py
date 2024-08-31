from django.shortcuts import render
from django.contrib.auth.models import User
from  rest_framework import generics, status
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Note
from rest_framework.response import Response

# Create your views here.


class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def create(self, request, *args, **kwargs):
        self.request.data.update({'author': self.request.user.id})
        serializer = NoteSerializer(data=self.request.data)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]