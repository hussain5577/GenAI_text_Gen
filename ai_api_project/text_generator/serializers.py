from rest_framework import serializers
from .models import TextGeneration

class TextGenerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextGeneration
        fields = ['id', 'prompt', 'generated_text', 'created_at']
        read_only_fields = ['generated_text', 'created_at']