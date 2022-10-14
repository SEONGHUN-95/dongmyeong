from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib import messages
from django.db.models import Count
from .models import Menu
from .forms import MenuForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def index(request):
    page = request.GET.get('page','1')
    menu_list = Menu.objects.order_by('date')
    pagiator = Paginator(menu_list, 7)
    page_obj = pagiator.get_page(page)
    context = {'menu_list' : page_obj}
    return render(request, 'menu/menu_list.html', context)

@login_required(login_url='accounts:login')
def menu_create(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        print('form', form)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.author = request.user
            menu.save()
            return redirect('menu:index')
    else:
        form = MenuForm()
    context = {'form': form}
    return render(request, 'menu/menu_form.html', context)

#베스트 메뉴 불러오기
def get_best_menu(request):
    menu_list = Menu.objects.annotate(voter_count=Count('voter')).order_by('-voter_count')
    best_list = menu_list[0:3]
    context = {'best_list':best_list}
    return render(request, 'menu/best_menu.html', context)

#메뉴 추천 버튼 구현
@login_required(login_url='accounts:login')
def menu_vote(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    menu.voter.add(request.user)
    return redirect('menu:index')

def setDate(request):
    date = request.GET.get('date') # HTML에서 받아온 date 값
    if date =='':
        messages.warning(request, '날짜 입력하세요')
    else:
        dateformat = "%Y-%m-%d" # str로 받아온 값 변환을 위한 포맷
        datedate = datetime.strptime(date, dateformat) # datetime 형으로 변환
        end_date = datedate + timedelta(days=3) # 기준일로부터 3일 뒤까지 설정
        strend_date = end_date.strftime(dateformat) #다시 str로 변환
        menu_list = Menu.objects.filter(date__range=(date,strend_date)) # 기준일+3일까지의 데이터 필터링
        context = {'menu_list' : menu_list}
        return render(request, 'menu/menu_list.html', context)
    return redirect('menu:index')