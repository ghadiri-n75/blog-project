from django.shortcuts import render
from article_app.models import Article

# Create your views here.

def home_page(request):
    article=Article.objects.all()
    recent_article=Article.objects.all()[:3]
    return render(request, 'home_app/index.html',{'article':article})


def sidebar(request):
    context={'name':'ghadiri'}
    return render (request,'include/sidebar.html',context=context)


