from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    rather = serializers.SerializerMethodField(read_only=True)
    agent = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Rating
        exclude = ["updated_at", "pkid"]

    
    def get_rather(self, obj):
        return obj.rather.username
    
    def get_agent(self, obj):
        return obj.agent.user.username
