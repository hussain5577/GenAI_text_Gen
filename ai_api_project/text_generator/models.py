from django.db import models

class TextGeneration(models.Model):
    prompt = models.TextField()
    generated_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Generation for: {self.prompt[:50]}..."