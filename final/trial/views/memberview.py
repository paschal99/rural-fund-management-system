from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from ..models.accont_model import *
from django.shortcuts import render, redirect
from ..models.user_model import *
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from django.contrib import messages
import qrcode
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import base64
from io import BytesIO
from django.db.models import F, Sum
from django.http import HttpResponse
from decimal import Decimal
from datetime import timedelta
from django.utils import timezone
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from datetime import datetime, timedelta


def calculate_remaining_time(request):
    """Calculate the time difference between now and a given end date."""
    now = timezone.now()  # Timezone-aware current time

    # If end_date is naive, make it timezone-aware
    if timezone.is_naive(end_date):
        end_date = timezone.make_aware(end_date)

    if end_date > now:
        remaining_time = end_date - now  # Calculate the timedelta
        days = remaining_time.days
        total_seconds = remaining_time.seconds
        hours = total_seconds // 3600  # Extract hours from seconds
        minutes = (total_seconds % 3600) // 60  # Extract minutes from remaining seconds
        seconds = total_seconds % 60  # Extract seconds from the remainder
        return {'days': days, 'hours': hours, 'minutes': minutes, 'seconds': seconds}
    else:
        return None

# View function using timezone-aware calculations
@login_required(login_url='/login/')
def member_dashboard(request):
    # Get the member associated with the logged-in user
    member = Member.objects.filter(profile__user=request.user).first()

    if not member:
        messages.error(request, "You do not belong to any group.")
        return redirect("login")

    group = member.group

    # Get the group's transactions
    transactions = DISTRICT_TRANSACTION.objects.filter(destination_account=group)

    # Get the group's loan schedule
    loan_schedule = LoanSchedule.objects.filter(group=group).first()

    group_acount = GroupAccount.objects.filter(group=group).aggregate(Sum('balance'))['balance__sum']
    remaining_time_details = None
    end_date_iso = None  # ISO formatted end date for JavaScript

    if loan_schedule and not loan_schedule.returned:
        end_date = loan_schedule.end_date

        # Make sure the end date is timezone-aware
        if timezone.is_naive(end_date):
            end_date = timezone.make_aware(end_date)

        # Calculate the remaining time components
        remaining_time = end_date - timezone.now()
        days = remaining_time.days
        hours = (remaining_time.seconds // 3600)
        minutes = (remaining_time.seconds % 3600) // 60
        seconds = (remaining_time.seconds % 60)

        remaining_time_details = {
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        }

        # Convert end date to ISO format for JavaScript
        end_date_iso = end_date.isoformat()

    penalty = Decimal(0)
    if loan_schedule and not loan_schedule.returned and timezone.now() > loan_schedule.end_date:
        penalty = loan_schedule.calculate_penalty()

    return render(request, 'member/member_dashboard.html', {
        'group': group,
        'group_acount': group_acount,
        'transactions': transactions,
        'loan_schedule': loan_schedule,
        'remaining_time_details': remaining_time_details,
        'penalty': penalty,
        'end_date_iso': end_date_iso,
        # Pass ISO formatted date for JS
    })


@login_required
def refund_fund(request, district_transaction_id):
    # Ensure the user is logged in and retrieve their member profile
    member = get_object_or_404(Member, profile=request.user.profile)

    # Retrieve the district transaction based on the provided ID
    district_transaction = get_object_or_404(DISTRICT_TRANSACTION, id=district_transaction_id)

    # Check if the member belongs to a group, if not, deny access
    if not member.group:
        return HttpResponse("Unauthorized", status=403)

    if request.method == "POST":
        # Retrieve the refund amount from the POST data
        refund_amount_str = request.POST.get("amount")

        try:
            # Convert the refund amount to a Decimal
            refund_amount = Decimal(refund_amount_str)
        except (ValueError, TypeError):
            # If the amount is not a valid number, set an error message
            messages.error(request, "<h6>Invalid refund amount.</h6>")
            return redirect('refund_fund', district_transaction_id=district_transaction_id)

        # Check if the refund amount is within valid bounds
        if refund_amount <= 0 or refund_amount > district_transaction.amount:
            # If the amount is invalid, set an error message
            messages.error(request, "Invalid refund amount.")
            return redirect('refund_fund', district_transaction_id=district_transaction_id)

        # Retrieve the group account associated with the member's group
        group_account = get_object_or_404(GroupAccount, group=member.group)

        # Create a return transaction for the refund
        return_transaction = ReturnTransaction.objects.create(
            member=member,
            amount=refund_amount,
            group_account=group_account,
            district_transaction=district_transaction,
        )

        # Update account balances: reduce group account balance, increase district account balance
        group_account.balance -= refund_amount
        group_account.save()

        district_transaction.from_account.balance_amount += refund_amount
        district_transaction.from_account.save()

        # Check if the returned amount matches the loan schedule's amount
        loan_schedule = LoanSchedule.objects.filter(group=member.group).first()
        if loan_schedule:
            loan_schedule.returned = True  # Mark as returned
            loan_schedule.save()

        # Set success message
        messages.success(request, "Refund successful")
        return redirect('refund_fund', district_transaction_id=district_transaction_id)

    # If the request method is not POST, render the refund form
    return render(request, 'member/refund.html')

# @login_required(login_url='/login/')  # Redirects to login page if user is not authenticated
def group_members(request):
    user = request.user
    user_profile = Profile.objects.filter(user=user).first()
    if user_profile:
        try:
            member = Member.objects.filter(profile=user_profile).first()
            group = member.group
            group_members = Member.objects.filter(group=group).order_by('-profile__user__first_name',
                                                                        'profile__user__last_name')
            context = {
                'group_members': group_members,
                'group_name': group.name if group else None,
            }
        except Member.DoesNotExist:
            group = None
            group_members = None
            context = {
                'group_members': group_members,
                'group_name': None,
            }
    else:
        context = {
            'group_members': None,
            'group_name': None,
        }
    return render(request, 'member/member.html', context)





@login_required
def view_group_information(request):
    # Get the profile associated with the logged-in user
    try:
        profile = request.user.profile  # Assuming Profile has a one-to-one relationship with User
    except AttributeError:
        # If there's no associated Profile, return an error message
        return render(request, 'member/group_information.html', {'error_message': 'Profile not found.'})

    # Find the Member object associated with this profile
    try:
        member = Member.objects.get(profile=profile)
    except Member.DoesNotExist:
        # If there's no associated Member, return an error message
        return render(request, 'member/group_information.html', {'error_message': 'Member not found.'})

    # Retrieve the Group the Member belongs to
    group = member.group  # Since Member has a ForeignKey to Group

    # Prepare context data for the template
    context = {
        'group': group,
        'member': member,
    }

    # Render the group information template with the context data
    return render(request, 'member/group_information.html', context)

def view_group_transactions(request):
    # Find the group the current user belongs to
    member = Member.objects.filter(profile__user=request.user).first()

    if not member:
        # If the user is not associated with any group, deny access
        messages.error(request, "You do not belong to any group.")
        return redirect("login")  # Redirect to a safe place

    # Get the group from the member
    group = member.group

    # Retrieve the district transactions for the group
    transactions = DISTRICT_TRANSACTION.objects.filter(destination_account=group)

    # Retrieve the loan schedule for the group
    loan_schedule = LoanSchedule.objects.filter(group=group).first()

    # Calculate the penalty, if any
    penalty = Decimal(0)
    if loan_schedule:
        if not loan_schedule.returned and timezone.now() > loan_schedule.end_date:
            penalty = loan_schedule.calculate_penalty()

    # Render the template with the group, transactions, loan schedule, and penalty
    return render(
        request,
        'member/view_group_transactions.html',
        {
            'group': group,
            'transactions': transactions,
            'loan_schedule': loan_schedule,
            'penalty': penalty,
        }
    )


# views.py

def group_transaction_detail(request):
    # Retrieve the member and ensure they are part of the correct group
    member = get_object_or_404(Member, profile=request.user.profile)
    group = member.group

    # Retrieve the specific transaction for this member
    try:
        transaction = ReturnTransaction.objects.get(group_account__group=group)
    except ReturnTransaction.DoesNotExist:
        messages.error(request, "Transaction not found or you do not have permission to view this transaction.")
        return redirect('member_dashboard')

    # Prepare QR code data
    qr_data = f"Transaction ID: {transaction.id}\nAmount: {transaction.amount}\nGroup: {transaction.member.group.name}"
    qr = qrcode.make(qr_data)
    img_io = BytesIO()
    qr.save(img_io, 'PNG')
    img_io.seek(0)
    qr_code_img = base64.b64encode(img_io.getvalue()).decode()

    # Pass transaction and QR code image to the template
    context = {
        'transaction': transaction,
        'qr_code_img': qr_code_img,
    }

    return render(request, 'member/transaction_detail.html', context)

def download_transaction_slip(request, transaction_id):
    # Ensure the user is logged in and retrieve their member profile
    member = get_object_or_404(Member, profile=request.user.profile)
    group = member.group

    # Retrieve the specific group account for this member
    group_account = GroupAccount.objects.get(group=group)

    # Retrieve the specific transaction for this member
    transaction = ReturnTransaction.objects.filter(id=transaction_id, group_account=group_account).first()
    if not transaction:
        messages.error(request, "Transaction not found or you do not have permission to view this transaction.")
        return redirect('member_dashboard')

    qr_data = f"Transaction ID: {transaction.id}\nAmount: {transaction.amount}\nGroup: {transaction.member.group.name}"

    # Generate QR code
    qr = qrcode.make(qr_data)
    qr_io = BytesIO()
    qr.save(qr_io, 'PNG')
    qr_io.seek(0)
    qr_image = Image(qr_io, 1*inch, 1*inch)  # Adjust the size as needed

    # Create a PDF
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Transaction data
    data = [
        ["Transaction ID", transaction.id],
        ["Amount", transaction.amount],
        ["Group", transaction.member.group.name],
        ["Date Created", transaction.date_created.strftime("%Y-%m-%d %H:%M:%S")],
        ["QR Code", qr_image]
    ]

    # Create a table
    table = Table(data, colWidths=[2 * inch, 4 * inch])

    # Style the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    table.setStyle(style)

    # Build the PDF
    elements = [table]
    doc.build(elements)

    # Serve the PDF as a downloadable file
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="transaction_{transaction.id}_slip.pdf"'
    return response