from django.contrib import admin
from django.urls import path
from p_library import views
from p_library.views import AuthorEdit, AuthorList 

app_name = 'p_library' 
urlpatterns = [
    path('author/create', AuthorEdit.as_view(), name='author_create'),  
    path('authors', AuthorList.as_view(), name='author_list'),  
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('house_list/', views.house_list),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
]
