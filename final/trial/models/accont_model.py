from datetime import timedelta
from django.utils import timezone
from decimal import Decimal
from .user_model import *
from django.db.models import F
from django.db import models
from datetime import timedelta


class DISTRICT_ACCOUNT(models.Model):
    name = models.CharField(max_length=20)
    account_name = models.CharField(max_length=20)
    account_number = models.CharField(max_length=30)
    balance_amount = models.IntegerField(default=0,)

    class Meta:
        db_table = 'District'

    def __str__(self):
        return str(self.name)


class Ward(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'Ward'

    def __str__(self):
        return str(self.name)


class Village(models.Model):
    name = models.CharField(max_length=20)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Village'

    def __str__(self):
        return str(self.name)


class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now=True)
    group_account = models.CharField(max_length=20)
    total_members = models.IntegerField(default=0)
    group_no = models.IntegerField(default=0)
    village = models.ForeignKey('Village', on_delete=models.CASCADE, null=True, blank=True)
    constitution = models.FileField(upload_to='group_constitution/', blank=True,
                                    null=True)  # New field for file upload

    class Meta:
        db_table = 'Group'

    def __str__(self):
        return f"{self.name} - {self.group_account}"


class AdminstrativeSecretary(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=50)

    class Meta:
        db_table = 'adminstrative_secretary'

    def __str__(self):
        return str(self.employee_id)


class Member(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    POSITION_CHOICE = (
        ('mwenyekiti', 'mwenyekiti'),
        ('mtunza_hazina', 'mtunza_hazina'),
        ('mwanachama', 'mwanachama')
    )
    position = models.CharField(choices=POSITION_CHOICE, max_length=14, default='mwanachama')

    class Meta:
        db_table = 'Member'

    def __str__(self):
        return str(self.profile)


class DevelopmentOfficer(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=50)

    class Meta:
        db_table = 'development_officers'

    def __str__(self):
        return str(self.employee_id)


class GroupAccount(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE, default=None)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = 'GroupAccount'

    def __str__(self):
        return str(self.group)


class Notification(models.Model):
    user = models.ForeignKey(AdminstrativeSecretary, on_delete=models.CASCADE)
    Member = models.ForeignKey(Member, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Notification'

    def __str__(self):
        return f"{self.group} - {self.date_created}"


class GroupTransaction(models.Model):
    TRANSACTION_TYPES = (
        ('deposit', 'Deposit'),
        ('transfer_in', 'Transfer In'),
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    account = models.ForeignKey(GroupAccount, on_delete=models.CASCADE, related_name='outgoing_transactions',
                                       blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'GroupTransaction'

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} - {self.date_created}"


class DISTRICT_TRANSACTION(models.Model):
    TRANSACTION_TYPES = (
        ('deposit', 'Deposit'),
        ('transfer_out', 'Transfer Out'),
    )
    adminstrative_officer = models.ForeignKey(AdminstrativeSecretary, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    from_account = models.ForeignKey(DISTRICT_ACCOUNT, on_delete=models.CASCADE)
    destination_account = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='incoming_transactions',
                                            blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'DISTRICT_TRANSACTION'

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} - {self.date_created}"

class LoanSchedule(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    amount_received = models.DecimalField(max_digits=10, decimal_places=2)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"Loan for {self.group.name}: {self.amount_received} due by {self.end_date}"

    def calculate_penalty(self):
        if self.returned:
            return Decimal(0)

        # Use timezone-aware datetime
        now = timezone.now()

        if now > self.end_date:
            # Calculate how many months overdue
            months_overdue = (now.year - self.end_date.year) * 12 + (now.month - self.end_date.month)

            # Apply 5% penalty for each month overdue
            penalty = self.amount_received * Decimal(0.05) * Decimal(months_overdue)
            return penalty
        else:
            return Decimal(0)


class ReturnTransaction(models.Model):
    # Define the necessary fields
    member = models.ForeignKey('Member', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    group_account = models.ForeignKey('GroupAccount', on_delete=models.CASCADE, default=1)
    district_transaction = models.ForeignKey('DISTRICT_TRANSACTION', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Ensure `group_account` exists
        if not self.group_account:
            raise ValueError("Group account is missing.")

        # Ensure `district_transaction` exists
        if not self.district_transaction:
            raise ValueError("District transaction is missing.")

        # Adjust the group account balance by subtracting the transaction amount
        group_account = self.group_account
        group_account.balance = F('balance') - self.amount
        group_account.save()

        # Adjust the district account balance by adding the transaction amount
        district_account = self.district_transaction.from_account
        district_account.balance_amount = F('balance_amount') + self.amount
        district_account.save()

        # Call the parent save method to save the current model instance
        super().save(*args, **kwargs)