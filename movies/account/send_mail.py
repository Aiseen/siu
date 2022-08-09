from django.core.mail import send_mail


def send_confirmation_email(code: object, email: object) -> object:
    full_link = f'http://localhost:8000/api/v1/account/active/{code}'
    send_mail(
        'Кино от Айсена',
        full_link,
        'sagynbaevajsen@gmail.com',
        [email]
    )