from rest_framework import serializers
from home.models import Records

class ItemSerializer(serializers.ModelSerializer):

    class Meta:

        model = Records
        fields = '__all__'
