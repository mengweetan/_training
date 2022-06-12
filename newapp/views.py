from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def TestView(request):
    #return HttpResponse("This is my first django views")
    mydictionary = {"key":"value"}
    return JsonResponse(mydictionary)

from django.template.response import TemplateResponse

def AnotherView(request):
    response = TemplateResponse(request, 'another_template.html', {})
    # Register the callback

    # Return the response
    return response

def RenderView(request):
    student= {'firstname': 'david', 'lastname': 'chua'}

    context= {
        'person1': student,
        'interest':"apple computer",

        }
    return render(request, 'rendered.html', context)

# lesson 4
# https://docs.djangoproject.com/en/4.0/topics/class-based-views/intro/
from django.views import View

class MyClassView(View):
    def get(self, request):
        # <view logic>
        print ("whatever you like")
        return HttpResponse('result')
