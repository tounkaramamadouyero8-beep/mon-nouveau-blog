from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .forms import MessageForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts': posts})

def create_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message_success')
    else:
        form = MessageForm()

    return render(request, 'blog/message_form.html', {'form': form})


def message_success(request):
    return render(request, 'blog/message_success.html')
