from django.db.models import Count
from django.core.cache import cache
from .models import *

menu = [
    {'title': "Біз жайлы", 'url_name':'about'},
    {'title': "Контактілер", 'url_name': 'contact'},
    {'title': "Блог", 'url_name': 'blog'},
    {'title': "Косметикалар", 'url_name': 'kosmetics'},
]

class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.annotate(Count('product'))
            cache.set('cats', cats, 60)


        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context