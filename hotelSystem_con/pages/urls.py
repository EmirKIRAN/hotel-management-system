from django.urls import path
from . import views
from  pages.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register")
]