from rest_framework import serializers

class AuthSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    auth_token = serializers.CharField(max_length=500, read_only=True)
    first_name = serializers.CharField(max_length=250)
    last_name = serializers.CharField(max_length=250)