from django.views.generic import ListView, UpdateView, FormView, CreateView, DeleteView
from django.core.exceptions import ObjectDoesNotExist
from .models import Contact, EmailSent, Draft
from .forms import SentEmailForm
from django.urls import reverse_lazy
# Create your views here.


class ContactListView(ListView):
    model = Contact

    def get_context_data(self, ** kwargs):
        context = super().get_context_data(** kwargs)
        return context


class DraftListView(ListView):
    model = Draft
    queryset = Draft.objects.all().order_by('-created_on')

    def get_context_data(self, ** kwargs):
        context = super().get_context_data(** kwargs)
        return context


class ContactCreate(CreateView):
    model = Contact
    fields = ['name', 'email', 'recipient_type']


class ContactUpdate(UpdateView):
    model = Contact
    fields = ['name', 'email', 'recipient_type']


class ContactDelete(DeleteView):
    model = Contact
    template_name = 'marketing/object_confirm_delete.html'
    success_url = reverse_lazy('marketing:contact-list')


class DraftDelete(DeleteView):
    model = Draft
    template_name = 'marketing/object_confirm_delete.html'
    success_url = reverse_lazy('marketing:draft-list')


class EmailListView(ListView):
    model = EmailSent
    queryset = EmailSent.objects.all().order_by('-sent_on')

    def get_context_data(self, ** kwargs):
        context = super().get_context_data(** kwargs)
        return context


class ComposeView(FormView):
    template_name = 'marketing/compose.html'
    form_class = SentEmailForm
    success_url = reverse_lazy('marketing:email-list')
    initial = {}

    def get_initial(self, **kwargs):
        initial = super().get_initial()

        # Get draft object and set subject and body otherwise create a new email
        try:
            obj = Draft.objects.get(pk=self.kwargs['draft_pk'])
            initial['subject'] = obj.subject
            initial['body'] = obj.body
        except ObjectDoesNotExist:
            pass

        return initial

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        if self.request.POST.get('draft', False):
            form.save_email()
        else:
            # It should return an HttpResponse.
            form.send_email()
        return super().form_valid(form)
