from django.http import HttpResponse
from django.urls import path


def health(request):
    return HttpResponse('OctoFit backend is running.', content_type='text/plain')


urlpatterns = [
    path('', health, name='health'),
]
