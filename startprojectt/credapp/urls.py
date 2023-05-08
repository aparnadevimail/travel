from.import views
from django.urls import path

urlpatterns = [
    path('Register',views.Register,name='Register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
]