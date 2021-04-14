from rest_framework import serializers

from .models import Survey, Response, Question


class QuestionSerializer(serializers.ModelSerializer):
    """Вывод вопроса"""

    class Meta:
        model = Question
        fields = ['id', 'text', 'type', 'pub_date']


class SurveyListSerializer(serializers.ModelSerializer):
    """Вывод списка опросов"""

    class Meta:
        model = Survey
        fields = ['id', 'title', 'start_date', 'finish_date', 'text']


class SurveyDetailSerializer(serializers.ModelSerializer):
    """Вывод опроса"""
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Survey
        fields = ['id', 'title', 'start_date', 'finish_date', 'text', 'questions']


class ResponseCreateSerializer(serializers.ModelSerializer):
    """Добавление ответа"""

    class Meta:
        model = Response
        fields = ['question', 'choice_text']


class ResponseListSerializer(serializers.ModelSerializer):
    """Получение списка опросов пользователя"""

    class Meta:
        model = Response
        fields = ['question', 'choice_text']
        depth = 1
