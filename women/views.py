from re import S
from turtle import title
from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render

from .serializers import WomenSerializer
from .models import Women


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()  # ленивый запрос
    serializer_class = WomenSerializer


class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

# class WomenAPIView(APIView):
#     def get(self, request):
#         posts = Women.objects.all().values()
#         return Response({'posts': WomenSerializer(posts, many=True).data})

#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'post': serializer.data})

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)

#         if not pk:
#             return Response({'error': 'Method PUT not allowed.'})

#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exists.'})
        
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'post': serializer.data})

#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)

#         if not pk:
#             return Response({'error': 'Method DELETE not allowed.'})

#         try:
#             instance = Women.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({'error': 'Object does not exists.'})
#         return Response({'post': 'delete post ' + str(pk)})


# lesson 2
# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer