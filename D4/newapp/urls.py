from django.urls import path
from .views import NewList
from django.conf.urls import url

urlpatterns = [
    path('', NewList.as_view()),
    url(r'^user_list$', user_list),

]
