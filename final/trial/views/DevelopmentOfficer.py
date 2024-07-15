from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.shortcuts import render, redirect
from ..forms import *
from django.contrib.auth.hashers import make_password, check_password
from ..SMS import send_sms
from django.http import HttpResponseNotFound
from django.contrib import messages
from ..models.accont_model import *
from login_history.models import LoginHistory
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

def development_officer_dashboard(request):
    group_count = Group.objects.count()
    return render(request, 'development_officer/dashboard.html', {'group_count': group_count})


def register_group(request):
    if request.method == 'POST':
        group_name = request.POST.get('name')
        description = request.POST.get('description')
        group_account = request.POST.get('group_account')
        village_id = request.POST.get('village')
        total_members = request.POST.get('total_members')
        group_no = request.POST.get('group_no')
        constitution_file = request.FILES.get('constitution')  # Retrieve uploaded file

        # Validate inputs
        if not group_name or not description or not group_account or not total_members:
            messages.error(request, "All fields are required.")
            return render(request, 'development_officer/register_group.html')

        try:
            total_members = int(total_members)
            if total_members < 0:
                raise ValueError("Total members cannot be negative.")
        except ValueError:
            messages.error(request, "Total members must be a valid integer.")
            return render(request, 'development_officer/register_group.html')

        try:
            village = Village.objects.get(pk=village_id)
        except Village.DoesNotExist:
            messages.error(request, "Village not found.")
            return render(request, 'development_officer/register_group.html')

        # Create and save the new group with the uploaded constitution
        new_group = Group(
            name=group_name,
            group_no=group_no,
            description=description,
            group_account=group_account,
            total_members=total_members,
            village=village,
            constitution=constitution_file,  # Add the constitution file
        )
        new_group.save()
        group_account = GroupAccount(
            group=new_group,
            balance=0
        )
        group_account.save()

        messages.success(request, "Group registered successfully!")
        return redirect('group_search')

    villages = Village.objects.all()  # For populating the village select box
    return render(request, 'development_officer/register_group.html', {'villages': villages})


def group_delete(request, pk):
    groups_list = Group.objects.filter(id=pk)
    if request.method == 'POST':
        groups_list.delete()
        return redirect('group_search')
    return render(request, 'development_officer/group_delete.html', {'groups_list': groups_list})


def group_search(request):
    query = request.GET.get('q')
    groups_list = Group.objects.all()

    if query:
        groups_list = groups_list.filter(name__icontains=query)

    # Order the queryset by a specific field
    groups_list = groups_list.order_by('name')

    # Pagination
    paginator = Paginator(groups_list, 2)
    page_number = request.GET.get('page')
    try:
        groups = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        groups = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results
        groups = paginator.page(paginator.num_pages)

    return render(request, 'development_officer/group_search.html', {'groups': groups})


def login_history(request):
    # Retrieve login history data
    login_history = LoginHistory.objects.all()  # You may want to filter this data based on user ID or other criteria

    # Render template with login history data
    return render(request, 'development_officer/login_history.html', {'login_history': login_history})


