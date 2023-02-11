from django import views
from django.urls import path
from . import views

app_name='article_app'

urlpatterns = [
    
    # function base views url
    path('details/<slug:slug>',views.post_details,name='post_details'),
    path('list',views.post_list,name='post_list'),
    path('category/<int:pk>',views.categoty_list ,name='category_list'),
    path('search/',views.search ,name='search-article'),
    path('contact_us',views.contact_us ,name='contact_us'),
    path('ticket',views.ticket_to_us ,name='ticket'),
    path('set_email',views.set_email ,name='set_email'),
    path('likes/<slug:slug>/<int:pk>',views.likes ,name='likes'),
    
    # class base views url 
    # path('class_list',views.PostList.as_view(),name='class_post_list'),
    path('class_list',views.ArticleListView.as_view(),name='class_post_list'),
    path('redirect_class',views.RedirectTo.as_view() ,name='redirect'),
    path('detail_class/<slug:slug>',views.ArticleDetailView.as_view() ,name='detail_class'),
    # path('class_contact_us',views.ContactUs.as_view() ,name='contact_us'),
    path('class_contact_us',views.MessageView.as_view() ,name='contact_us'),
    path('archive',views.ArchiveIndexArticleView.as_view() ,name='article_archive'),
]


