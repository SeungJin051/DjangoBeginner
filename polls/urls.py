from django.urls import path

from . import views

# 앱 네임 추가
app_name = 'polls'

urlpatterns = [
    path("", views.index, name="index"),
    # ex : polls/5/ | question_id를 받는 path 현재 10을 받아주는 코드
    path("<int:question_id>/", views.detail, name="detail"),
    # ex : polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex : polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="ç"),

]