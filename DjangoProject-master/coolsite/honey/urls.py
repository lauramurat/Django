from django.urls import path, re_path
from django.utils import archive

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addproduct/', addproduct, name='addproduct'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('login/', login, name='login'),
    path('registeer/', register, name='register'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name = 'category'),
]