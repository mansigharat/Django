from django.shortcuts import render,redirect
from .models import *
from django.db.models import Sum 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def expenses(request):
    if request.method=="POST":
        data = request.POST

        expense_name = data.get('expense_name')
        expense_amount = data.get('expense_amount')
        expense_category = data.get('expense_category')
        expense_date = data.get('expense_date')

        Expense.objects.create(
            user=request.user,
            name=expense_name,
            amount=expense_amount,
            category=expense_category,
            date=expense_date
        )
        
        return redirect('/expenses/')

    queryset = Expense.objects.filter(user=request.user)

    total_amount = Expense.objects.filter(user=request.user).aggregate(total = Sum('amount'))['total'] or 0

    context = {'expenses' : queryset , 'total_amount' : total_amount}

    return render(request,'expense.html',context)

@login_required(login_url="/login/")
def update_expense(request,id):
    queryset = Expense.objects.get(id=id,user=request.user)

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

@login_required(login_url="/login/")
def delete_expense(request,id):
    queryset=Expense.objects.get(id=id, user=request.user)
    queryset.delete()
    return redirect('/expenses/')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

                                   #username = "manasi"
        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid Username")
            return redirect('/login/')

        user = authenticate(username = username , password=password)
        if user is None:
            messages.error(request,"Invalid Password")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/expenses/')
    return render(request,'login_page.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username already exists")
            return redirect('')

        user = User.objects.create(
            first_name =  first_name,
            last_name = last_name,
            username = username,
        )

        user.set_password(password)
        user.save()
        messages.info(request, "Account Created Successfully")
        return redirect('')
    return render(request,'register.html')