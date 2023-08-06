from django.shortcuts import render, redirect
from .models import expense
from django.http import Http404
from rest_framework.decorators import api_view
from django.contrib import messages

# Create your views here.
@api_view(['GET','POST'])
def expense_list(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        description = request.POST.get('description')

        existing_expense = expense.objects.filter(name=name, amount=amount, date=date, description=description).first()
        if not existing_expense:
            new_expense = expense(id=id,name=name, amount=amount, date=date, description=description)
            new_expense.save()
     
    expenses = expense.objects.all()
    return render(request, 'expense_list.html', {'expenses':expenses})


def expense_delete(request,pk):
    try:
        expenses = expense.objects.get(pk=pk)
    except expense.DoesNotExist:
        raise Http404('expense not found')
    if request.method == 'POST':
        expenses.delete()
        messages.success(request, 'expense deleted successfully')
        return redirect('expense-list')


def expense_update(request,pk):
    expenses = expense.objects.get(pk=pk)
    expenses.name = request.POST.get('name')
    expenses.amount = request.POST.get('amount')
    expenses.date = request.POST.get('date')
    expenses.description = request.POST.get('description')
    expenses.save()
    return redirect('expense-list')