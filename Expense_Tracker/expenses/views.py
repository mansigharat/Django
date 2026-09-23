from django.shortcuts import render,redirect
from .models import *

def expenses(request):
    if request.method=="POST":
        data = request.POST

        expense_name = data.get('expense_name')
        expense_amount = data.get('expense_amount')
        expense_category = data.get('expense_category')
        expense_date = data.get('expense_date')

        Expense.objects.create(
            name=expense_name,
            amount=expense_amount,
            category=expense_category,
            date=expense_date
        )
        
        return redirect('/expenses/')
    queryset = Expense.objects.all()

    context = {'expenses' : queryset}
    return render(request,'expense.html',context)

def update_expense(request,id):
    queryset = Expense.objects.get(id=id)

    if request.method == "POST":
        data=request.POST
        expense_name = data.get('expense_name')
        expense_amount = data.get('expense_amount')
        expense_category = data.get('expense_category')
        expense_date = data.get('expense_date')

        queryset.name = expense_name
        queryset.amount = expense_amount
        queryset.category = expense_category
        queryset.date = expense_date

        queryset.save()
        return redirect('/expenses/')

    context = {'expenses' : queryset}
    return render(request,'update_expense.html',context)
    


