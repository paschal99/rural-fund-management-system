from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..forms import *
from django.contrib import messages
from ..models.accont_model import *
from ..models.user_model import *
from django.contrib.auth import get_user_model

User = get_user_model()


def registration(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            if User.objects.filter(username=username).exists():
                # User with the same username already exists
                message = "User with the same username already exists."
                return render(request, 'register.html', {'form': form, 'message': message})
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=form.cleaned_data['password'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name']
                )
                profile = Profile.objects.create(
                    user=user,
                    phone=form.cleaned_data['phone'],
                    sex=form.cleaned_data['sex'],
                    role='member'
                )
                group = form.cleaned_data['group']
                member = Member.objects.create(

                    profile=profile,
                    group=group
                )
                user = authenticate(username=username, password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('login')  # Redirect to login page after successful registration
    return render(request, 'register.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to dashboard based on user role
                if user.profile.role == 'Development-Officer':
                    return redirect('development_officer_dashboard')
                elif user.profile.role == 'member':
                    return redirect('member_dashboard')
                elif user.profile.role == 'Administrative-Secretary':
                    return redirect('administrative_secretary_dashboard')
            else:
                # Invalid login credentials
                return render(request, 'login.html', {'form': form, 'message': 'Invalid username or password'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')
#
#
# @login_required(login_url='login')
# def update_member_details(request):
#     # Fetch the current user's profile
#     profile = Profile.objects.get(user=request.user)
#
#     if request.method == 'POST':
#         form = MemberUpdateForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('member_dashboard')  # Redirect to member dashboard after updating details
#     else:
#         form = MemberUpdateForm(instance=profile)
#
#     return render(request, 'update_member_details.html', {'form': form})

@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')

            # Redirect based on user role
            if request.user.profile.role == 'Development-Officer':
                return redirect('development_officer_dashboard')
            elif request.user.profile.role == 'member':
                return redirect('member_dashboard')
            elif request.user.profile.role == 'Administrative-Secretary':
                return redirect('administrative_secretary_dashboard')
            else:
                return redirect('index')  # Fallback redirect if role is not matched
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)

    # Set the dashboard template based on user's role
    if request.user.profile.role == 'member':
        dashboard_template = 'member/member_dashboard.html'
    elif request.user.profile.role == 'Development-Officer':
        dashboard_template = 'development_officer/dashboard.html'
    elif request.user.profile.role == 'Administrative-Secretary':
        dashboard_template = 'administrative_secretary/dashboard.html'
    else:
        # Default to member dashboard if role is not recognized
        dashboard_template = 'member/member_dashboard.html'

    return render(request, 'administrative_secretary/change_password.html', {'form': form, 'dashboard_template': dashboard_template})

@login_required
def display_user_info(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'user_info.html', {'profile': profile})

@login_required
def update_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        # Get data from the form
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        sex = request.POST.get('sex')
        # role = request.POST.get('role')

        # Update User model
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        # Update Profile model
        profile.phone = phone
        profile.sex = sex
        # profile.role = role
        profile.save()

        # Redirect to the appropriate dashboard based on role
        if profile.role == 'member':
            return redirect('member_dashboard')
        elif profile.role == 'Development-Officer':
            return redirect('development_officer_dashboard')
        elif profile.role == 'Administrative-Secretary':
            return redirect('administrative_secretary_dashboard')

    # Set the dashboard template based on user's role
    if profile.role == 'member':
        dashboard_template = 'member/member_dashboard.html'
    elif profile.role == 'Development-Officer':
        dashboard_template = 'development_officer/dashboard.html'
    elif profile.role == 'Administrative-Secretary':
        dashboard_template = 'administrative_secretary/dashboard.html'
    else:
        # Default to member dashboard if role is not recognized
        dashboard_template = 'member/member_dashboard.html'

    context = {
        'user': user,
        'profile': profile,
        'dashboard_template': dashboard_template,
    }

    # Add a success message
    messages.success(request, 'Your profile has been successfully updated!')

    return render(request, 'update_profile.html', context)

