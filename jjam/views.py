from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseNotAllowed
from django.db.models import Q, Count
from django.contrib import messages


from .models import Question
from .models import QuestionCount
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def index(request):
    page = request.GET.get('page','1')
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so','recent')
    #정렬
    if so == "recommend":
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    elif so == 'recent':
        question_list = Question.objects.order_by('-create_date')
    else:
        question_list = Question.objects.order_by('-view_count')
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    pagiator = Paginator(question_list, 10)
    page_obj = pagiator.get_page(page)
    context = {'question_list' : page_obj, 'page':page, 'kw':kw}
    return render(request, 'jjam/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'jjam/question_detail.html', context)

@login_required(login_url='accounts:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('jjam:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'jjam/question_form.html', context)

@login_required(login_url='accounts:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method =="POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('jjam:detail', question_id = question.id)
    else:
        return HttpResponseNotAllowed('plz Login')
    context = {'question': question, 'form':form}
    return render(request, 'jjam/question_detail.html',context)
    
@login_required(login_url='accounts:login')
def question_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인의 게시물을 추천할 수는 없습니다.')
    else:
        question.voter.add(request.user)
    return redirect('jjam:detail', question_id=question.id)

@login_required(login_url='accounts:login')
def answer_vote(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인의 게시물을 추천할 수는 없습니다.')
    else:
        answer.voter.add(request.user)
    return redirect('jjam:detail', answer_id=answer.id)

