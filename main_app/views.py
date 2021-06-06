from django.shortcuts import render
from django.views.generic import TemplateView, FormView


class IndexView(TemplateView):
    template_name = 'main_app/index.html'


class FeedbackFormView(TemplateView):
    template_name = 'main_app/services.html'
