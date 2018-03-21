

from rest_framework import serializers
from study.models import Study


class StudySerializers(serializers.ModelSerializer):

    class Meta:
        model = Study
        fields = ('id','create_time','title','url','password','abstract','images')