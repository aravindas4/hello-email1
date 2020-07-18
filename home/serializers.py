from rest_framework import serializers
from . import models


class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Email
        fields = '__all__'
        extra_kwargs = {
            'is_success': {'read_only': True}
        }

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.send_email()
        return instance
