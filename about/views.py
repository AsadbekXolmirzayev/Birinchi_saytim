from django.shortcuts import render
from .models import Feedback


def about(request):
    feedbacks = Feedback.objects.all()
    # last_3_articles = Article.objects.order_by('-id')[:3]
    ctx = {
        "feedbacks": feedbacks
    }
    return render(request, 'wordify/about.html', ctx)


# Create your views here.
