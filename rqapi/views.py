from randomquestions.serializers import QuestionsSerializer
from randomquestions.models import Question
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class RandomQuestionsView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request, *args, **kwargs):
        getData = Question.objects.all()
        serializer = QuestionsSerializer(getData, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = QuestionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)