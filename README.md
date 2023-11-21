# 파이썬 장고 웹프로그래밍

[Django Project docs](https://docs.djangoproject.com/en/4.2/intro/tutorial01/).

# 프로젝트 생성

django-admin startproject myproject .

# 초기 파일 설명

manage.py: 이 Django 프로젝트와 다양한 방식으로 상호 작용할 수 있게 해주는 명령줄 유틸리티입니다. django-admin 및manage.pymanage.py 에 대한 모든 세부 정보를 읽을 수 있습니다 . <br>
내부 mysite/디렉터리는 프로젝트의 실제 Python 패키지입니다. 이름은 그 안에 있는 항목을 가져오는 데 사용해야 하는 Python 패키지 이름입니다(예: mysite.urls). <br>
mysite/settings.py: 이 Django 프로젝트에 대한 설정/구성입니다. Django 설정은 설정이 어떻게 작동하는지 알려줍니다. <br>
mysite/urls.py: 이 Django 프로젝트에 대한 URL 선언입니다. Django 기반 사이트의 "목차"입니다. URL 디스패처 에서 URL에 대해 자세히 알아볼 수 있습니다. <br>
mysite/asgi.py: 프로젝트를 제공하기 위한 ASGI 호환 웹 서버의 진입점입니다. 자세한 내용은 ASGI를 사용하여 배포하는 방법을 참조하세요. <br>
mysite/wsgi.py: 프로젝트를 제공하기 위한 WSGI 호환 웹 서버의 진입점입니다. 자세한 내용은 WSGI를 사용하여 배포하는 방법을 참조하세요. <br>

# 개발 서버

python manage.py runserver (포트번호)

# CREATE APP

django-admin startapp (앱이름) <br>
프로젝트와 앱의 차이점은 무엇인가요? 앱은 블로그 시스템, 공공 기록 데이터베이스 또는 소규모 설문 조사 앱과 같은 작업을 수행하는 웹 애플리케이션입니다. 프로젝트는 특정 웹사이트에 대한 구성 및 앱의 모음입니다. 프로젝트에는 여러 앱이 포함될 수 있습니다. 앱은 여러 프로젝트에 있을 수 있습니다.
