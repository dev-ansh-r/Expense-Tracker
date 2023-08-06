from django.urls import path
from . import views

urlpatterns=[
    path('expense/',views.expense_list, name='expense-list'),
    path('expense/<int:pk>/update/', views.expense_update, name='expense-update'),
    path('expense/<int:pk>/delete/', views.expense_delete, name='expense-delete'),
]