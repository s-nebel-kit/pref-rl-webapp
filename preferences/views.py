from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.template import context

from .models import Preference


def index(request):
    latest_queries = Preference.objects.order_by('created_timestamp')[:5]
    context = {
        'latest_queries': latest_queries,
    }
    return render(request, 'preferences/index.html', context)


def query(request, query_id):

    query = get_object_or_404(Preference, pk=query_id)
    context = {
        'query': query,
        'video_url_left': query.video_url_left,
        'video_url_right': query.video_url_right
    }
    return render(request, 'preferences/query.html', context)
