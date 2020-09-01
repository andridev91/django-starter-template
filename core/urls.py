from django.urls import path

from . import views


app_name = 'core'
urlpatterns = [
    path('', views.RootView.as_view(), name='root'),
]
