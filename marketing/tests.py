from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from .models import EmailSent, Draft, Contact
# Create your tests here.


def login(self):
    self.user = User.objects.create_user(username='eight_user', password='test@ssignment')
    self.client.login(username='eight_user', password='test@ssignment')


class ContactViewTests(TestCase):
    def test_no_contacts(self):
        """
        If no contacts exist, an appropriate message is displayed.
        """
        login(self)
        response = self.client.get(reverse('marketing:contact-list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['object_list'], [])

    def test_add_contacts(self):
        """
        Add contact and redirect to contact list.
        """
        login(self)
        response = self.client.get(reverse('marketing:contact-add'))
        self.assertTemplateUsed(response, "marketing/contact_form.html")
        self.assertContains(response, "name")
        self.assertContains(response, "email")
        self.assertContains(response, "recipient_type")
        response = self.client.post(reverse('marketing:contact-add'),
                                    data={"name": "fred", "email": "subscriber@test.com", "recipient_type": "SUB", })
        self.assertEqual(Contact.objects.count(), 1)
        self.assertRedirects(response, reverse('marketing:contact-list'))


class EmailListViewTests(TestCase):
    def test_no_emails(self):
        """
        If no emails exist, an appropriate message is displayed.
        """
        login(self)
        response = self.client.get(reverse('marketing:email-list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['object_list'], [])

    def test_compose_email(self):
        """
        Compose email and redirect to email list.
        """
        login(self)
        response = self.client.get(reverse('marketing:compose', kwargs={'draft_pk': 0}))
        self.assertTemplateUsed(response, "marketing/compose.html")
        self.assertContains(response, "contact")
        self.assertContains(response, "body")
        self.assertContains(response, "subject")
        self.assertContains(response, "from_address")
        contact_obj = Contact.objects.create(name="tester", email="tester@gmail.com", recipient_type="SUB")
        response = self.client.post(reverse('marketing:compose', kwargs={'draft_pk': 0}),
                                    data={"contact": contact_obj.pk, "from_address": "test@from.com",
                                          "body": "test_body", "subject": "test_subject"
                                          })
        self.assertEqual(EmailSent.objects.count(), 1)
        self.assertRedirects(response, reverse('marketing:email-list'))


class DraftViewTests(TestCase):
    def test_no_draft(self):
        """
        If no draft emails exist, an appropriate message is displayed.
        """
        login(self)
        response = self.client.get(reverse('marketing:draft-list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['object_list'], [])


