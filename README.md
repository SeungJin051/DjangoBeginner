# 파이썬 장고 웹프로그래밍

[Django Project docs](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)

# 프로젝트 생성

```
django-admin startproject myproject .
```

# 초기 파일 설명

<ul>
  <li>manage.py: 이 Django 프로젝트와 다양한 방식으로 상호 작용할 수 있게 해주는 명령줄 유틸리티입니다. django-admin 및manage.pymanage.py 에 대한 모든 세부 정보를 읽을 수 있습니다.</li>
  <li>내부 mysite/디렉터리는 프로젝트의 실제 Python 패키지입니다. 이름은 그 안에 있는 항목을 가져오는 데 사용해야 하는 Python 패키지 이름입니다(예: mysite.urls).</li>
  <li>mysite/settings.py: 이 Django 프로젝트에 대한 설정/구성입니다. Django 설정은 설정이 어떻게 작동하는지 알려줍니다.</li>
  <li>mysite/urls.py: 이 Django 프로젝트에 대한 URL 선언입니다. Django 기반 사이트의 "목차"입니다. URL 디스패처 에서 URL에 대해 자세히 알아볼 수 있습니다.</li>
  <li>mysite/asgi.py: 프로젝트를 제공하기 위한 ASGI 호환 웹 서버의 진입점입니다. 자세한 내용은 ASGI를 사용하여 배포하는 방법을 참조하세요.</li>
  <li>mysite/wsgi.py: 프로젝트를 제공하기 위한 WSGI 호환 웹 서버의 진입점입니다. 자세한 내용은 WSGI를 사용하여 배포하는 방법을 참조하세요.</li>
</ul>

# 개발 서버

```
python manage.py runserver (포트번호)
```

# CREATE APP

```
django-admin startapp (앱이름)
```

프로젝트와 앱의 차이점은 무엇인가요? 앱은 블로그 시스템, 공공 기록 데이터베이스 또는 소규모 설문 조사 앱과 같은 작업을 수행하는 웹 애플리케이션입니다. 프로젝트는 특정 웹사이트에 대한 구성 및 앱의 모음입니다. 프로젝트에는 여러 앱이 포함될 수 있습니다. 앱은 여러 프로젝트에 있을 수 있습니다.

# 1.
<ul>
  <li>urls - 사이트에 어디에 있는지 파싱을 하고 뷰에 연결하여 라우팅 역할 (path_converters, re_path)</li>
  <li>views - What to Show, 비지니스 로직 (함수 베이스 뷰 -> 간단하지만 반복되는 코드가 많아짐, 클래스 베이스 뷰 -> 반복되는 코드가 적고, CRUD 효과적)</li>
  <li>404 URL NOT FOUND - handler404 변수로 urls.py를 설정, 에러시 디버그 로그들이 모두 보여 해킹의 위험 -> DEBUG = False, ALLOWED_HOSTS=['*']</li>
  <li>302 REDIRECT - 어떤 url에서 다른 url로 다시 바꾸는 것, HttpResponseRedirect(), </li>
  <li>Reverse URL(더 알아보기) - path -> name은 템플릿 연결</li>
</ul>

Templates 템플릿 - Syntax는 Jinja2, Load HTML, CSS, JS
