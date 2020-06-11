
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

# from .forms import PostForm
# Create your views here.
def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

# def daily_neccessity(request):
#     posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/daily_necessity.html', {'posts':posts})

def daily_necessity(request):
    return render(request, 'blog/daily_necessity.html')

def eventitem(request):
    return render(request, 'blog/eventitem.html')

def ingredients(request):
    return render(request, 'blog/ingredients.html')

def online(request):
    return render(request, 'blog/online.html')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # return redirect('post_detail', pk=post.pk)
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

# def creat(request):
#     blog=Blog()
#     blog.title=request.GET['title']
#     blog.body=request.GET['body']
#     blog.price=request.GET['price']
#     blog.put_date=timezone.datetime.now()
#     blog.save()
#     return redirect('/blog/'+str(blog.id))
