from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Market, Scrap
from .forms import PostForm
import csv
from django.http import HttpResponse

def store(request):
    #이화가 구현한 시간순 정렬.. 크으
    #posts = Market.objects.order_by('-scrap_count')
    posts = Market.objects.order_by('-pub_date')
    return render(request, 'store.html', {'posts': posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Market, pk = post_id)
    #if User.DoesNotExist:
        #return render(request, 'detail.html', {'post': post_detail})
    #else: 
    scrap = Scrap.objects.filter(user=request.user, post=post_detail)
    return render(request, 'detail.html', {'post': post_detail, 'scrap': scrap})



    #post_detail = get_object_or_404(Market, pk = post_id)
    #if request.user.exists():
    #    scrap = Scrap.objects.filter(user=request.user, post=post_detail)
    #    return render(request, 'detail.html', {'post': post_detail, 'scrap': scrap})
    #else:
    #    return render(request, 'detail.html', {'post': post_detail})

    
def new(request):
    return render(request, 'new.html')

def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(username = request.user.get_username())
            post.save()
            return redirect('store')
    else:
        form = PostForm()
    return render(request, 'new.html', {'form': form})

def edit(request):
    return render(request, 'edit.html')

def postupdate(request, post_id):
    post = get_object_or_404(Market, pk = post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(username = request.user.get_username())
            post.save()
            return redirect('detail', post_id=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'edit.html', {'form':form})

def postdelete(request, post_id):
    post = get_object_or_404(Market, pk=post_id)
    post.delete()
    return redirect('store')

def scrap(request, post_id):
    post = get_object_or_404(Market, pk=post_id)
    scrapped = Scrap.objects.filter(user=request.user, post=post)
    if not scrapped:
        Scrap.objects.create(user=request.user, post=post)
    #request.user는 현재 로그인한 user
    else:
        scrapped.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



#서치기능
def result(request):
    post_object = Market.objects
    query = request.GET.get('query','')
    if query:
        post_object = post_object.filter(title__contains=query).order_by('-pub_date')
        return render(request, 'result.html', {'result':post_object})

def empty_ppt(request):
    return render(request, 'empty_ppt.html')

def ppt(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="papo.ppt"'
    
    writer = csv.writer(response)
    writer.writerow({'paporika!'})
    
    return response