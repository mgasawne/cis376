from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile, PostBox, Comment
from .forms import PostBoxForm, CommentForm

# Home view


def home(request):
    try:
        posts = PostBox.objects.all()  # Fetch all posts
        print("Posts fetched:", posts)  # Debugging line
    except PostBox.DoesNotExist:
        posts = []  # Default to an empty list if there are no posts
    except Exception as e:
        messages.error(request, f"An error occurred: {e}")
        posts = []  # Default to an empty list in case of unexpected errors

    return render(request, 'home.html', {"posts": posts})

# Profile list view


def profile_list(request):
    try:
        profiles = Profile.objects.all()  # Fetch all profiles
        return render(request, 'profile_list.html', {"profiles": profiles})
    except Profile.DoesNotExist:
        profiles = []  # Default to an empty list if there are no profiles
        messages.error(request, "No profiles found.")
        return render(request, 'profile_list.html', {"profiles": profiles})

# Profile detail view


def profile(request, pk):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user_id=pk)
        return render(request, "profile.html", {"profile": profile})
    else:
        messages.error(request, "Please log in to view this profile.")
        return redirect('login')

# Login view


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout view


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

# Signup view


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Create post view


def create_post(request):
    if request.method == 'POST':
        form = PostBoxForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, "Post created successfully.")
            return redirect('home')
        else:
            messages.error(request, 'Form is not valid.')
            print(form.errors)  # Debugging line to print form errors
    else:
        form = PostBoxForm()
    return render(request, 'create_post.html', {'form': form})

# Delete post view


def delete_post(request, pk):
    post = get_object_or_404(PostBox, pk=pk)
    if post.user == request.user:
        post.delete()
        messages.success(request, "Post deleted successfully.")
    else:
        messages.error(
            request, "You do not have permission to delete this post.")
    return redirect('home')

# Edit post view


def edit_post(request, pk):
    post = get_object_or_404(PostBox, pk=pk)
    if request.method == 'POST':
        form = PostBoxForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            # Redirect back to the homepage or another page after saving
            return redirect('home')
    else:
        form = PostBoxForm(instance=post)  # Pre-fill form with post data
    return render(request, 'edit_post.html', {'form': form, 'post': post})

# Comment View


def comment_post(request, pk):
    post = get_object_or_404(PostBox, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'comment_post.html', {'form': form, 'post': post})
