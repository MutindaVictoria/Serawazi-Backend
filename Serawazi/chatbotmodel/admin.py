from django.contrib import admin
from .models import Chatbot
from .models import ChatbotSession
from .models import ChatbotResponse
from .models import Message

# Register your models here.
class ChatbotAdmin(admin.ModelAdmin):
    list_display=("name", "description","chatgpt_api_key")
admin.site.register(Chatbot, ChatbotAdmin)
class ChatbotSessionAdmin(admin.ModelAdmin):
    list_display=("start_time","end_time")
admin.site.register(ChatbotSession, ChatbotSessionAdmin)
class ChatbotResponseAdmin(admin.ModelAdmin):
    list_display=("message", "content")
admin.site.register(ChatbotResponse,ChatbotResponseAdmin)
class MessageAdmin(admin.ModelAdmin):
    list_display=("sesssion", "content","is_user_message", "timestamp")
admin.site.register(Message, MessageAdmin)



