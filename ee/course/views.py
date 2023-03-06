from rest_framework.views import APIView
from .serializer import CourseSerializer, ElectiveSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Elective, Course
from django.http import JsonResponse

class CreateCourseView(APIView):
    def post(self, request):
        if request.method == "POST":
            serializer = CourseSerializer(data=request.data)
            if serializer.is_valid():
                data = serializer.create(request.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "{} method is not allowed".format(request.method)})


class GetCourseByProgramView(APIView):
    def get(self, request):
        if request.method == "GET":
            try:
                course = Course.objects.filter(semester=request.data.get('semester'), program=request.data.get('program')).values()
            except Course.DoesNotExist:
                return Response({"message": "Course of the required program and semester not found"}, status=status.HTTP_404_NOT_FOUND)
            return Response(course)
        return Response({"message": "{} method is not allowed".format(request.method)})

