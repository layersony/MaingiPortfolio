from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from mainsite import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', views.indexView, name='home'),
    # path('thankyou/', views.thankyouView, name='thankyou')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)