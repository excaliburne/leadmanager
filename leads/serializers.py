from rest_framework import serializers
from . import models 

# Lead Serializer 
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lead
        fields = '__all__'