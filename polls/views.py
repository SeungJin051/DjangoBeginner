from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

def index(request):
    return render(request, 'polls/main.html')

def detail(request, question_id):
    return HttpResponse("질문 %s." % question_id)

def results(request, question_id):
    response =  "현재 질문의 결과는 %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("voting 질문 %s." % question_id)