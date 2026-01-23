from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny

from authentication.serializers import RegisterSerializer, CustomTokenObtainPairSerializer
from django.contrib.auth.models import User

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.response import Response
from rest_framework import status

class UserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            return Response({
                {"detail": "Usuário cadastrado. Solicitação foi enviada ao administrador."}
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

@api_view(["POST"])
@permission_classes([IsAdminUser])
def approve_user(request, pk):
    user = User.objects.get(pk=pk, is_active=False)
    user.is_active = True
    user.save()

    return Response(
        {"detail": "Usuário aprovado com sucesso."},
        status=status.HTTP_200_OK
    )

@api_view(["POST"])
@permission_classes([IsAdminUser])
def reject_user(request, pk):
    user = User.objects.get(pk=pk, is_active=False)
    user.delete()

    return Response(
        {"detail": "Usuário reprovado."},
        status=status.HTTP_200_OK
    )

@api_view(["GET"])
@permission_classes([IsAdminUser])
def pending_user(request):
    users = User.objects.filter(is_active=False)
    data = [{"id": user.id, "email": user.email} for user in users]

    return Response(data)