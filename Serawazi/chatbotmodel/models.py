from django.db import models
import openai 


# Create your models here.
class ChatbotSession(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
class Message(models.Model):
    sesssion = models.ForeignKey(ChatbotSession, on_delete=models.CASCADE)
    content = models.TextField()
    is_user_message = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
class ChatbotResponse(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    content = models.TextField()
class Chatbot(models.Model):
    name = models.CharField(max_length=100)
    description=models.TextField()
    chatgpt_api_key = models.CharField(max_length=100)

# Setting up API key
openai.api_key = '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'

def get_governance_principles_response(user_question):
    prompt = f"User: {user_question}\nAI:"

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100
    )

    return response.choices[0].text.strip()

def __str__(self):
    return self.name