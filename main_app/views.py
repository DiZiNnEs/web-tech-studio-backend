from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from django.conf import settings
from django.core.mail import send_mail


class IndexView(View):
    template_name = 'main_app/index.html'

    def get(self, request):
        return render(request, template_name=self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        title = request.POST.get('title')
        desc = request.POST.get('desk')

        subject = 'IT - WebTech studio'
        message = f'''
            Здравствуйте, {username}!
            Благодарю за заявку! В скором времени мы ответим на неё.
            
            С уважением,
            Х.
        '''
        email_from = settings.EMAIL_HOST_USER
        recipients = [email, ]
        send_mail(subject=subject, message=message, from_email=email_from, recipient_list=recipients)
        return redirect('/')


class ServicesView(TemplateView):
    template_name = 'main_app/services.html'
