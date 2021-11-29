from django.http.response import Http404
from .models import BackendData
from .serializers import YoutubeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class VideoList(APIView):
    
    def get(self, request):
        data = BackendData.objects.all()
        serializer = YoutubeSerializer(data, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = YoutubeSerializer(data = request.data, many = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class VideoDetails(APIView):
    
    def get_video_details(self, pk):
        try:
            return BackendData.objects.get(pk = pk)
        except:
            raise Http404
    
    def get(self, request, pk):
        video_details = self.get_video_details(pk)
        serializer = YoutubeSerializer(video_details)
        return Response(serializer.data)
    
        
    def put(self, request, pk):
        video_details = self.get_video_details(pk)
        serializer = YoutubeSerializer(video_details, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        video_details = self.get_video_details(pk)
        video_details.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
  