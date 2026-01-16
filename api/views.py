from django.shortcuts import render
from Beauty.models import Master
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action

from api.serializators import MasterSerializer

class MasterList(APIView):

    @action(methods=['get'], detail=False)
    def get(self, request, format=None):
        masters = Master.objects.all()
        serializer = MasterSerializer(masters, many=True)
        return Response(serializer.data)

    @action(methods=['post'])
    def post(self, request, format=None):
        serializer = MasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MasterDetail(APIView):
    def get_object(self, pk):
        try:
            return Master.objects.get(pk=pk)
        except Master.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        master = self.get_object(pk)
        serializer = MasterSerializer(master)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        master = self.get_object(pk)
        serializer = MasterSerializer(master, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        master = self.get_object(pk)
        master.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)