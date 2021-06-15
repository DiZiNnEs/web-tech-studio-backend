from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.conf import settings
from django.core.mail import send_mail

from main_app.forms import CustomerForm
from main_app.models import Project


class IndexView(CreateView):
    template_name = 'main_app/index.html'
    form_class = CustomerForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['first_six_projects'] = Project.objects.all()[:3]
        context['second_six_projects'] = Project.objects.all()[4:6]
        context['our_project'] = Project.objects.all()[:4]
        return context

    def form_valid(self, form):
        username = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')

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

        super().form_valid(form)
        return redirect(self.success_url)


class ServicesView(TemplateView):
    template_name = 'main_app/services.html'
