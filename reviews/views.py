from django.shortcuts import render
from .models import *


def details(request, content_id):
    """
    You could easily change this to your by appending the .get(pk=content_id)
    """
    content = Content.objects.annotate(nreview=Count('review'), avg=Avg('review__avg_rating'))
    print(content)
    return render(request, 'content/details.html', {'content': content})
