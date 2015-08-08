__author__ = 'jason.a.parent@gmail.com (Jason Parent)'

# Django imports...
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

# Local imports...
from .apis import ApartmentAPIView

admin.autodiscover()

urlpatterns = [
    url(r'^$', ApartmentAPIView.as_view()),
]
