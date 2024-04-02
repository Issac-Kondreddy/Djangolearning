from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('allmembers.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        'mymember':mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render({}, request))

def testing(request):
    #mydata = Member.objects.all().values()
    #mydata = Member.objects.all().order_by('firstname').values()
    #mydata = Member.objects.all().order_by('-firstname').values()
    mydata = Member.objects.all().order_by('lastname', '-id').values()
    template = loader.get_template('template.html')
    context = {
        'fruits': ['apple', 'banana', 'orange'],
    }
    return HttpResponse(template.render(context, request))