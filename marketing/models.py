from django.db import models
from django.urls import reverse_lazy
# Create your models here.


class Draft(models.Model):
    subject = models.TextField()
    body = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class Contact(models.Model):
    RECIPIENT_TYPE_CHOICE = (
        ('CUS', 'Customer'),
        ('SUB', 'Subscriber'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    recipient_type = models.CharField(choices=RECIPIENT_TYPE_CHOICE, max_length=3)

    def get_absolute_url(self):
        # return reverse('contact-detail', kwargs={'pk': self.pk})
        return reverse_lazy('marketing:contact-list')

    def __str__(self):
        return self.email


class EmailSent(models.Model):
    contact = models.ManyToManyField(Contact)
    body = models.TextField(blank=True)
    subject = models.CharField(max_length=200)
    sent_on = models.DateTimeField(auto_now=True)
    from_address = models.EmailField()

    def __str__(self):
        return self.from_address
