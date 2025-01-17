from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .form import SignUpForm, AddRecordForm
from .models import Record


def home(request):
    records=Record.objects.all()
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You are logged in")
            return redirect('home')
        else:
            messages.success(request,"Error logging in. Please try again")
            return redirect('home')
    else:
        return render(request,'home.html',{'records':records})


# def login_user(request):
#     pass


def logout_user(request):
    logout(request)
    messages.success(request,"you have been logged out")
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})



def customer_record(request,pk):
    if request.user.is_authenticated:
        record= Record.objects.get(id=pk)
        return render(request,'record.html',{'record':record})
    else:
        messages.success(request,"You must be logged in.")
        return redirect('home')
    

def delete_record(request,pk):

    if request.user.is_authenticated:
        delete= Record.objects.get(id=pk)
        delete.delete()
        messages.success(request,"Record deleted successfully")
        return redirect('home')
    else:
        messages.success(request,"You must be logged in.")
        return redirect('home')



def add_record(request):
    form= AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                add_record=form.save()
                messages.success(request,"Record Added...")
                return redirect('home')
        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request,"You must be logged in")
        return redirect('home')

def update_record(request,pk):
    if request.user.is_authenticated:
        record= Record.objects.get(id=pk)
        form= AddRecordForm(request.POST or None, instance=record)
        if form.is_valid():
            add_record=form.save()
            messages.success(request,"Record Updated...")
            return redirect('home')
        return render(request,'update_record.html',{'form':form})
    else:
        messages.success(request,"You must be logged in")
        return redirect('home')