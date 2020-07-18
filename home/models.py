from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class Base(TimeStampedModel):

    class Meta:
        abstract = True


def send_email(message):

    try:
        send_grid = SendGridAPIClient(settings.SEND_GRID_API_KEY)
        response = send_grid.send(message)

        if int(response.status_code) in [200, 201, 202]:
            result = True
        else:
            result = False

    except Exception as e:
        result = False

    return result


class EmailQueryset(models.QuerySet):

    def get_success_emails(self):
        return self.filter(is_success=True)


class Email(Base):
    email = models.EmailField()
    is_success = models.BooleanField(default=False)

    objects = EmailQueryset.as_manager()

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.email}'

    def send_email(self):
        message = Mail(
            from_email=settings.FROM_EMAIL,
            to_emails=self.email,
            subject='Send Grid email',
            html_content=f'<strong>Email generated at {self.created}'
        )
        self.is_success = send_email(message)
        self.save()
