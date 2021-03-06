from django.http.response import Http404
from .models import BackendData
from .serializers import BackendSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class VideoList(APIView):
# Create your views here.
    def get(self, request):
        data = BackendData.objects.all()
        serializer = BackendSerializer(data, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BackendSerializer(data = request.data, many = True)
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
    
    #get by id
    def get(self, request, pk):
        video_details = self.get_video_details(pk)
        serializer = BackendSerializer(video_details)
        return Response(serializer.data)
    
    #update    
    def put(self, request, pk):
        video_details = self.get_video_details(pk)
        serializer = BackendSerializer(video_details, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    #delete
    def delete(self, request, pk):
        video_details = self.get_video_details(pk)
        video_details.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
  