from django.shortcuts import render,redirect
from .forms import User_form,User_info_form
from user_model.models import User_data,User_info
# Create your views here.

def User_input(request):
    if request.method == "POST":
        user_form = User_form(request.POST)
        user_info = User_info_form(request.POST)

        if user_form.is_valid() and user_info.is_valid():
            name = user_form.save()

            info = user_info.save(commit=False)
            info.user = name
            info.save()
            return redirect('home')
    else:
        user_form = User_form()
        user_info = User_info_form()
        return render(request,'input.html',{'user_form': user_form, 'user_info': user_info})


def home(request):
    users = User_info.objects.all()
    for obj in users:
        print(obj.dob)
    return render(request,'home.html',{'users':users})
