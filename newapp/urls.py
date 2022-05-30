from django.views.generic import TemplateView
from django.urls import path, include
urlpatterns = [

    path('about/', TemplateView.as_view(template_name="about.html")),
]
