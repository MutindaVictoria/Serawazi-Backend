from django.db import models
import openai 
import json

# Create your models here.

class Message(models.Model):
    content = models.TextField()
    is_user_message = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    bot_response = models.TextField('Response')
    chatgpt_api_key = models.CharField(max_length=100)
    summary = models.JSONField(null=True, blank=True)  # Allow it to be nullable and blank

    def save(self, *args, **kwargs):
        # Construct the summary JSON based on content and bot_response
        summary_data = {
            "content": self.content,
            "bot_response": self.bot_response,
        }

        # Convert the dictionary to JSON and store it in the summary field
        self.summary = json.dumps(summary_data)

        super(Message, self).save(*args, **kwargs)

    def __str__(self):
        return f"Message {self.id}"
# Setting up API key
openai.api_key = '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'