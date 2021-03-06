"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path("page/", include("page.urls")),  # page라는 주소로 들어오면, page.urls에서 처리
    # 기본 주소로 들어오면, page/로 보냄
    path("", RedirectView.as_view(url="/page/", permanent=True)),

]

# jsp, css, image 파일 등의 정적 파일 처리 가능
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
