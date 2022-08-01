from django.template.response import TemplateResponse
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .serializers import StudentSerializer
from .models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class Login(APIView):

    permission_classes = (permissions.AllowAny,)
    #permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        context = {}
        data = request.data
        print(data)
        if data.get("id") == "mw" and data.get("pw") == "password":
            print('ok')
            user = User.objects.get(username='mw')
            token, _ = Token.objects.get_or_create(user=user)
            context["token"] = token.key

        return Response(context)


class ChangeData(APIView):
    #permission_classes = (permissions.AllowAny,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        #print("changeData-post")
        data = request.data

        name = data.get("name")
        student = Student.objects.get(name=name)
        print(student)
        student.name = "NotMary"
        student.save()
        data = {"result": "name changed"}
        context = {"message": data}
        return Response(context)


class StudentViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    Headers should be set as
    Content-Type: application/json
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        students = Student.objects.all()
        context = {}
        context['data'] = StudentSerializer(students, many=True).data
        return Response(context)

    def post(self, request, format=None):
        context = {'action': 'post'}
        """
        {"name":"mengwee"}
        """
        data = request.data

        print(data)
        try:
            name = data["name"]
            new_student = Student()
            new_student.name = name
            new_student.save()
            context['remark'] = f"New student name is {name}"
        except:
            context['remark'] = "error"
        return Response(context)

    def put(self, request, format=None):
        context = {'action': 'put'}
        """
        {"name":"mengwee",
        "new_name":"tanmengwee"}
        """
        data = request.data
        print(data)
        try:
            name = data["name"]
            students = Student.objects.filter(name=name)
            existing_student = students[0]
            existing_student.name = data["new_name"]
            existing_student.save()
            context['remark'] = f"Student new name is {existing_student.name}"
        except:
            context['remark'] = "error"
        return Response(context)

    def delete(self, request, format=None):
        context = {'action': 'delete'}
        """
        {"name":"mengwee"}
        """
        data = request.data
        print(data)
        try:
            name = data["name"]
            students = Student.objects.filter(name=name)
            existing_student = students[0]

            # another method
            existing_student = Student.objects.get(name=name)

            existing_student.delete()
            context['remark'] = f"Deleted student whese name is {name}"
        except:
            context['remark'] = "error"
        return Response(context)


def TestView(request):
    #return HttpResponse("This is my first django views")
    mydictionary = {"key": "value"}
    return JsonResponse(mydictionary)


def AnotherView(request):
    response = TemplateResponse(request, 'another_template.html', {})
    # Register the callback

    # Return the response
    return response


def RenderView(request):
    student = {'firstname': 'david', 'lastname': 'chua'}

    context = {
        'person1': student,
        'interest': "apple computer",

        }
    return render(request, 'rendered.html', context)


# lesson 4
# https://docs.djangoproject.com/en/4.0/topics/class-based-views/intro/


class MyClassView(View):
    def get(self, request):
        aaa = 123
        bbb = 456
        print(aaa+bbb)
        # <view logic>
        print("whatever you like")
        return HttpResponse('result')


class MyFormView(View):
    from .forms import myTestForm

    form_class = myTestForm

    template_name = 'form_template.html'

    def get(self, request):
        # <view logic>
        context = {}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        from .models import Student

        if form.is_valid():
            # <process form cleaned data>
            name = form.cleaned_data['name']

            student = Student()
            student.name = name
            student.save()

            mydictionary = {"key": "value"}
            return JsonResponse(mydictionary)

        return render(request, self.template_name, {'form': form})
        return render(request, self.template_name, {'form': form})
