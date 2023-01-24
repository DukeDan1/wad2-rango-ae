from django.urls import path
from rango import views
from django.urls import include
from django.contrib import admin

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('rango/', include('rango.urls')),
    path('admin/', admin.site.urls)
]