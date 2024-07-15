from django.conf import settings
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template.loader import get_template
from xhtml2pdf import pisa
from ..SMS import *
from django.db.models import Sum,Count
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from ..models.accont_model import *
from ..models.user_model import *
from django.core.exceptions import ObjectDoesNotExist
import os

# Ensure the Group model is imported correctly
from ..models.accont_model import Group  # Adjust to the correct import path



def link_callback(uri, rel):
    if uri.startswith('file://'):
        uri = uri.replace('file://', '')
    elif settings.STATIC_URL and uri.startswith(settings.STATIC_URL):
        uri = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ""))
    elif settings.MEDIA_URL and uri.startswith(settings.MEDIA_URL):
        uri = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    return uri


# Render a PDF with information for all groups
def group_pdf_view(request):
    groups = Group.objects.all()  # Fetch all groups

    if not groups:
        return HttpResponse("No group information found.")

    template_path = 'administrative_secretary/user_print.html'  # Template name
    context = {'groups': groups}  # Pass all groups to the context
    template = get_template(template_path)
    html = template.render(context)  # Render the template with context data

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="group_report.pdf"'

    # Create PDF with proper error handling
    pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)

    if pisa_status.err:
        return HttpResponse(f"Error generating PDF: {pisa_status.err}.")

    return response

def view_unreturned_loans(request):
    # Retrieve loan schedules for unreturned loans
    unreturned_loans = LoanSchedule.objects.filter(returned=False)

    # Pagination
    paginator = Paginator(unreturned_loans, 10)  # Show 10 unreturned loans per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pass the data to the template
    return render(request, 'administrative_secretary/unreturned_loans.html', {'page_obj': page_obj})

def is_administrative_secretary(user):
    try:
        profile = user.profile
        return profile.role == 'Administrative-Secretary'
    except AttributeError:
        return False


def view_returned_loans(request):
    # Retrieve loan schedules for groups that have received a loan and have returned it
    returned_loans = LoanSchedule.objects.filter(returned=True)

    # Pagination
    paginator = Paginator(returned_loans, 10)  # Show 10 loans per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pass the data to the template
    return render(request, 'administrative_secretary/returned_loans.html', {'page_obj': page_obj})


def administrative_secretary_dashboard(request):
    groups_list = Group.objects.all()
    total_balance = DISTRICT_ACCOUNT.objects.aggregate(Sum('balance_amount'))['balance_amount__sum']
    total_groups = Group.objects.aggregate(Count('id'))['id__count']
    # Calculate total amount transferred from all district accounts
    total_transfer_out = DISTRICT_TRANSACTION.objects.filter(transaction_type='transfer_out') \
        .aggregate(Sum('amount'))['amount__sum']

    total_beneficiary_groups = DISTRICT_TRANSACTION.objects.values('destination_account') \
        .distinct() \
        .aggregate(Count('destination_account'))['destination_account__count']

    return render(request, 'administrative_secretary/dashboard.html', {
        'total_balance': total_balance,
        'total_transfer_out': total_transfer_out,
        'groups_list': groups_list,
        'total_groups':total_groups,
        'total_beneficiary_groups':total_beneficiary_groups,
    })


# def transfer_money(request, group_id):
#     if request.method == 'POST':
#         amount = request.POST.get('amount')
#         from_account_id = request.POST.get('from_account')

#         try:
#             if not all([amount, from_account_id]):
#                 raise ValueError("Missing required fields.")

#             amount = Decimal(amount)  # Convert to Decimal
#             from_account = DISTRICT_ACCOUNT.objects.get(id=from_account_id)
#             to_account = GroupAccount.objects.filter(group_id=group_id).first()  # Ensure the group account exists

#             if not to_account:
#                 raise ValueError("No GroupAccount found for the given group.")

#             if from_account.balance_amount < amount:
#                 raise ValueError("Insufficient balance in the district account.")

#             with transaction.atomic():
#                 # Deduct the amount from the district account
#                 from_account.balance_amount -= amount
#                 from_account.save()

#                 # Add the amount to the group account
#                 to_account.balance += amount
#                 to_account.save()

#                 # Retrieve the profile and administrative secretary
#                 profile = Profile.objects.get(user=request.user)
#                 admin_profile = AdminstrativeSecretary.objects.filter(profile=profile).first()

#                 if not admin_profile:
#                     raise ValueError("Administrative Secretary not found.")

#                 # Create the district transaction
#                 district_transaction = DISTRICT_TRANSACTION(
#                     adminstrative_officer=admin_profile,
#                     amount=amount,
#                     transaction_type='transfer_out',
#                     from_account=from_account,
#                     destination_account=to_account.group
#                 )
#                 district_transaction.save()

