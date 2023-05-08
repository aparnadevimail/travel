from.import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    # path('',views.demoo,name='demoo'),
    # path('about/',views.about,name='about'),
]