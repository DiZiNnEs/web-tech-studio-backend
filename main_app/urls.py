from django.urls import path

from main_app.views import IndexView, FeedbackFormView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('services/', FeedbackFormView.as_view(), name='services'),
]
