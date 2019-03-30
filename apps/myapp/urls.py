
from django.urls import path

from myapp.views.api_views import *
from myapp.views.user_views import *

app_name = 'myapp'

urlpatterns = [
    path('log/',login,name='log'),
    path('reg/',register,name='reg'),
    path('mine/',mine,name='mine'),
    path('louout/',louout,name='louout'),
    path('index/',index),
    path('update_order/',update_order),
    path('pay_result/',pay_result)
]
