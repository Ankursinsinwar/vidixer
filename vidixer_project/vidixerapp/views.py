from django.shortcuts import render, redirect, HttpResponse
from .forms import VideoForm
from django.contrib import messages
from django.contrib.auth.models import User
# from rest_framework import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Video



# Create your views here.

def home(request):
    return render(request, 'home.html')



def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



# def login_view(request):
#     # if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request,"Successfully loged in")

#             return redirect('user_home')
#         else:            
#             messages.success(request,"Invalid username or password")

#             return render(request, 'login.html', {'error_message': 'Invalid username or password'})
#     # else:
#     #     return HttpResponse("404 - not found")



def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST["username"],
                            password=request.POST["password"])
        if user:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('user_home')
        else:
            messages.success(request,"Invalid username or password")
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    return render(request, 'login.html')


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
# def upload_video(request):
#     if request.method == 'POST':
#         print("post")
#         form = VideoForm( request.POST, request.FILES,)
#         print("ki")
#         if form.is_valid():
#             print("valid")
#             video = form.save(commit=False)
#             video.uploaded_by = request.user
#             video.save()
#             print("save")
#             return redirect('vedio_decription')  # Redirect to a success page
#         else:
#             print(form.errors)
#     else:
#         form = VideoForm(initial={'uploaded_by': request.user})
#         print(request.user)
#     return render(request, 'video_upload.html', {'form': form})
@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.uploaded_by = request.user  # Set uploaded_by here
            video.save()
            return redirect('vedio_decription')  # Redirect to a success page
        else:
            print(form.errors)
    else:
        form = VideoForm()
    return render(request, 'video_upload.html', {'form': form})



@login_required
def vedio_decription(request):
    # Fetch all videos uploaded by the current user
    videos = Video.objects.filter(uploaded_by=request.user)
    context = {
        'videos': videos
    }
    return render(request, 'vedio_decription.html', context)





# class VideoSerializer (serializers.ModelSerializer):
#     class Meta:
#         model = Video
#         fields = ['title', 'description', 'uploaded_by', 'video_file']
#         extra_kwargs = {"author": { "read_only": True}}