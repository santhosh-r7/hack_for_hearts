from django.contrib import admin
from django.urls import path ,  include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('indexsign/' , include('indexsign.urls')),
    path('movie_list/' , include('movie_list.urls')),
    path('signUP/' , include('signUP.urls')),
]



