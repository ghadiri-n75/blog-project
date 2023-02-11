from urllib import request
from django.shortcuts import redirect, render, get_object_or_404
from . models import Article, Category, Comment, Message, Ticket,Likes
from django.core.paginator import Paginator
from .forms import ContactUsForm, MessageForm, TicketForm, SetEmail
from django.contrib.auth.models import User
from django.views.generic.base import  TemplateView , RedirectView
from django.views.generic import DetailView ,ListView , FormView , CreateView , ArchiveIndexView
from .forms import MessageForm
from django.urls import reverse_lazy


# Create your views here.


def post_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(body=body, user=request.user,
                               article=article, parent_id=parent_id)
    return render(request, 'article_app/post_details.html', {'article': article})


def post_list(request):
    article = Article.objects.all()
    paginator = Paginator(article, 2)
    page_number = request.GET.get('page')
    objects_list = paginator.get_page(page_number)
    return render(request, 'article_app/post_list.html', {'article': objects_list})


def categoty_list(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    article = category.articles.all()
    return render(request, 'article_app/post_list.html', {'article': article})


def search(request):
    q = request.GET.get('q')
    article = Article.objects.filter(title__icontains=q)
    paginator = Paginator(article, 2)
    page_number = request.GET.get('page')
    objects_list = paginator.get_page(page_number)
    return render(request, 'article_app/post_list.html', {'article': objects_list})


def contact_us(request):
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            email = form.cleaned_data['email']
            Message.objects.create(title=title, text=text, email=email)
            return redirect('article_app:contact_us')
    else:
        form = MessageForm()
    return render(request, 'article_app/contact_us.html', {'form': form})


def ticket_to_us(request):
    if request.method == 'POST':
        form = TicketForm(data=request.POST)
        if form.is_valid():
            author = request.user
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            if request.user.email:

                Ticket.objects.create(title=title, text=text, author=author)
                return redirect('home_app:home_page')
            else:
                return redirect('article_app:set_email')

    else:
        form = TicketForm()
    return render(request, 'article_app/ticket_to_us.html', {'form': form})


def set_email(request):
    if request.method == 'POST':
        form = SetEmail(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            User.objects.filter(id=request.user.id).update(email=email)
            return redirect('article_app:ticket')
        else:
            return redirect('article_app:set_email')
    else:
        form = SetEmail()
    return render(request, 'article_app/set_email.html', {'form': form})


#    ......... class base viws .............



class PostList(TemplateView):
    model=Article
    template_name="article_app/class_post_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = Article.objects.all()
        return context


class RedirectTo(RedirectView):
    # url= '/article/list'
    pattern_name= 'article_app:set_email'
    
    
class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_app/post_details.html"
    
    
    
class ArticleListView(ListView):
    model= Article
    template_name = 'article_app/post_list.html'
    context_object_name = 'article'
    paginate_by = 2
    
    
class ContactUs(FormView):
    template_name = 'article_app/contact_us.html'
    form_class = MessageForm
    success_url = reverse_lazy('home_app:home_page')
    
    def form_valid(self, form):
        form_data=form.cleaned_data
        Message.objects.create(**form_data)
        return super().form_valid(form)
        
        
class MessageView(CreateView):
    model= Message
    template_name: str = 'article_app/contact_us.html'
    fields =( 'title' , 'text')
    success_url = reverse_lazy('home_app:home_page')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = Message.objects.all()
        return context
    
    def form_valid(self, form) :
        instance= form.save(commit=False)
        instance.email = self.request.user.email
        instance.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        print(self.object)
        return super(MessageView,self).get_success_url()



class ArchiveIndexArticleView(ArchiveIndexView):
    model = Article
    date_field = ' pub_date'
    
    
def likes(request,slug,pk):
    try:
       like=Likes.objects.get(article__slug=slug,user_id=request.user.id)
       like.delete()
    except:
        like=Likes.objects.create(article_id=pk , user_id=request.user.id)
        
    return redirect('article_app:post_details',slug)