from django.urls import path, re_path
from django.utils import archive
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', ProductHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addproduct/', AddProduct.as_view(), name='addproduct'),
    path('kosmetics/', CosmeticHome.as_view(), name='kosmetics'),
    # path('bailanys/', Bailanys.as_view(), name='bailanys'),
    path('blog/', blog, name='blog'),
    path('face1/', face, name='face'),
    path('face2/', face2, name='face2'),
    path('cont/', AddBailanys.as_view(), name='contact'),
    path('news/', News.as_view(), name='news'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('registeer/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', ProductCategory.as_view(), name = 'category'),
]