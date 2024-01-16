from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    # tags = serializers.StringRelatedField(many=True)
    # comment = serializers.StringRelatedField()
    # user = serializers.StringRelatedField()

    class Meta:
        model = Image
        fields = "__all__"