from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return HttpResponse("main index")

# 요청, 예외
def error_404_view(request, exception):
    return HttpResponseNotFound("페이지 찾을 수 없음 404!")