from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from movies.account.serializers import  RegisterSerializer, LoginSerializer, ChangePasswordSerializer

User = get_user_model()

class RegisterView(APIView):
 def post(self,request):
        data = request.data
        serializers = RegisterSerializer(data=data)

        if serializers.is_valid(raise_exception=True):
            serializers.save()
            message = f'Вы смогли зарегаться.Чекните почту'
            return Response(message, status=201)

class ActivationView(APIView):
    def get(self,request,activation_code):
        try:
            user = User.objects.get(activation_code = activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'msg': 'Успешно'}, status=200 )
        except User.DoesNotExist:
            return Response({'msg': 'Неверный код!'}, status=400)

class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializers = ChangePasswordSerializer(data=request.data,
                                               context={'request': request})

        serializers.is_valid(raise_exception=True)
        serializers.set_new_password()
        return Response('Пароль был обновлен успешно.')


class LogOutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Вы успешно вышли с аккаунта.')



