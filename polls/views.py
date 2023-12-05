from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

def index(request):
    ctx = {
        "greetings" : "Hello there",
        "location" : {
            "city" :"Busan",
            "country" : "South Korea"
        },
        "languages" : ["Korean", "English"]
    }
    return render(request, 'polls/main.html', context=ctx)

def detail(request, question_id):
    return HttpResponse("질문 %s." % question_id)

def results(request, question_id):
    response =  "현재 질문의 결과는 %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("voting 질문 %s." % question_id)