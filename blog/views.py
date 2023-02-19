from django.shortcuts import get_object_or_404, render
from django.views.generic import  DeleteView, CreateView, UpdateView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from .filter import Filter


def index(request):
    db_list = Post.objects.all()
    db_filter = Filter(request.GET, queryset=db_list)
    return render(request, 'index.html', {'filter':db_filter})


def Blog_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    comment = Comment.objects.filter(post=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post = post
            form.save()
    else:
        form = CommentForm()


    return render(request, 'post_detail.html', {'post':post, 'comment':comment, 'form':form})

   

class CreatePost(CreateView):
    model = Post
    template_name = 'new_post.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePost(UpdateView):
    model = Post
    template_name = 'update.html'
    form_class = UpdateForm




class DeletePost(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('index')



class CreateCategory(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    success_url = reverse_lazy('index')

    