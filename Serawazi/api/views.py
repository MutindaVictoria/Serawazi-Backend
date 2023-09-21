from .serializers import MessageSerializer
from rest_framework.views import APIView
from chatbotmodel.models import Message
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound



class MessageListView (APIView):
   def get(self, request):
    message = Message.objects.all()
    serializer = MessageSerializer(message, many =True)
    return Response(serializer.data)
   def post(self,request):
        serializer = MessageSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
class MessageDetailView(APIView):
    def get(self, request,id,format = None):
        try:
            message= Message.objects.get(id=id)
            serializer = MessageSerializer(message)
            return Response(serializer.data)
        except Message.DoesNotExist:
            raise NotFound("Messge not found")
    def put(self, request,id,format = None):
       message = Message.objects.get(id=id)
       serializer = MessageSerializer(message,request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
       return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def delete(self, request,id,format = None):
        message=Message.objects.get(id=id)
        message.delete()
        return Response("Message has been Deleted", status = status.HTTP_204_NO_CONTENT)










