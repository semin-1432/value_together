from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
# from .forms import PostForm
# Create your views here.
def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# def post_new(request):
#     form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})

def writing_page(request):
    # posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/writing_page.html')

# def creat(request):
#     blog=Blog()
#     blog.title=request.GET['title']
#     blog.body=request.GET['body']
#     blog.price=request.GET['price']
#     blog.put_date=timezone.datetime.now()
#     blog.save()
#     return redirect('/blog/'+str(blog.id))
