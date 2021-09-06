from rest_framework import serializers
from curd.models import employee

class curdserializers(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields= '__all__' 
        