
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SignUpSerializer,LoginSerializer



from rest_framework import permissions, status

# Create your views here.


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {"message": "Kullanici olusturuldu", "data": serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = []
    serializer_class = LoginSerializer
    def post(self, request: Request):
        serializer_class = self.serializer_class(data=request.data)
        if serializer_class.is_valid():
            token = serializer_class.validated_data['token']
            return Response(data=token,status=status.HTTP_200_OK)
            
        
       

        
    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)



class RetrieveUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = request.user
    user = SignUpSerializer(user)

    return Response(user.data, status=status.HTTP_200_OK)

