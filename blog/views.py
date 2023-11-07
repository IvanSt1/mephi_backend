from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(generic.ListView):
    model = Post
    
class DetailView(generic.DetailView):
    model = Post

class CreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ['title', 'text']
    template_name = "blog/post_new.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)  
    
class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    fields = ['title', 'text']
    template_name = "blog/post_edit.html" 
    
class DeleteView(LoginRequiredMixin, generic.DeleteView):
    # post_confirm_delete.html
    model = Post
    success_url = reverse_lazy("blog:index") 

class IndexView(generic.ListView):
    model = Post
    paginate_by = 10
    queryset = Post.objects.prefetch_related('author')