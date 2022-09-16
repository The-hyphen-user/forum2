
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework import status

# Create your views here.

@api_view(['POST'])
def createUser(request):
    if request.method == 'POST':
        dupUser = User.objects.get(username=request.data['username'])
        if dupUser.exists():
            return Response({'message': 'User already exists'})
        else:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getUser(request, username):
    if request.method == 'GET':
        user = User.objects.get(username=request.data['username'])
        serializer = UserSerializer(user, many=False)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)