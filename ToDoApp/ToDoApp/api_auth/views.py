from django.contrib.auth import get_user_model
from rest_framework import generics as rest_generic_views
from rest_framework import views as rest_views
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response


from ToDoApp.api_auth.serializers import CreateUserSerializer

UserModel = get_user_model()


class CreateUserApiView(rest_generic_views.CreateAPIView):
    queryset = UserModel
    serializer_class = CreateUserSerializer


class LoginApiView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
        })


class LogoutApiView(rest_views.APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass

    def __perform_logout(request):
        request.user.auth_token.delete()
        return Response({
            'message': 'user log out'
        })
