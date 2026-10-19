from rest_framework import serializers
from scool.models import *

class CourseSerializer(serializers.Serializer):
    class Meta:
        model = CourseModel
        fields = '__all__'

class SubjectSerializer(serializers.Serializer):
    class Meta:
        model = SubjectModel
        fields = '__all__'
