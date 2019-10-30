from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.http import HttpResponseRedirect

# Rest API
from rest_framework import routers
from mtasks.serializers import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)



urlpatterns = [
    url(r'^$', lambda r: HttpResponseRedirect('admin/')),   # Remove this redirect if you add custom views
    path('admin/', admin.site.urls),
    url(r'^advanced_filters/', include('advanced_filters.urls')),
    url(r'^api/v1/', include(router.urls)),
]

admin.site.site_header = settings.SITE_HEADER