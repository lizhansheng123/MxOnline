from django.shortcuts import render

# Create your views here.

def getForm(request):
    return render(request,'course_form.html')