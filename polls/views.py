from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list' : latest_question_list, }
    #output = ', '.join([q.question_text for q in latest_question_list])
    #httpresponse활용하여 출력하기
    #return HttpResponse(template.render(context, request))
    #render함수 활용하여 출력하기.
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #404 error 처리
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question' : question})
    #return HttpResponse("당신은 지금 질문을 보고 있습니다. %s ." %question_id)

def results(request, question_id):
    response = "당신은 지금 질문의 결과를 보고 있습니다. %s ."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("당신은 지금 질문에 투표중입니다. %s" % question_id)


# Create your views here.
