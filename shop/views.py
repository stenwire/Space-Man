from django.views import generic
from .models import Post

class ItemList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'shop.html'

class ItemDetail(generic.DetailView):
    model = Post
    template_name = 'item_detail.html'
