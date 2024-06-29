from rest_framework import serializers
from .models import ExcelModel

class ExcelModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelModel
        fields = '__all__'
