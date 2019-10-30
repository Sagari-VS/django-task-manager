"""djangotest3 URL Configuration

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

from django.contrib import admin
from testapp3 import views
from django.conf.urls import url
from django.urls import include
from djangotest3.user_management import views as core_views

urlpatterns = [
    url('', views.home, name='home'),
    url('admin/', admin.site.urls),
    url('user_management/', include('user_management.urls')),
    url(r'^signup/$', core_views.signup, name='signup'),
    # url(r'^$', views.Hello()),
    #path('djangovirtu/', include('django.contrib.auth.urls')),
]
