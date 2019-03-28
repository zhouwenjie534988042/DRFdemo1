"""DRFdemo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter, SimpleRouter

from DRFdemo1 import settings
from stuapp import views
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='我的接口文档')),
    url(r'^', include('stuapp.urls')),
]


# router = DefaultRouter() #创建路由器对象
router = SimpleRouter() #创建路由器对象

# url(r'^actors/$', views.ActorListView.as_view()),
# url(r'^actors/(?P<pk>\d+)/$', views.ActorDetailView.as_view()),
router.register('actors', views.ActorListView, basename='actors')  # 向路由器中注册视图集
# router.register('movies', views.MovieListView, basename='movies')  # 向路由器中注册视图集

urlpatterns += router.urls

from django.conf.urls.static import static
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
