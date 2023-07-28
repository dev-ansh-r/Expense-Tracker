from django.urls import path
from . import views

urlpatterns=[
    path('expense/',views.expense_list, name='expense-list'),
    path('expense/<int:pk>/', views.expense_detail, name='expense-detail'),
]