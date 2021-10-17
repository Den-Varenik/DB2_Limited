from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),
    url(r'^api/chat/', include('chat.api.urls'))
]
