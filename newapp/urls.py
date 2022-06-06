from django.views.generic import TemplateView
from django.urls import path, include
from .views import TestView, AnotherView,RenderView
urlpatterns = [

    path('try/', TemplateView.as_view(template_name="about.html")),
    path('try2/', TestView, name='test'),
    path('try3/', AnotherView, name='another_view'),
    path('try4/', RenderView, name='render_view')
]
