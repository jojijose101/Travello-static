from django.urls import path, include

from joapp import views

urlpatterns = [
    path('',views.index,name='index')
]
