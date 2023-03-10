from django.urls import path, re_path
from django.utils import archive

from .views import *

urlpatterns = [
    path('', ProductHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addproduct/', AddProduct.as_view(), name='addproduct'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('login/', login, name='login'),
    path('registeer/', register, name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', ProductCategory.as_view(), name = 'category'),
]