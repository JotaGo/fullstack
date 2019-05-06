"""techk URL Configuration

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
from apps.base.views import index
from apps.scraper import views  


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'scraper/', views.index, name='scraper_b'),
    url(r'executing/', views.execute, name='exec_scraper'),
    url(r'categorys/([0-9]+)/([0-9]+)/', views.book_delete, name='delete'),
    url(r'categorys/([0-9]+)/', views.book_list, name='books'),
    url(r'categorys/', views.category_list, name='categorias'),
    url(r'', index),
    url(r'^api-auth/', include('rest_framework.urls'))
]