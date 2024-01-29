from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import StreamPlatform,WatchList
from .serializers import StreamPlatformSerializer,WatchListSerializer

class StreamPlatformAV(APIView):
    def get(self,request):
        platform=StreamPlatform.objects.all()
        serializer=StreamPlatformSerializer(platform,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
class WatchListAV(APIView):
    def get(self,request):
        movies=WatchList.objects.all()
        serializer=WatchListSerializer(movies,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
class WatchDetailAV(APIView):
    def get(self,request,pk):
        try:
            movie=WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'erorr':'not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=WatchListSerializer(movie)
        return Response(serializer.data)
        
            # serializer=WatchListSerializer(movie)

    # def put(request,pk):
    # def delete(request,pk):



# Create your views here.