#                 # Create the loan schedule with a defined return period (e.g., 30 days)
#                 start_date = datetime.now()  # When the transaction occurs
#                 loan_duration = 30  # 30 days to return the fund
#                 end_date = start_date + timedelta(days=loan_duration)

#                 loan_schedule = LoanSchedule(
#                     group=to_account.group,
#                     start_date=start_date,
#                     end_date=end_date,
#                     amount_received=amount,
#                     returned=False,
#                 )
#                 loan_schedule.save()

#             messages.success(request, "Transfer successful, loan schedule created!")
#             return redirect('display_district_transactions')  # Redirect to the district transactions page

#         except (ValueError, GroupAccount.DoesNotExist, DISTRICT_ACCOUNT.DoesNotExist) as error:
#             messages.error(request, str(error))
#             return redirect('transfer_money', group_id=group_id)  # Redirect back to the transfer page

#     try:
#         group = get_object_or_404(Group, id=group_id)
#     except Group.DoesNotExist:
#         messages.error(request, "Group not found.")
#         return redirect('display_groups_without_funds')  # Redirect to an error page

#     district_accounts = DISTRICT_ACCOUNT.objects.all()
#     return render(request, 'administrative_secretary/transfer_money.html', {'district_accounts': district_accounts, 'group_id': group_id, 'group': group})


def display_groups_without_funds(request):
    groups_without_funds = Group.objects.filter(
        ~Q(id__in=DISTRICT_TRANSACTION.objects.values('destination_account').distinct())
    )

    paginator = Paginator(groups_without_funds, 10)  # Display 10 groups per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Check if there are no groups
    no_groups_found = not groups_without_funds.exists()

    context = {
        'groups_without_funds': page_obj,
        'no_groups_found': no_groups_found
    }
    return render(request, 'administrative_secretary/groups_without_funds.html', context)


def display_groups_with_funds(request):
    # Fetch the groups that have received funds
    groups_with_funds = Group.objects.filter(
        Q(id__in=DISTRICT_TRANSACTION.objects.values('destination_account').distinct())
    )

    # Number of items per page (e.g., 4)
    items_per_page = 4

    # Create a paginator instance
    paginator = Paginator(groups_with_funds, items_per_page)

    # Get the current page number from the GET parameters; default to 1
    page_number = request.GET.get('page', 1)

    # Retrieve the corresponding page object
    page_obj = paginator.get_page(page_number)

    # Check if there are no groups
    no_groups_found = not groups_with_funds.exists()

    # Return the paginated results to the template
    return render(request, 'administrative_secretary/groups_with_funds.html', {
        'page_obj': page_obj,
        'no_groups_found': no_groups_found
    })


def view_groups(request):
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

    return render(request, 'administrative_secretary/groups.html',{'groups': groups})


def display_district_transactions(request):
    transactions = DISTRICT_TRANSACTION.objects.all()
    paginator = Paginator(transactions, 10)  # Show 10 transactions per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'administrative_secretary/district_transactions.html', {'page_obj': page_obj})


def link_callback(uri, rel):
    if uri.startswith('file://'):
        uri = uri.replace('file://', '')
    elif settings.STATIC_URL and uri.startswith(settings.STATIC_URL):
        uri = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ""))
    elif settings.MEDIA_URL and uri.startswith(settings.MEDIA_URL):
        uri = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    return uri


def generate_district_transactions_pdf(request):
    transactions = DISTRICT_TRANSACTION.objects.all()  # Fetch all district transactions

    if not transactions:
        return HttpResponse("No transactions found.")

    # Specify the template used to generate the PDF
    template_path = 'administrative_secretary/district_transactions_report.html'
    context = {
        'transactions': transactions,
        'request': request  # Include request for context
    }

    # Render the template to HTML
    template = get_template(template_path)
    html = template.render(context)

    # Create HTTP response with PDF content type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="district_transactions_report.pdf"'

    # Generate the PDF
    pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)

    # Handle errors during PDF generation
    if pisa_status.err:
        return HttpResponse(f"Error generating PDF: {pisa_status.err}.")

    return response


def cancel_transaction(request, transaction_id):
    # Retrieve the transaction
    transaction = get_object_or_404(DISTRICT_TRANSACTION, id=transaction_id)

    # Retrieve the group account and district account
    group_account = transaction.from_account
    district_account = DISTRICT_ACCOUNT.objects.first()  # Assuming there's only one district account

    # Retrieve the amount transferred in the transaction
    amount_transferred = transaction.amount

    # Create a return transaction to track the return of funds
    ReturnTransaction.objects.create(
        member=None,  # Not associated with a specific member
        amount=amount_transferred,
        group_account=group_account,
        district_transaction=transaction
    )

    # Update the group account balance by subtracting the transferred amount
    group_account.balance -= amount_transferred
    group_account.save()

    # Update the district account balance by adding the transferred amount
    district_account.balance_amount += amount_transferred
    district_account.save()

    # Delete the transaction
    transaction.delete()

    # Redirect back to the page displaying transactions
    return redirect('display_transactions')



