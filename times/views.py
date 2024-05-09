from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.http import Http404, HttpResponseForbidden, JsonResponse
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt

from .models import UserProfile, Time
from .serializers import TimeSerializer

@api_view(['POST'])
# @permission_classes([AllowAny])
@csrf_exempt
def api_user(request):
    if request.method == 'POST':
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        # name = request.data['name']

        # user = User.objects.create_user(username, password)
        # user.save()
        new_profile = UserProfile(name=username, email=email, password=password)
        new_profile.save()
        return Response(status=204)


@api_view(['POST'])
def api_get_token(request):
    try:
        if request.method == 'POST':
            username = request.data['username']
            password = request.data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return JsonResponse({"token":token.key})
            else:
                return HttpResponseForbidden()
    except:
        return HttpResponseForbidden()
    
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def api_notes(request):

    if request.method == "POST":
        new_note_data = request.data
        title = new_note_data['title']
        content = new_note_data['content']
        note = Note(title=title, content=content)
        note.save()

    notes = Note.objects.all()

    serialized_note = NoteSerializer(notes, many=True)
    return Response(serialized_note.data)

@api_view(['GET', 'POST'])
def api_favoritos(request, note_id):
    times = Time.objects.all()
    serialized_time = TimeSerializer(times, many=True)
    return Response(serialized_time.data)