def download_constitution(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if group.constitution:
        file_path = group.constitution.path
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=' + group.constitution.name
            return response
    else:
        return HttpResponse("No constitution available.")

# views.py
def register_member(request):
    if request.method == 'POST':
        # Extract the data from the POST request
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        sex = request.POST.get('sex')
        group_id = request.POST.get('group_id')  # ID of the group the member will join
        position = request.POST.get('position')  # Member's position in the group

        # Set a default password if not provided
        password =  '123456789'  # Default password is '123456789'
        hash_password = make_password(password)

        # Check if all required fields are provided
        if not (username and first_name and group_id and position and phone):
            messages.error(request, "Please provide all required information.")
            return render(request, 'development_officer/register_member.html')

        # Format the phone number to include country code (255)
        if phone.startswith('0'):
            phone = '255' + phone[1:]  # Assuming '0' is the country code for Tanzania

        # Validate phone number format
        if not phone.startswith('255') or not phone[3:].isdigit() or len(phone) != 12:
            messages.error(request, "Please provide a valid phone number.")
            return render(request, 'development_officer/register_member.html')

        # Create a new User instance
        user = User.objects.create_user(
            username=username,
            password=hash_password,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        # Create a new Profile instance
        profile = Profile(
            user=user,
            phone=phone,
            sex=sex,
            role='member',  # Default role for a new member
        )
        profile.save()  # Save the profile to the database

        # Retrieve the Group instance
        try:
            group = Group.objects.get(pk=group_id)
        except Group.DoesNotExist:
            messages.error(request, "Group not found.")
            return render(request, 'development_officer/register_member.html')

        # Create and save the new Member instance
        new_member = Member(
            profile=profile,
            group=group,
            position=position,
        )
        new_member.save()  # Save the new member to the database
        user_id = user.pk

        # Send SMS to the newly registered user
        sms_message = f"Welcome to our platform! by visting to rfms Your username is: {username}, and your password is: {password}."
        recipients = [{"user_id": user_id, "dest_addr": phone}]
        response = send_sms(phone, sms_message)  # Pass the recipient's username as the recipient

        if "Error" in response:
            messages.error(request, "Member registered but failed to send SMS.")
        else:
            messages.success(request, "Member registered successfully and SMS sent!")

        return redirect('member_list', group_id=group.id)  # Redirect to a page with the list of members

    # If GET request, render the registration form
    groups = Group.objects.all()  # Fetch all groups for the dropdown
    return render(request, 'development_officer/register_member.html', {'groups': groups})


def list_group_members(request, group_id):
    try:
        group = Group.objects.get(pk=group_id)  # Retrieve the group by ID
    except Group.DoesNotExist:
        return HttpResponseNotFound("Group not found")  # Return 404 if group not found

    members = Member.objects.filter(group=group)  # Fetch all members in the group
    return render(request, 'development_officer/group_members_list.html', {'group': group, 'members': members})


def register_member(request):
    if request.method == 'POST':
        # Extract the data from the POST request
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        sex = request.POST.get('sex')
        group_id = request.POST.get('group_id')  # ID of the group the member will join
        position = request.POST.get('position')  # Member's position in the group

        # Set a default password if not provided
        password =  '123456789'  # Default password is '123456789'
        hash_password = make_password(password)

        # Check if all required fields are provided
        if not (username and first_name and group_id and position and phone):
            messages.error(request, "Please provide all required information.")
            return render(request, 'development_officer/register_member.html')

        # Format the phone number to include country code (255)
        if phone.startswith('0'):
            phone = '255' + phone[1:]  # Assuming '0' is the country code for Tanzania

        # Validate phone number format
        if not phone.startswith('255') or not phone[3:].isdigit() or len(phone) != 12:
            messages.error(request, "Please provide a valid phone number.")
            return render(request, 'development_officer/register_member.html')

        # Create a new User instance
        user = User.objects.create_user(
            username=username,
            password=hash_password,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        # Create a new Profile instance
        profile = Profile(
            user=user,
            phone=phone,
            sex=sex,
            role='member',  # Default role for a new member
        )
        profile.save()  # Save the profile to the database

        # Retrieve the Group instance
        try:
            group = Group.objects.get(pk=group_id)
        except Group.DoesNotExist:
            messages.error(request, "Group not found.")
            return render(request, 'development_officer/register_member.html')

        # Create and save the new Member instance
        new_member = Member(
            profile=profile,
            group=group,
            position=position,
        )
        new_member.save()  # Save the new member to the database
        user_id = user.pk

        # Send SMS to the newly registered user
        sms_message = f"Welcome to our platform! by visting to rfms Your username is: {username}, and your password is: {password}."
        recipients = [{"user_id": user_id, "dest_addr": phone}]
        response = send_sms(phone, sms_message)  # Pass the recipient's username as the recipient

        if "Error" in response:
            messages.error(request, "Member registered but failed to send SMS.")
        else:
            messages.success(request, "Member registered successfully and SMS sent!")

        return redirect('member_list', group_id=group.id)  # Redirect to a page with the list of members

    # If GET request, render the registration form
    groups = Group.objects.all()  # Fetch all groups for the dropdown
    return render(request, 'development_officer/register_member.html', {'groups': groups})
