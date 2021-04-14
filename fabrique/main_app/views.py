from django.db import models
from rest_framework import generics

from .models import Survey, get_ip, Response
from .serializers import SurveyListSerializer, ResponseCreateSerializer, SurveyDetailSerializer, ResponseListSerializer


class SurveyListView(generics.ListAPIView):
    """Вывод списка опросов"""

    serializer_class = SurveyListSerializer
    queryset = Survey.objects.filter(is_active=True)


class SurveyDetailView(generics.RetrieveAPIView):
    """Вывод активного опроса"""
    serializer_class = SurveyDetailSerializer
    queryset = Survey.objects.filter(is_active=True)


class ResponseCreateView(generics.CreateAPIView):
    """Создание ответа"""
    serializer_class = ResponseCreateSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_ip(self.request))


class ResponseView(generics.ListAPIView):
    """Вывод вопросов пользователя"""
    serializer_class = ResponseListSerializer

    def get_queryset(self):
        queryset = Response.objects.filter(ip=get_ip(self.request))
        return queryset
