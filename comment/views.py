from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from market.models import Market
from .models import Comment 
from django.contrib.auth.models import User

# Create your views here.

def commentcreate(request, post_id):
    post = get_object_or_404(Market, pk=post_id)

    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = User.objects.get(username = request.user.get_username())
            comment.post = post
            comment.save()
            return redirect('detail', post_id=post.pk)
        else:
            redirect('list')

    else:
        form = CommentForm()
        return render(request, 'detail.html', {'form': form, 'post': post})


def commentupdate(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if request.user != comment.author:
        messages.warning(request, "권한 없음")
        #return redirect(document)

    if request.method=='POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('detail', post_id=comment.post.pk)
        else:
            return redirect('list')

    else:
        form = CommentForm(instance=comment)
        return render(request, 'detail.html', {'form_comment': form, 'post': comment.post})







def commentdelete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.author == User.objects.get(username = request.user.get_username()):
        comment.delete()
    return redirect('detail', post_id=comment.post.pk)