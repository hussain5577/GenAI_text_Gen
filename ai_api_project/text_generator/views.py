from rest_framework import viewsets
from rest_framework.response import Response
from transformers import pipeline
from .models import TextGeneration
from .serializers import TextGenerationSerializer

class TextGenerationViewSet(viewsets.ModelViewSet):
    queryset = TextGeneration.objects.all()
    serializer_class = TextGenerationSerializer
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Initialize the model only once when the view is created
        self.generator = pipeline('text-generation', model='gpt2')
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Generate text using the model
        prompt = serializer.validated_data['prompt']
        generated_text = self.generator(
            prompt,
            max_length=100,
            num_return_sequences=1
        )[0]['generated_text']
        
        # Save the generation
        instance = TextGeneration.objects.create(
            prompt=prompt,
            generated_text=generated_text
        )
        
        response_serializer = self.get_serializer(instance)
        return Response(response_serializer.data)