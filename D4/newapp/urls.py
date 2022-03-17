from django.urls import path
from .views import NewList, NewDetailView, NewCreateView, NewUpdateView, NewDeleteView


urlpatterns = [
    path('', NewList.as_view()),
    path('<int:pk>/', NewDetailView.as_view(), name='new_detail'),  # Ссылка на детали товара
    path('create/', NewCreateView.as_view(), name='add'),  # Ссылка на создание товара
    path('create/<int:pk>', NewUpdateView.as_view(), name='add'),
    path('delete/<int:pk>', NewDeleteView.as_view(), name='new_delete'),
]
