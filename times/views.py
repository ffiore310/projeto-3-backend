from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.http import Http404, HttpResponseForbidden, JsonResponse
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Time
from .serializers import TimeSerializer

@api_view(['POST'])
def api_user(request):
    if request.method == 'POST':
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']

        user = User.objects.create_user(username=username, password=password,email=email)
        user.save()
        return Response(status=204)


@api_view(['POST'])
def api_get_token(request):
    try:
        if request.method == 'POST':
            username = request.data['username']
            print(username)
            password = request.data['password']
            print("a senha eh: ",password)
            user = authenticate(username=username, password=password)

            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return JsonResponse({"token":token.key})
            else:
                print("Usuário não autenticado")
                return HttpResponseForbidden()
    except:
        return HttpResponseForbidden()
    

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def api_favoritos(request, note_id):
    times = Time.objects.all()
    serialized_time = TimeSerializer(times, many=True)
    return Response(serialized_time.data)