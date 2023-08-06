from django.urls import path
from . import views

urlpatterns=[
    path('',views.expense_list, name='expense-list'),
    path('  <int:pk>/update/', views.expense_update, name='expense-update'),
    path('<int:pk>/delete/', views.expense_delete, name='expense-delete'),
]