def format_phone_number(phone_number):
    """
    Ensure the phone number starts with the country code +255 for Tanzania.
    Strip any leading 0 and add the country code.
    """
    if phone_number.startswith('0'):
        phone_number = '255' + phone_number[1:]
    elif not phone_number.startswith('255'):
        phone_number = '255' + phone_number
    
    return phone_number

def get_group_members_phones(group_id):
    members = Member.objects.filter(group_id=group_id).select_related('profile')
    phones = [format_phone_number(member.profile.phone) for member in members]
    return phones

def send_group_message(group_id, message):
    phones = get_group_members_phones(group_id)
    response = send_sms(phones, message)
    return response


def transfer_money(request, group_id):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        from_account_id = request.POST.get('from_account')

        try:
            if not all([amount, from_account_id]):
                raise ValueError("Missing required fields.")

            amount = Decimal(amount)  # Convert to Decimal
            from_account = DISTRICT_ACCOUNT.objects.get(id=from_account_id)
            to_account = GroupAccount.objects.filter(group_id=group_id).first()  # Ensure the group account exists

            if not to_account:
                raise ValueError("No GroupAccount found for the given group.")

            if from_account.balance_amount < amount:
                raise ValueError("Insufficient balance in the district account.")

            with transaction.atomic():
                # Deduct the amount from the district account
                from_account.balance_amount -= amount
                from_account.save()

                # Add the amount to the group account
                to_account.balance += amount
                to_account.save()

                # Retrieve the profile and administrative secretary
                profile = Profile.objects.get(user=request.user)
                admin_profile = AdminstrativeSecretary.objects.filter(profile=profile).first()

                if not admin_profile:
                    raise ValueError("Administrative Secretary not found.")

                # Create the district transaction
                district_transaction = DISTRICT_TRANSACTION(
                    adminstrative_officer=admin_profile,
                    amount=amount,
                    transaction_type='transfer_out',
                    from_account=from_account,
                    destination_account=to_account.group
                )
                district_transaction.save()

                # Create the loan schedule with a defined return period (e.g., 30 days)
                start_date = datetime.now()  # When the transaction occurs
                loan_duration = 30  # 30 days to return the fund
                end_date = start_date + timedelta(days=loan_duration)

                loan_schedule = LoanSchedule(
                    group=to_account.group,
                    start_date=start_date,
                    end_date=end_date,
                    amount_received=amount,
                    returned=False,
                )
                loan_schedule.save()

                # Send SMS notification to group members
                message = f"An amount of {amount} has been deposited to your group account."
                send_group_message(group_id, message)

            messages.success(request, "Transfer successful, loan schedule created, and members notified!")
            return redirect('display_district_transactions')  # Redirect to the district transactions page

        except (ValueError, GroupAccount.DoesNotExist, DISTRICT_ACCOUNT.DoesNotExist) as error:
            messages.error(request, str(error))
            return redirect('transfer_money', group_id=group_id)  # Redirect back to the transfer page

    try:
        group = get_object_or_404(Group, id=group_id)
    except Group.DoesNotExist:
        messages.error(request, "Group not found.")
        return redirect('display_groups_without_funds')  # Redirect to an error page

    district_accounts = DISTRICT_ACCOUNT.objects.all()

    return render(request, 'administrative_secretary/transfer_money.html', {'district_accounts': district_accounts, 'group_id': group_id, 'group': group})



def generate_all_loans_return_pdf(request):
    groups = Group.objects.filter(loanschedule__returned=True).distinct()

    # Fetch all loan schedules for the groups
    loan_schedules = LoanSchedule.objects.filter(group__in=groups, returned=True)

    # Rendered HTML template
    template_path = 'administrative_secretary/loan_return_pdf_template.html'
    context = {'loan_schedules': loan_schedules}

    # Create a Django response object
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="all_returned_loans.pdf"'

    # Create a PDF
    template = get_template(template_path)
    html = template.render(context)

    # Create PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response


def generate_all_not_returned_loans_pdf(request):
    groups = Group.objects.filter(loanschedule__returned=False).distinct()

    # Fetch all loan schedules for the groups that have not returned loans
    loan_schedules = LoanSchedule.objects.filter(group__in=groups, returned=False)

    # Rendered HTML template
    template_path = 'administrative_secretary/all_not_returned_loans_pdf.html'
    context = {'loan_schedules': loan_schedules}

    # Create a Django response object
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="all_not_returned_loans.pdf"'

    # Create a PDF
    template = get_template(template_path)
    html = template.render(context)

    # Create PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response