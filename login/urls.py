from django.urls import path


#vistas
from . import views
urlpatterns = [
    path('',views.login, name='login'),
    path('login',views.login_user, name='login'),
    path('logout',views.logout_user, name='logout')
]