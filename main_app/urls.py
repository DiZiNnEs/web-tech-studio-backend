from django.urls import path

from main_app.views import IndexView, ServicesView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('services/', ServicesView.as_view(), name='services'),
]
