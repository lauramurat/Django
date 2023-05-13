from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied, BadRequest
from django.core.paginator import Paginator
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import TokenAuthentication

from .serializers import HoneySerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .forms import *
from .utils import *
from rest_framework.views import APIView

class HoneyAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 2

class HoneyAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = HoneySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = HoneyAPIListPagination

class HoneyAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = HoneySerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )

class HoneyAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = HoneySerializer
    permission_classes = (IsAdminOrReadOnly, )

class ProductHome(DataMixin, ListView):
    paginate_by = 3
    model = Product
    template_name = 'honey/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = "Honey Skin")
        return dict(list(context.items()) +list(c_def.items()))

    def get_queryset(self):
        return Product.objects.filter(is_published = True).select_related('cat')

class AddBailanys(DataMixin, FormView):
    form_class = BailanysForm
    template_name = 'honey/bailanys.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Bailanys")
        return dict(list(context.items()) + list(c_def.items()))

    # def form_valid(self, form):
    #     bailanys = form.save()
    #     return redirect('home')

def about(request):
    contact_list = Product.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'honey/about.html', {'page_obj': page_obj, 'menu': menu, 'title': 'Біз жайлы'})


def blog(request):
    contact_list = Product.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'honey/blog.html', {'page_obj': page_obj, 'menu': menu, 'title': 'Біз жайлы'})


class CosmeticHome(DataMixin, ListView):
    paginate_by = 3
    model = Product
    template_name = 'honey/kosmetics.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = "Honey Skin")
        return dict(list(context.items()) +list(c_def.items()))

    def get_queryset(self):
        return Product.objects.filter(is_published = True).select_related('cat')

class AddProduct(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddProductForm
    template_name = 'honey/addproduct.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = "Add product")
        return dict(list(context.items()) +list(c_def.items()))

class News(LoginRequiredMixin, DataMixin, CreateView):
    form_class = NewsForm
    template_name = 'honey/blog.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = "Subscribe news")
        return dict(list(context.items()) +list(c_def.items()))

class ShowPost(DataMixin, DetailView):
    model = Product
    template_name = 'honey/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))

class ProductCategory(DataMixin, ListView):
    model = Product
    template_name = 'honey/kosmetics.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'honey/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Register")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'honey/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Authentication")
        return dict(list(context.items()) + list(c_def.items()))

def logout_user(request):
    logout(request)
    return redirect('login')

def categories(request,category):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>all categories =) </h1><p>{category}</p>")


def archive(request,year):
    if int(year) > 2023:
        raise Http404()
    elif int(year) == 2021:
        raise PermissionDenied
    elif int(year) == 2004:
        raise BadRequest()
    return HttpResponse(f"<h1>archives =) </h1><p>{year}</p>")


def not_found(request, exception):
    return HttpResponseNotFound('<h1> 404 </h1> <h2> Stranitsa ne naidena! </h2> ')

def closed_access(request, exception):
    return HttpResponseNotFound('<h1>Dostup zakryt!</h1>')

def bad_request(request, exception):
    return HttpResponseBadRequest("<h1>Nevozmozhno obnovit' zapros!</h1>")

def server_error(request):
    return HttpResponseServerError('<h1> Oshibka servera! </h1>')



