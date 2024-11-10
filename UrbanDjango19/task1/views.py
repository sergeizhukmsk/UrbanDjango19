from django.shortcuts import render

def class_template(request):
    return render(request, 'second_task/class_template.html')

def func_template(request):
    return render(request, 'second_task/func_template.html')

