from django.shortcuts import render
from schoolnews.models import Article

# Create your views here.
def index(request):
    context_dict = {}
    context_dict['articles'] = Article.objects.order_by('-date')
    return render(request, 'schoolnews/index.html', context=context_dict)
