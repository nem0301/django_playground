from django.shortcuts import render

# Create your views here.

def index(request):
    template = {}
    return render(request, 'test_app/index.html', template)

def str_param(request, param):
    template = {}
    template['param_type'] = str(type(param))
    template['param'] = param

    return render(request, 'test_app/str_param.html', template)

def int_param(request, param):
    template = {}
    template['param_type'] = str(type(param))
    template['param'] = param

    return render(request, 'test_app/int_param.html', template)