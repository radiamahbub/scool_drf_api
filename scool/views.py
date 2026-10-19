from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from scool.serializers import *
from scool.models import *

# APIView----------------------------------------------------------------------------------

class CourseListAPI(APIView):
    def get(self, request):
        course_data = CourseModel.objects.all()

        serializers_data = CourseSerializer(course_data, many=True)

        return Response({
            'success':True,
            'message':"Successfully got course information.",
            'data':serializers_data.data
        }, status=status.HTTP_200_OK)


    def post(self, request):

        serializers_data = CourseSerializer(data = request.data)

        if serializers_data.is_valid():
            serializers_data.save()

            return Response({
                'success':True,
                'message':"Successfully created course information.",
                'data':serializers_data.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'success':True,
                'message':serializers_data.errors
            }, status=status.HTTP_400_BAD_REQUEST)

class CoursedetailsAPI(APIView):
    def get_object(self, request, id):
        try: 
            data = get_object_or_404(CourseModel, id=id)  
        except:
            return Response({
                'success':True,
                'message':'Data not found.',
                'data': []
            }, status=status.HTTP_404_NOT_FOUND)


    def get(self, request, id):
        course_data = self.get_object(id)
        serializer_data = CourseSerializer(course_data)
        return Response({
            'success':True,
            'message':"Successfully created course's details information.",
            'data': serializer_data.data
        }, status=status.HTTP_201_CREATED)   

    def put(self, request, id):

        course_data = self.get_object(id)

        serializers_data = CourseSerializer(course_data, data = request.data)
        
        if serializers_data.is_valid():
            serializers_data.save()

            return Response({
                'success':True,
                'message':"Successfully updated course information.",
                'data':serializers_data.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'success':True,
                'message':serializers_data.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        self.get_object(id).delete()
        return Response({
            'success':True,
            'message':'Data deleted',
            'data': []
        }, status=status.HTTP_410_GONE)

# GENERICS----------------------------------------------------------------------------------

class SubjectListAPI(generics.ListCreateAPIView):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializer 

class SubjectIndividual(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializer       



            
