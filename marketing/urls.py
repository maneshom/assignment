from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .views import ContactListView, ComposeView, EmailListView, ContactCreate, ContactUpdate, ContactDelete, DraftListView, DraftDelete
from django.contrib.auth.decorators import login_required

app_name = 'marketing'
urlpatterns = [

    path('contacts/', login_required(ContactListView.as_view()), name='contact-list'),
    path('drafts/', login_required(DraftListView.as_view()), name='draft-list'),
    path('contact/add/', login_required(ContactCreate.as_view()), name='contact-add'),
    path('contact/<int:pk>/', login_required(ContactUpdate.as_view()), name='contact-update'),
    path('contact/<int:pk>/delete/', login_required(ContactDelete.as_view()), name='contact-delete'),
    path('draft/<int:pk>/delete/', login_required(DraftDelete.as_view()), name='draft-delete'),
    path('emails/', login_required(EmailListView.as_view()), name='email-list'),
    path('compose/<int:draft_pk>', login_required(ComposeView.as_view()), name='compose'),
    path('', login_required(TemplateView.as_view(template_name='marketing/home.html')), name='home'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='marketing/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/marketing/accounts/login/'), name='logout'),
]
