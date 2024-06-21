from django.shortcuts import render, redirect, HttpResponse
from .forms import VideoForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.

def home(request):
    return render(request, 'home.html')




def login_view(request):
    # if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"Successfully loged in")

            return redirect('user_home')
        else:            
            messages.success(request,"Invalid username or password")

            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    # else:
    #     return HttpResponse("404 - not found")



@login_required
def logout_view(request):
    # if request.method == 'POST':
        logout(request)
        messages.success(request,"Successfully loged out'")

        return redirect('home')
    # else:
    #     return HttpResponse("404 - not found")





@login_required
def user_home(request):
    user = request.user  # Access the currently logged-in user
    return render(request, 'home.html', {'user': user})




@login_required
def video_upload(request):
    user = request.user.username
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user_home')  # Redirect to home page after successful upload
    else:
        form = VideoForm()
       
    return render(request, 'video_upload.html', {'form': form,'user': user})
