from django.shortcuts import render, redirect
from .forms import VideoForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required



# Create your views here.

def home(request):
    return render(request, 'home.html')




def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a specific page after successful login
            return redirect('home')
        else:
            # Handle invalid login credentials
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')



@login_required
def logout_view(request):
    if request.method == 'GET':
        return home



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
            return redirect('home')  # Redirect to home page after successful upload
    else:
        form = VideoForm()
       
    return render(request, 'video_upload.html', {'form': form,'user': user})
