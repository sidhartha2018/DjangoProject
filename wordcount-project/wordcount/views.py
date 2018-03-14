from django.http import HttpResponse
from django.shortcuts import render

def Homepage(request):
    return render(request,'home.html',{'Hey':'I love you Man'})

def Page1(request):
      return HttpResponse('<h3>This is from Page1</h3>')
