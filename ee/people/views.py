from rest_framework.views import APIView
from .serializer import PeopleSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import People
# Create your views here.


class PeopleView(APIView):
    def post(self, request):
        if request.method == "POST":
            serializer = PeopleSerializer(data=request.data)
            if serializer.is_valid():
                data = serializer.create(request.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "{} method is not allowed".format(request.method)})


class GetPeopleView(APIView):
    def get(self, request):
        if request.method == "GET":
            try:
                people = People.objects.all()
            except people.DoesNotExist:
                return Response({"error": "No people"}, status=404)
            people = PeopleSerializer(people, many=True)
            return Response(people.data)
        return Response({"message": "{} method is not allowed".format(request.method)})
    
class GetPeopleByType(APIView):
    def get(self,request,people_type):
        if request.method == "GET":
            try:
                people = People.objects.filter(people_cat=people_type).values()
            except People.DoesNotExist:
                return Response({"error": "No people"}, status=404)
            return Response(people)
        return Response({"message": "{} method is not allowed".format(request.method)})
