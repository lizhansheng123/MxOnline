# _*_ ecoding:utf-8 _*_
from django.shortcuts import render

# Create your views here.
from .models import UserMessage


def getform(request):
    all_messages = UserMessage.objfv  ects.all()
    for message in all_messages:
        id = message.object_id

        print(id)
        print(message.name)

    return render(request, 'course_form.html')
