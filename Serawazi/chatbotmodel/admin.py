from django.contrib import admin
from .models import Message

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display=("content","is_user_message", "timestamp","chatgpt_api_key","bot_response","summary")
    readonly_fields = ('summary',)
admin.site.register(Message, MessageAdmin)



