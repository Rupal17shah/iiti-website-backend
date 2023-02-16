from rest_framework.views import APIView
from .serializer import ResearchSerializers,PapersSerializers,ProjectsSerializers,LabsSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Research, Projects, Papers, Labs
# Create your views here.


class ResearchView(APIView):
    def post(self, request):
        if request.method == "POST":
            serializer = ResearchSerializers(data=request.data)
            if serializer.is_valid():
                data = serializer.create(request.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "{} method is not allowed".format(request.method)})


class GetResearchView(APIView):
    def get(self, request):
        if request.method == "GET":
            try:
                research = Research.objects.all()
            except research.DoesNotExist:
                return Response({"error": "No research"}, status=404)
            research = ResearchSerializers(research, many=True)
            return Response(research.data)
        return Response({"message": "{} method is not allowed".format(request.method)})
    

class ProjectView(APIView):
    def post(self, request):
        if request.method == "POST":
            serializer = ProjectsSerializers(data=request.data)
            if serializer.is_valid():
                data = serializer.create(request.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "{} method is not allowed".format(request.method)})


class GetProjectView(APIView):
    def get(self, request):
        if request.method == "GET":
            try:
                project = Projects.objects.all()
            except project.DoesNotExist:
                return Response({"error": "No project"}, status=404)
            project = ProjectsSerializers(project, many=True)
            return Response(project.data)
        return Response({"message": "{} method is not allowed".format(request.method)})
    

class LabsView(APIView):
    def post(self, request):
        if request.method == "POST":
            serializer = LabsSerializer(data=request.data)
            if serializer.is_valid():
                data = serializer.create(request.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "{} method is not allowed".format(request.method)})


class GetLabsView(APIView):
    def get(self, request):
        if request.method == "GET":
            try:
                Lab = Labs.objects.all()
            except Lab.DoesNotExist:
                return Response({"error": "No Labs"}, status=404)
            Lab = LabsSerializer(Lab, many=True)
            return Response(Lab.data)
        return Response({"message": "{} method is not allowed".format(request.method)})
    

class PapersView(APIView):
    def post(self, request):
        if request.method == "POST":
            serializer = PapersSerializers(data=request.data)
            if serializer.is_valid():
                data = serializer.create(request.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "{} method is not allowed".format(request.method)})


class GetPapersView(APIView):
    def get(self, request):
        if request.method == "GET":
            try:
                paper = Papers.objects.all()
            except paper.DoesNotExist:
                return Response({"error": "No papers"}, status=404)
            paper = ResearchSerializers(paper, many=True)
            return Response(paper.data)
        return Response({"message": "{} method is not allowed".format(request.method)})
