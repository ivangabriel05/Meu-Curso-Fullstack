from django.shortcuts import render
from rest_framework import generics, filters, serializers
from apps.core.models import clients
from .serializers import PostSerializer
from rest_framework import filters

class PostListCreate(generics.ListCreateAPIView):
 queryset = clients.objects.all()
 serializer_class = PostSerializer
 filter_backends = [filters.SearchFilter, filters.OrderingFilter]
 search_fields = ['title', 'content']
 ordering_fields = ['created_at']

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset = clients.objects.all()
 serializer_class = PostSerializer

class PostSerializer(serializers.ModelSerializer):
 class Meta:
    model = clients
    fields = ['id', 'title', 'content', 'created_at']
 def validate_title(self, value):
    if len(value) < 5:
        raise serializers.ValidationError("O título deve ter pelo menos 5caracteres.")
    return value

