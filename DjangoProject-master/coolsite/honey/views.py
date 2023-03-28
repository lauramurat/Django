from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied, BadRequest
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from .utils import *

class ProductHome(DataMixin, ListView):
    model = Product
    template_name = 'honey/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = "Honey Skin")
        return dict(list(context.items()) +list(c_def.items()))

    def get_queryset(self):
        return Product.objects.filter(is_published = True)

# def index(request):
#     posts = Product.objects.all()
#     cats = Category.objects.all()
#     context = {
#         'posts': posts,
#         'cats': cats,
#         'menu': menu,
#         'title':'Basty bet',
#         'cat_selected':0,
#     }
#     return render(request, 'honey/index.html', context=context)
@login_required
def about(request):
    return render(request, 'honey/about.html', {'menu': menu, 'title': 'Біз жайлы'})

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

# def addproduct(request):
#     if request.method == 'POST':
#         form = AddProductForm(request.POST, request.FILES)
#         if form.is_valid():
#                 form.save()
#                 return redirect('home')
#     else:
#         form = AddProductForm()
#     return render(request, 'honey/addproduct.html', {'menu':menu,'form':form, 'title' : 'Продукт қосу'})

def contact(request):
    return HttpResponse("Keri bailanys")

class ShowPost(DataMixin, DetailView):
    model = Product
    template_name = 'honey/index.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = context['post'])
        return dict(list(context.items()) +list(c_def.items()))

# def show_post(request, post_slug):
#     post = get_object_or_404(Product, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'name': post.name,
#         'cat_selected':post.cat_id,
#
#     }
#     return render(request, 'honey/post.html', context=context)

class ProductCategory(DataMixin, ListView):
    model = Product
    template_name = 'honey/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(cat__slug = self.kwargs['cat_slug'], is_published = True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Category - ' + str(context['posts'][0].cat),
                                      cat_selected = context['posts'][0].cat_id)
        return dict(list(context.items()) +list(c_def.items()))

# def show_category(request, cat_id):
#     posts = Product.objects.filter(cat_id=cat_id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Basty bet',
#         'cat_selected': cat_id,
#     }
#     return render(request, 'honey/index.html', context=context)

def blog(request):
    return HttpResponse("Blog")



def login(request):
    return HttpResponse("Avtorisaviya")

def register(request):
    return HttpResponse("Tirkelu")


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



