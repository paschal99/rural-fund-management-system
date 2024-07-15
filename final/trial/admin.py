from django.contrib import admin
from .models.accont_model import (
    DISTRICT_ACCOUNT,
    Ward,
    Village,
    GroupAccount,
    Group,
    AdminstrativeSecretary,
    Member,
    DevelopmentOfficer,
    Notification,
    GroupTransaction,
    DISTRICT_TRANSACTION,
    ReturnTransaction,
    LoanSchedule
)
from .models.user_model import Profile

# Custom admin class for Profile
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'role', 'sex')  # Display useful fields in the list view
    search_fields = ('user__username', 'phone')  # Allow searching by user name and phone
    list_filter = ('role', 'sex')  # Optional filters for role and sex


# Register all models in the admin interface
admin.site.register(Profile, ProfileAdmin)  # Register Profile with the custom admin class


# Custom admin classes for adding search and list display functionality

class DISTRICT_ACCOUNT_Admin(admin.ModelAdmin):
    list_display = ('name', 'account_name', 'account_number', 'balance_amount')
    search_fields = ('name', 'account_name', 'account_number')

class LoanSchedule_Admin(admin.ModelAdmin):
    list_display = ('group', 'amount_received', 'start_date', 'end_date', 'returned')
    search_fields = ('returned', 'group', 'amount_received')


class WardAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class VillageAdmin(admin.ModelAdmin):
    list_display = ('name', 'ward')
    search_fields = ('name', 'ward__name')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'group_account', 'total_members', 'village', 'created_at')
    search_fields = ('name', 'group_account')
    list_filter = ('village', 'created_at')


class AdminstrativeSecretaryAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'profile')
    search_fields = ('employee_id', 'profile__user__username')


class MemberAdmin(admin.ModelAdmin):
    list_display = ('profile', 'group', 'position')
    search_fields = ('profile__user__username', 'group__name', 'position')


class DevelopmentOfficerAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'profile')
    search_fields = ('employee_id', 'profile__user__username')


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'Member', 'content', 'date_created')
    search_fields = ('user__profile__user__username', 'Member__profile__user__username')


class GroupTransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_type', 'group', 'amount', 'date_created')
    search_fields = ('transaction_type', 'group__name')
    list_filter = ('transaction_type', 'date_created')


class GroupAccountAdmin(admin.ModelAdmin):
    list_display = ('group', 'balance')
    search_fields = ('group',)


class DISTRICT_TRANSACTION_Admin(admin.ModelAdmin):
    list_display = ('transaction_type', 'adminstrative_officer', 'amount', 'from_account', 'destination_account', 'date_created')
    search_fields = ('transaction_type', 'sponsor__profile__user__username', 'from_account__name', 'destination_account__name')
    list_filter = ('transaction_type', 'date_created')

class ReturnTransactionAdmin(admin.ModelAdmin):
    # Define the fields you want to display in the admin interface
    list_display = ['member', 'amount', 'group_account', 'district_transaction', 'date_created']
    # Optionally, you can add filters, search fields, and readonly fields

admin.site.register(ReturnTransaction, ReturnTransactionAdmin)
admin.site.register(LoanSchedule, LoanSchedule_Admin)
admin.site.register(DISTRICT_ACCOUNT, DISTRICT_ACCOUNT_Admin)
admin.site.register(Ward, WardAdmin)
admin.site.register(Village, VillageAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(AdminstrativeSecretary, AdminstrativeSecretaryAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(DevelopmentOfficer, DevelopmentOfficerAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(GroupTransaction, GroupTransactionAdmin)
admin.site.register(GroupAccount, GroupAccountAdmin)
admin.site.register(DISTRICT_TRANSACTION, DISTRICT_TRANSACTION_Admin)
