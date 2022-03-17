from django.urls import path
from .views import NewList, user_list
#from django.conf.urls import url   # <--- Пачиму

urlpatterns = [
    path('', NewList.as_view()),
    #url(r'^user_list$', user_list),
]
