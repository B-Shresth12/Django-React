from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSearializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# note Models
from .models import Note


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


# Note Class
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSearializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user  # $user = auth()->user()
        return Note.objects.filter(author=user)  # $notes = $user->notes

    def perform_create(self, serializer):
        if serializer.is_valid():  # checks the model $request->validate()
            serializer.save(author=self.request.user)  # $note->save()
        else:
            print(serializer.errors)


# Delete Notes
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSearializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
