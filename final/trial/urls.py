from django.urls import path
from .views import authentication, AdministrativeSecretary, memberview, DevelopmentOfficer
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='custom_password_reset.html'), name='password_reset'),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name='custom_password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='custom_password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='custom_password_reset_complete.html'), name='password_reset_complete'),

    path('index/', authentication.index, name='index'),
    path('register-group/', DevelopmentOfficer.register_group, name='register_group'),

    path('group_delete/<int:pk>/', DevelopmentOfficer.group_delete, name='group_delete'),

    path('group_search/', DevelopmentOfficer.group_search, name='group_search'),
    path('group_transaction_detail/', memberview.group_transaction_detail, name='qrcode'),
    path('group_transaction/<int:transaction_id>/download/', memberview.download_transaction_slip, name='download_transaction_slip'),

    path('register/', authentication.registration, name='register'),
    path('profile/update/', authentication.update_profile, name='update_profile'),

    path('', authentication.user_login, name='login'),
    # path('accounts/login/', authentication.user_login, name='login'),

    path('view_unreturned_loans/', AdministrativeSecretary.view_unreturned_loans, name='view_unreturned_loans'),

    path('view_returned_loans/', AdministrativeSecretary.view_returned_loans, name='view_returned_loans'),


    path('view_groups/',AdministrativeSecretary.view_groups, name='view_groups'),

    path('calculate_remaining_time/', memberview.calculate_remaining_time, name='calculate_remaining_time'),

    path('development_officer/register_member/', DevelopmentOfficer.register_member, name='register_member'),
    # Ensure case consistency
    path('group/<int:group_id>/members/', DevelopmentOfficer.list_group_members, name='member_list'),
    # Correct URL pattern
    path('member_dashboard/', memberview.member_dashboard, name='member_dashboard'),

    path('logout/', authentication.user_logout, name='logout'),
    path('refund_fund/<int:district_transaction_id>/',memberview.refund_fund, name='refund_fund'),
    path('group/<int:group_id>/constitution', DevelopmentOfficer.download_constitution, name='download_constitution'),
    path('transfer_money/<int:group_id>/', AdministrativeSecretary.transfer_money, name='transfer_money'),

    path('change_password/', authentication.change_password, name='change_password'),
    path('login_history/', DevelopmentOfficer.login_history, name='login_history'),
    path('members/', memberview.group_members, name='group_members'),

    path('generate_district_transactions_pdf/', AdministrativeSecretary.generate_district_transactions_pdf, name='generate_district_transactions_pdf'),
    path('group_transactions/', memberview.view_group_transactions, name='view_group_transactions'),

    path('display_district_transactions/',AdministrativeSecretary.display_district_transactions, name='display_district_transactions'),
    path('display_groups_without_funds/', AdministrativeSecretary.display_groups_without_funds, name='display_groups_without_funds'),
    path('view-your-member/', memberview.view_group_information, name='view_group_information'),
    path('render_pdf_view/', AdministrativeSecretary.group_pdf_view, name='group_pdf_view'),



    path('display_groups_with_funds/', AdministrativeSecretary.display_groups_with_funds, name='display_groups_with_funds'),
    path('adminstrative_view/', AdministrativeSecretary.administrative_secretary_dashboard, name='administrative_secretary_dashboard'),
    path('development_officer_dashboard/', DevelopmentOfficer.development_officer_dashboard, name='development_officer_dashboard'),
    path('transactions/<int:transaction_id>/cancel/', AdministrativeSecretary.cancel_transaction, name='cancel_transaction'),

    path('generate_all_loans_return_pdf/', AdministrativeSecretary.generate_all_loans_return_pdf, name='generate_all_loans_return_pdf'),
    path('generate_all_not_returned_loans_pdf/', AdministrativeSecretary.generate_all_not_returned_loans_pdf, name='generate_all_not_returned_loans_pdf'),

]
