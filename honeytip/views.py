from django.shortcuts import render, get_object_or_404, redirect
from .models import Tip, Suggest
from .forms import SuggestForm

# Create your views here.
def honeytip(request):
    if request.method == 'POST':
        options = request.POST['options']
    #return render(request, 'honeytip.html', {'tips': tips})
        if options == "1":
                #tips = Tip.objects.order_by('-pub_date')
                tips = Tip.objects.filter(group="귀차니즘").order_by('-pub_date')
                return render(request, 'honeytip.html', {'tips': tips})
        elif options == "2":
                tips = Tip.objects.filter(group="시간절약").order_by('-pub_date')
                return render(request, 'honeytip.html', {'tips': tips})
        else:
                tips = Tip.objects.filter(group="폭풍간지").order_by('-pub_date')
                return render(request, 'honeytip.html', {'tips': tips})
    else:
        tips = Tip.objects.order_by('-pub_date')
        return render(request, 'honeytip.html', {'tips': tips})


#def tipresult(request):
#    tips = Tip.objects
#    category = id 어떻게 받아오는지request.GET.get('query','')
#    if query:
#        tips = tips.filter(group_contains=query).order_by('-pub_date')
#        return render(request, 'honeytip.html', {'tips': tips})


#서치기능
#def result(request):
#    post_object = Market.objects
#    query = request.GET.get('query','')
#    if query:
#        post_object = post_object.filter(title__contains=query).order_by('-pub_date')
#        return render(request, 'result.html', {'result':post_object})


#def honeytip(request):
#    tips = Tip.objects
#    return render(request, 'honeytip.html', {'tips': tips})

def suggestnew(request):
        return render(request, 'suggest.html')



def suggestcreate(request):
        if request.method =='POST': # POST 방식으로 요청이 들어왔을 때
                form = SuggestForm(request.POST) # 입력된 내용들을 form이라는 변수에 저장
                if form.is_valid(): # form이 유효하다면(models.py에서 정의한 필드에 적합하다면)
                        post = form.save(commit=False) # form 데이터를 가져온다.
                        post.save() # form 데이터를 DB에 저장한다.
                        return redirect('honeytip')
        else: # GET 방식으로 요청이 들어왔을 때
                form = SuggestForm()
                return render(request,'suggest.html', {'form': form})
