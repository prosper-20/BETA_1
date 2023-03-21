from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
)
from .models import Post



class PostListView(ListView):
    model = Post
    template_name = 'home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'



def about(request):
    return render(request, 'about.html', {'title': 'About'})