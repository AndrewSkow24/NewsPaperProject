from django.conf import settings
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.http import HttpResponse


class HomePageView(TemplateView):
    template_name = "home.html"


def test_email(request):
    send_mail(
        "Тема рассылки",
        "Сообщение письма",
        "andrewskow@yandex.ru",
        [
            "anjeie24@mail.ru",
        ],
        fail_silently=False,
    )
    return HttpResponse("Message was send")
