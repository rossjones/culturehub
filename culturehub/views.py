from django.http import Http404
from django.shortcuts import render_to_response

from culturehub.categories.models import Category

"""
def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
"""

def home(request):
    pass

def graph(request):
    categories = Category.objects.filter(interesting=True).all()

    return render_to_response('graph.html', {
            "categories": categories

        })