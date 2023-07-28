from django.shortcuts import render
from .models import expense
from django.http import Http404

# Create your views here.

def expense_list(request):
    expenses = expense.objects.all()
    return render(request, 'expense_list.html', {'expense':expenses})

def expense_detail(request,pk):
    try:
        expense = expense.objects.get(pk=pk)
    except expense.DoesNotExist:
        raise Http404('expense not found')
    return render(request, 'templates/expense_detail.html', {'expense':expense})
