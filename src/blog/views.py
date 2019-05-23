from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post
from django.contrib.auth.models import User


# def index(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blogs/index.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = '-date_posted'
    paginate_by = 3

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = '-date_posted'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(authors=user).order_by('-date_posted')




class PostDetailView(DetailView):
    model = Post


## To make a post user need to login at first
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    ## author name set to the user name
    def form_valid(self, form):
        form.instance.authors = self.request.user
        return super().form_valid(form)


# Need to login,Need to the author of that post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    ## author name set to the user name
    def form_valid(self, form):
        form.instance.authors = self.request.user
        return super().form_valid(form)

    # if:user=author,then user can update that post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.authors:
            return True
        else:
            False


class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    success_url = '/'

    # if:user=author,then user can delete that post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.authors:
            return True
        else:
            False


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
