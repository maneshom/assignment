from django import forms
from .models import EmailSent, Draft
from django.core.mail import send_mail


class SentEmailForm(forms.ModelForm):
    class Meta:
        model = EmailSent
        fields = ('from_address', 'contact', 'subject', 'body')

    def send_email(self):    # send email using the self.cleaned_data dictionary
        data = self.cleaned_data
        from_address = data['from_address']
        subject = data['subject']
        body = data['body']
        recipient_list = [x for x in data['contact'].values_list('email', flat=True)]
        send_mail(
            subject,
            body,
            from_address,
            recipient_list,
            fail_silently=False,
        )
        self.save(commit=True)

    def save_email(self):    # save email subject and body using the self.cleaned_data dictionary
        data = self.cleaned_data
        subject = data['subject']
        body = data['body']
        draft_obj = Draft(subject=subject, body=body)
        draft_obj.save()
